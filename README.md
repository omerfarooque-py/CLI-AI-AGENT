# CLI AI Agent

A powerful CLI-based AI Agent that can perform various tasks such as file manipulation, running Python scripts, fixing errors, and providing information about files in the working directory. The agent is designed to be flexible and can be extended with additional functions as needed.

## Features

- **File Management**: List, read, and write files with security constraints
- **Code Execution**: Run Python scripts and capture output
- **Intelligent Processing**: Uses Google's Gemini AI to understand and execute complex requests
- **Multi-turn Conversations**: Maintains context across multiple interactions
- **Extensible Architecture**: Easy to add new functions for additional capabilities
- **Verbose Mode**: Optional detailed output for debugging

## Prerequisites

- Python 3.x
- Google Gemini API key
- Required Python packages (see Installation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/omerfarooque-py/CLI-AI-AGENT.git
cd CLI-AI-AGENT
```

2. Install dependencies:
```bash
pip install python-dotenv google-genai
```

3. Set up your environment variables:
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/)

## Usage

### Basic Command

```bash
python main.py "Your request here"
```

### Examples

**List files in a directory:**
```bash
python main.py "List all files in the calculator directory"
```

**Read file content:**
```bash
python main.py "Show me the content of calculator/main.py"
```

**Write to a file:**
```bash
python main.py "Create a file called output.txt with the text 'Hello, World!'"
```

**Run a Python script:**
```bash
python main.py "Run the calculator tests"
```

**Verbose mode (see token usage and detailed output):**
```bash
python main.py "Your request here" --verbose
```

## Available Functions

The AI agent has access to the following functions:

### 1. `get_files_info(working_directory, path="")`
Lists files and directories in a specified location.
- Returns file/directory information
- Supports relative paths
- Security: Cannot access paths outside working directory

### 2. `get_file_content(working_directory, file_path)`
Reads and returns the content of a file.
- Returns file contents as text
- Cannot read directories
- Security: Prevents access to system files outside working directory

### 3. `write_file(working_directory, file_path, content)`
Writes content to a file.
- Creates or overwrites files
- Supports nested directories
- Security: Cannot write to paths outside working directory (e.g., `/tmp/`)

### 4. `run_python_file(working_directory, file_path)`
Executes a Python script and returns output.
- Captures stdout and stderr
- Useful for running tests and utilities
- All paths are relative to working directory

## Project Structure

```
CLI-AI-AGENT/
├── main.py                      # Main entry point
├── functions/
│   ├── get_files_info.py       # File/directory listing functions
│   ├── get_file_content.py     # File reading functions
│   ├── run_python_file.py      # Python script execution
│   └── call_function.py        # Function dispatcher
├── calculator/                  # Example project directory
│   ├── main.py                 # Calculator main module
│   ├── tests.py                # Unit tests
│   └── pkg/
│       └── calculator.py       # Calculator implementation
├── test_*.py                   # Test scripts for individual functions
└── README.md                   # This file
```

## How It Works

1. **User Input**: You provide a natural language request via CLI
2. **AI Processing**: Gemini AI interprets your request and creates a function call plan
3. **Function Execution**: The agent executes necessary functions (file ops, script runs, etc.)
4. **Feedback Loop**: Results are sent back to the AI for context
5. **Response**: The agent provides a human-readable response

The agent uses a loop system (max 20 attempts) to handle complex multi-step requests that may require multiple function calls.

## Testing

Run the included test files to verify functionality:

```bash
# Test file listing
python test_get_files_info.py

# Test file reading
python test_get_file_content.py

# Test file writing
python test_write_file.py

# Test calculator functionality
python calculator/tests.py
```

## Security

The agent includes built-in security measures:

- **Path Validation**: Cannot access files outside the specified working directory
- **Absolute Path Blocking**: Prevents access to system paths (e.g., `/tmp/`, `/bin/`)
- **Sandboxed Execution**: All operations are relative to the working directory
- **No System Commands**: Can only execute Python files, not arbitrary shell commands

## Configuration

### System Prompt
Modify the `system_prompt` in `main.py` to change the agent's behavior and instructions.

### Model Selection
Currently uses `gemini-2.5-flash` for fast responses. Can be changed in the `generate_content()` call.

### Max Attempts
Default is 20 iterations. Adjust `max_attempts` variable if needed for complex operations.

## Troubleshooting

**"response or usage metadata has malfunctioned"**
- Check your internet connection
- Verify your Gemini API key is valid
- Ensure `.env` file is properly configured

**Permission Denied errors**
- Verify file/directory permissions
- Ensure paths are relative to working directory
- Check that files aren't write-protected

**Module not found errors**
- Install all required dependencies: `pip install -r requirements.txt`
- Verify Python file structure and imports

## Extending the Agent

To add new capabilities:

1. Create a new function file in the `functions/` directory
2. Define both the function and its schema (for Gemini)
3. Import and add the schema to `available_functions` in `main.py`
4. Update the system prompt with descriptions of new operations

## Example Extension

```python
# functions/my_function.py
from google.genai import types

def my_function(working_directory, param1):
    # Implementation here
    return result

schema_my_function = types.FunctionDeclaration(
    name="my_function",
    description="Description of what this function does",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "working_directory": types.Schema(type="STRING"),
            "param1": types.Schema(type="STRING")
        }
    )
)
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests to help improve the CLI AI Agent.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Created with ❤️ using Google Gemini AI**
