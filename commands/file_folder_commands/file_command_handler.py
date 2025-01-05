from .copy_file_folder_command import CopyFileFolderCommand
from .move_file_folder_command import MoveFileFolderCommand
from .delete_file_folder_command import DeleteFileFolderCommand
from exceptions import CustomError , ErrorType , handle_exception
from utils import continue_after_arguments

def handle_file_folder_command(command_name , args) :
    try :
        if command_name == "copy" or command_name == "move":
            if (command_name == "copy"):
                command_instance = CopyFileFolderCommand(args[0],args[1])
            else:
                command_instance = MoveFileFolderCommand(args[0],args[1])
            if (len(args) > 2):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(2,args,ce)
        elif command_name == "delete":
             command_instance = DeleteFileFolderCommand(args[0])
             if (len(args) > 1):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(1,args,ce)
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