from .file_folder_commands import handle_file_folder_command
from .process_comands import handle_process_command
from .registry_commands import handle_registry_command
from exceptions import CustomError , ErrorType , handle_exception
from utils import is_correct_path,display_help
import os
DEBUG = False

def handle_command(command_input):
    global DEBUG
    try:

        if "--debug" in command_input:
            DEBUG = True
            command_input = command_input.replace("--debug", "").strip()

        parts = command_input.strip().split()
        if not parts :
            raise CustomError(ErrorType.INVALID_COMMAND, "No command provided")
        
        command_name = parts[0].lower()
        args = parts[1:]
        
        if DEBUG:
            print(f"[DEBUG] Command name: {command_name}, Arguments: {args}")

        if command_name == "help":
            display_help(args)
            return

        if command_name in ["copy","move","delete"]:
           handle_file_folder_command(command_name , args)  
        elif command_name in ["list_proc" , "kill_proc"]:
            handle_process_command(command_name,args)   
        elif command_name in ["list_reg","create_reg","modify_reg","delete_reg"]:
            handle_registry_command(command_name, args)
        else:
             raise CustomError(ErrorType.INVALID_COMMAND, f"Unknown command: {command_name}")

    except CustomError as ce :
        handle_exception(ce)
    except Exception as e:
        handle_exception(CustomError(ErrorType.UNKNOWN_ERROR, str(e)))
