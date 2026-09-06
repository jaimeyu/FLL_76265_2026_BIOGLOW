#!/usr/bin/env python3
"""
FLL Team 76265 - PII Leak Scanner
Scans repository files for leaks of Personally Identifiable Information (PII)
(emails, phone numbers, SSNs, credit cards) while respecting an exception list.
"""

import sys
import os
import re
import json
import subprocess
from pathlib import Path

# Default PII regex patterns
PATTERNS = {
    "Email Address": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
    "Phone Number": re.compile(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'),
    "Social Security Number (SSN)": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    "Credit Card Number": re.compile(r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b')
}

def load_config(config_path=".pii-exceptions.json"):
    if not os.path.exists(config_path):
        return {
            "allowed_emails": [],
            "allowed_keywords": [],
            "excluded_file_patterns": [r'\.git/.*', r'\.pii-exceptions\.json$']
        }
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_git_files(repo_root):
    try:
        cmd = ["git", "ls-files"]
        result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True, check=True)
        files = result.stdout.strip().splitlines()
        return [f for f in files if os.path.isfile(os.path.join(repo_root, f))]
    except Exception:
        # Fallback to directory walk if git fails
        all_files = []
        for root, _, filenames in os.walk(repo_root):
            if '.git' in root:
                continue
            for name in filenames:
                rel_path = os.path.relpath(os.path.join(root, name), repo_root)
                all_files.append(rel_path)
        return all_files

def is_excluded(filepath, excluded_patterns):
    for pattern in excluded_patterns:
        if re.search(pattern, filepath):
            return True
    return False

def scan_file(filepath, repo_root, config):
    full_path = os.path.join(repo_root, filepath)
    allowed_emails = set(config.get("allowed_emails", []))
    
    findings = []
    
    try:
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_no, line in enumerate(f, 1):
                # Skip comments or code instructions that explicitly mention pattern examples in scanner
                if "PATTERNS =" in line or "PII Leak Scanner" in line:
                    continue
                
                for pii_type, pattern in PATTERNS.items():
                    matches = pattern.findall(line)
                    for match in matches:
                        # Check allowed email exceptions
                        if pii_type == "Email Address" and match in allowed_emails:
                            continue
                        
                        # Filter out common false positives (e.g. standard CSS or HTML versions/hex colors)
                        if pii_type == "Phone Number" and (match.startswith("0.0.") or "127.0.0.1" in match):
                            continue

                        findings.append({
                            "type": pii_type,
                            "file": filepath,
                            "line": line_no,
                            "match": match,
                            "snippet": line.strip()
                        })
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)

    return findings

def main():
    repo_root = os.getcwd()
    config_path = os.path.join(repo_root, ".pii-exceptions.json")
    config = load_config(config_path)
    
    excluded_patterns = config.get("excluded_file_patterns", [])
    files_to_scan = get_git_files(repo_root)
    
    all_findings = []
    
    for rel_path in files_to_scan:
        if is_excluded(rel_path, excluded_patterns):
            continue
        findings = scan_file(rel_path, repo_root, config)
        all_findings.extend(findings)
        
    if all_findings:
        print("\n❌ PII LEAK DETECTED! Safety Policy Violation:", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        for item in all_findings:
            print(f"[{item['type']}] {item['file']}:{item['line']}", file=sys.stderr)
            print(f"  Match:   {item['match']}", file=sys.stderr)
            print(f"  Snippet: {item['snippet']}", file=sys.stderr)
            print("-" * 60, file=sys.stderr)
        print("\nPlease remove the sensitive PII or add allowed items to .pii-exceptions.json if authorized.", file=sys.stderr)
        sys.exit(1)
    else:
        print("✅ PII Leak Scan Passed: Zero un-whitelisted PII leaks detected.")
        sys.exit(0)

if __name__ == "__main__":
    main()
