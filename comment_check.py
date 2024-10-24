import os
import sys


def check_comments_in_script(file_path):
    """Check if the given script contains comments or docstrings."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # Specify encoding
            for line in file:
                line = line.strip()
                if line.startswith("#"):
                    return True
                if ('"""' in line or "'''" in line) and "=" not in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return False


def main():
    """Main function to iterate through provided files and validate them."""
    status_passed = True
    for file in sys.argv[1:]:
        if not os.path.isfile(file):
            print(f"{file} is not a valid file.")
            status_passed = False
            continue

        if not check_comments_in_script(file):
            print(f"No comments or docstrings found in {file}.")
            status_passed = False
        else:
            print(f"Comments or docstrings validated in {file}.")

    sys.exit(0 if status_passed else 1)


if __name__ == "__main__":
    main()
