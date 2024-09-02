import os
import sys
from dotenv import load_dotenv
import fnmatch

# Load environment variables
load_dotenv()

# Configuration variables
PROJECT_DIRECTORY = os.environ.get('PROJECT_DIRECTORY')
if not PROJECT_DIRECTORY:
    sys.exit("PROJECT_DIRECTORY environment variable is not set.")
if not os.path.isdir(PROJECT_DIRECTORY):
    sys.exit(f"{PROJECT_DIRECTORY} is not a directory or does not exist.")

SAVE_DIRECTORY = os.environ.get('SAVE_DIRECTORY', '.')
SKIP_EMPTY_FILES = os.environ.get('SKIP_EMPTY_FILES', 'FALSE').upper() == 'TRUE'

# Ensure SAVE_DIRECTORY exists
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

IGNORE_FILES = os.environ.get('IGNORE_FILES', '').split(',')
IGNORE_DIRS = os.environ.get('IGNORE_DIRS', '').split(',')

def should_ignore(file_path: str) -> bool:
    """Check if the file or directory should be ignored based on patterns."""
    for ignore_dir in IGNORE_DIRS:
        if ignore_dir in file_path:  # This checks directory names within the path
            return True

    for pattern in IGNORE_FILES:
        if fnmatch.fnmatch(os.path.basename(file_path), pattern):  # This checks the file name against patterns
            return True

    return False

def get_file_paths(start_path: str) -> list:
    """Recursively collect file paths, excluding ignored files and directories."""
    file_paths = []
    for root, dirs, files in os.walk(start_path, topdown=True):
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]  # Filter ignored dirs
        files[:] = [f for f in files if not should_ignore(os.path.join(root, f))]  # Correctly filter files
        for file in files:
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    return file_paths

def write_to_txt(output_path: str, file_paths: list) -> None:
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for path in file_paths:
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content:  # Check if the file has content
                        output_file.write(f"PATH: {path}\nCONTENT:\n{content}\n\n")
            except Exception as e:
                print(f"Error processing {path}: {e}")

if __name__ == '__main__':
    file_paths = get_file_paths(PROJECT_DIRECTORY)
    if not file_paths:
        print(f"No files found in the git directory: {PROJECT_DIRECTORY}")
        sys.exit(1)

    output_file_path = os.path.join(SAVE_DIRECTORY, f"{os.path.basename(PROJECT_DIRECTORY)}_files.txt")
    write_to_txt(output_file_path, file_paths)
    print(f"All files have been written to {output_file_path}")
