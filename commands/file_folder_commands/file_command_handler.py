from .copy_file_folder_command import CopyFileFolderCommand
from exceptions import CustomError , ErrorType , handle_exception
from utils import continue_after_arguments

def handle_file_folder_command(command_name , args) :
    try :
        if command_name == "copy" :
            if (args < 2): 
                raise CustomError(
                    ErrorType.INVALID_COMMAND,
                    f"Missing arguments for command '{command_name}'"
                )
            command_instance = CopyFileFolderCommand(args[0],args[1])
            ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
            continue_after_arguments(2,args,ce)
        else :
            raise CustomError (
                ErrorType.INVALID_COMMAND,
                f"Invalid command or missing arguments for command '{command_name}'"
            )
        return command_instance.execute()
    except CustomError as ce :
        handle_exception(ce)
    except Exception as e:
        handle_exception(CustomError(ErrorType.UNKNOWN_ERROR , str(e)))