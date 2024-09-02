# filestotext

`filestotext` is a Python script that combines the content of all files present in a specified folder into a single .txt document. This tool is useful for creating a consolidated view of your project's files, making it to feed your codebase into an AI.

## Features

- Recursively scans a specified directory for files
- Combines the content of all files into a single .txt document
- Allows skipping empty files
- Supports ignoring specific files and directories
- Configurable through environment variables

## Requirements

- Python 3.6+
- `python-dotenv` library

## Installation

1. Clone this repository or download the script.
2. Install the required library:

```bash
pip install python-dotenv
```

## Configuration

Create a `.env` file in the same directory as the script with the following variables:

```
PROJECT_DIRECTORY=/your/local/folder
SAVE_DIRECTORY=/directory/where/txtfile/is/saved
SKIP_EMPTY_FILES=TRUE
IGNORE_FILES=*.log,*.tmp,*.cache,.DS_Store,*.py,.env,package-lock.json
IGNORE_DIRS=node_modules,build,dist,migrations,venv,.git
```

### Environment Variables

- `PROJECT_DIRECTORY`: The directory containing the files you want to combine (required)
- `SAVE_DIRECTORY`: The directory where the output .txt file will be saved (default: current directory)
- `SKIP_EMPTY_FILES`: Set to "TRUE" to skip empty files (default: FALSE)
- `IGNORE_FILES`: Comma-separated list of file patterns to ignore
- `IGNORE_DIRS`: Comma-separated list of directory names to ignore

## Usage

Run the script using Python:

```bash
python filestotext.py
```

The script will create a .txt file in the specified `SAVE_DIRECTORY` with the name format: `{project_directory_name}_files.txt`.

## Output

The output .txt file will contain the content of all processed files, with each file's content preceded by its path:

```
PATH: /path/to/file1.txt
CONTENT:
[Content of file1.txt]

PATH: /path/to/file2.py
CONTENT:
[Content of file2.py]

...
```

## Error Handling

- If `PROJECT_DIRECTORY` is not set or doesn't exist, the script will exit with an error message.
- If no files are found in the specified directory, the script will exit with an error message.
- Any errors encountered while processing individual files will be printed to the console, but the script will continue processing other files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]
