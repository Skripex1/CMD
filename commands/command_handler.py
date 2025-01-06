from .file_folder_commands import handle_file_folder_command
from .process_comands import handle_process_command
from exceptions import CustomError , ErrorType , handle_exception
from utils import is_correct_path,display_help
import os
def handle_command(command_input):
    try:
        parts = command_input.strip().split()
        if not parts :
            raise CustomError(ErrorType.INVALID_COMMAND, "No command provided")
        
        command_name = parts[0].lower()
        args = parts[1:]
        print(f"Debug: command_name={command_name}, args={args}")
        print(args)

        if command_name == "help":
            display_help(args)
            return

        if command_name in ["copy","move","delete"]:
           handle_file_folder_command(command_name , args)  
        elif command_name in ["list_proc" , "kill_proc"]:
            handle_process_command(command_name,args)   
        else:
             raise CustomError(ErrorType.INVALID_COMMAND, f"Unknown command: {command_name}")

    except CustomError as ce :
        handle_exception(ce)
    except Exception as e:
        handle_exception(CustomError(ErrorType.UNKNOWN_ERROR, str(e)))
