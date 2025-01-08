# CMD Project Documentation

This project provides a command-line interface for performing various file, process, and registry operations.

## Available Commands

1. **File/Folder Operations**:
    - `copy` - Copies a file or folder from the source path to the destination path.
    - `move` - Moves a file or folder from the source path to the destination path.
    - `delete` - Deletes a file or folder at the specified path.

2. **Process Management**:
    - `list_proc` - Lists the currently running processes.
    - `kill_proc` - Kills the process with the specified PID.

3. **Registry Operations**:
    - `create_reg` - Creates a new registry key at the specified path with the provided value.
    - `modify_reg` - Modifies an existing registry key's value at the specified path.
    - `delete_reg` - Deletes a registry key or value at the specified path.
    - `list_reg` - Lists all the values under the specified registry key.

4. **Other**:
    - `help` - Displays this help message.

## Usage

The general syntax for each command is:

### Example Commands:

- `copy <source> <destination>`: Copies a file or folder.
- `move <source> <destination>`: Moves a file or folder.
- `delete <path>`: Deletes the specified file or folder.
- `list_proc`: Lists all running processes.
- `kill_proc <pid>`: Kills a process by its PID.
- `create_reg <key_path> <subkey_name>`: Creates a registry key.
- `modify_reg <key_path> <value_name> <new_value>`: Modifies a registry key.
- `delete_reg <key_path> <value_name>`: Deletes a registry key or value.
- `list_reg <key_path>`: Lists registry values under a key.

### Help Command:

To get more details about a specific command, type: 

`help <command>`

For example :

 `help <copy>`

This will show the usage and description for the `copy` command.

---

### Error Handling

If any command fails, the program will print an error message. Common errors include:

- **Invalid Path**: Occurs when the specified file or folder path doesn't exist.
- **Incorrect Number of Arguments**: Triggered if a command receives the wrong number of arguments.
- **Unknown Command**: Raised when an invalid or unrecognized command is used.
- **Invalid Registry Key Path**: Happens when the registry path is incorrect or doesn't exist.
- **Invalid PID**: Raised if an invalid Process ID (PID) is provided to the `kill_proc` command.

---
### Debugging Mode

To aid with troubleshooting, debugging mode can be activated in your `main.py`. When debugging is enabled, the program will print more detailed error messages, such as stack traces and variable values, to help identify the root cause of issues.

To enable debugging, pass the `--debug` flag when running the program:

## Requirements

- Python 3.x
- Necessary permissions for modifying files, processes, and registry keys.