from __future__ import annotations

import argparse
import os
import subprocess
from collections.abc import Sequence

# Set the maximum file size (in bytes)
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB, adjust this value as needed

def main(argv: Sequence[str] | None = None) -> int:
    """Main function to check for large files in the specified files."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        if os.path.isfile(filename):  # Check if the file exists
            file_size = os.path.getsize(filename)  # Get the size of the file
            if file_size > MAX_FILE_SIZE:
                print(f"{filename}: File size {file_size / (1024 * 1024):.2f} MB exceeds the limit of {MAX_FILE_SIZE / (1024 * 1024):.2f} MB.")
                retcode = 1  # Set return code to indicate large file found

    return retcode

if __name__ == "__main__":
    raise SystemExit(main())
