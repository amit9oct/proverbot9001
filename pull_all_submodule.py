#!/usr/bin/env python3

# This file will be used to pull all submodules in the repository
# Path: data/proverbot9001/pull_all_submodule.py
import subprocess

def main():
    # Get all submodules in the repository
    submodules = subprocess.check_output(["git", "submodule", "status"]).decode("utf-8")
    submodules = [line.split(" ")[2].strip() for line in submodules.splitlines()]
    print(submodules)
    # Pull all submodules one by one
    for submodule in submodules:
        print(f"Pulling {submodule}...")
        output = subprocess.check_output(["git", "submodule", "update", "--init"], cwd=submodule).decode("utf-8")
        print(output)
        print("Done")
        print()

if __name__ == "__main__":
    main()