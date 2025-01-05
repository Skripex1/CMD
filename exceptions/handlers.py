from .custom_exception import ErrorType, CustomError

def handle_exception (exception: CustomError) :
    if exception.error_type == ErrorType.FILE_NOT_FOUND or exception.error_type == ErrorType.DIRECTORY_NOT_FOUND :
        print(f"Error: File or Folder was not found ! {exception.message}")
    elif exception.error_type == ErrorType.INVALID_COMMAND :
        print(f"Error: Invalid command ! {exception.message}")
    elif exception.error_type == ErrorType.NOT_EXISTING_PATH:
        print(f"Error: Path is not correct ! {exception.message}")
    else:
        print(f"Error: {exception.message}")
