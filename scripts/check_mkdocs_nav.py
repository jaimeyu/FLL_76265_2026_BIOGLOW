#!/usr/bin/env python3
"""
Validates that all documentation files referenced in mkdocs.yml:
1. Actually exist on disk in docs_dir.
2. Are tracked in git (or staged for commit) so they don't break GitHub Actions CI (mkdocs build --strict).
3. If mkdocs is installed locally, optionally executes 'mkdocs build --strict'.
"""

import os
import re
import subprocess
import sys
import tempfile


def main():
    repo_root = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True
    ).stdout.strip()

    if not repo_root:
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    mkdocs_file = os.path.join(repo_root, "mkdocs.yml")
    if not os.path.exists(mkdocs_file):
        print("⚠️ mkdocs.yml not found, skipping documentation navigation check.")
        return 0

    with open(mkdocs_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine docs_dir (default: 'docs', this repo uses 'doc')
    docs_dir_match = re.search(r"^docs_dir:\s*([^\s#]+)", content, re.MULTILINE)
    docs_dir_name = docs_dir_match.group(1) if docs_dir_match else "docs"
    docs_dir = os.path.join(repo_root, docs_dir_name)

    # Extract nav section
    nav_match = re.search(r"\nnav:\s*\n(.*)", content, re.DOTALL)
    if not nav_match:
        print("⚠️ No 'nav' section found in mkdocs.yml.")
        return 0

    nav_text = nav_match.group(1)

    # Extract all file targets (anything ending in .md or .html or images, excluding web URLs)
    file_candidates = re.findall(r":\s*([^\s#]+\.(?:md|html))", nav_text)

    # Get list of staged files in git
    staged_res = subprocess.run(
        ["git", "diff", "--name-only", "--cached"],
        cwd=repo_root,
        capture_output=True,
        text=True
    )
    staged_files = set(filter(None, staged_res.stdout.strip().splitlines()))

    errors = []

    for rel_path in file_candidates:
        if rel_path.startswith("http://") or rel_path.startswith("https://"):
            continue

        full_disk_path = os.path.join(docs_dir, rel_path)
        git_rel_path = os.path.join(docs_dir_name, rel_path)

        # 1. Check if file exists on disk
        if not os.path.exists(full_disk_path):
            errors.append(f"❌ Missing on disk: '{git_rel_path}' (referenced in mkdocs.yml nav)")
            continue

        # 2. Check if file is tracked in git or staged for commit
        is_staged = git_rel_path in staged_files
        is_tracked = False

        tracked_res = subprocess.run(
            ["git", "ls-files", "--error-unmatch", git_rel_path],
            cwd=repo_root,
            capture_output=True,
            text=True
        )
        if tracked_res.returncode == 0:
            is_tracked = True

        if not is_tracked and not is_staged:
            errors.append(
                f"❌ Untracked in git: '{git_rel_path}' is referenced in mkdocs.yml nav but has NOT been added to git.\n"
                f"   👉 Run: git add {git_rel_path}"
            )

    if errors:
        print("\n🚨 MkDocs Navigation Integrity Check Failed:")
        for err in errors:
            print(f"  {err}")
        print("\nFix the missing or untracked files before committing so GitHub Actions CI does not fail.\n")
        return 1

    # 3. If mkdocs is available locally, run a test build
    mkdocs_bin = subprocess.run(["which", "mkdocs"], capture_output=True, text=True).stdout.strip()
    if mkdocs_bin:
        with tempfile.TemporaryDirectory() as tmpdir:
            build_res = subprocess.run(
                [mkdocs_bin, "build", "--strict", "--site-dir", tmpdir],
                cwd=repo_root,
                capture_output=True,
                text=True
            )
            if build_res.returncode != 0:
                print("\n🚨 'mkdocs build --strict' failed locally:")
                print(build_res.stderr or build_res.stdout)
                return 1

    print(f"✅ MkDocs navigation check passed ({len(file_candidates)} referenced files verified and tracked in git).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
