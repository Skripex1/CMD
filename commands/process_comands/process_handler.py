from .kill_process_command import KillProcessCommand
from .list_process_command import ListProcessCommand
from utils import continue_after_arguments
from exceptions import CustomError,ErrorType,handle_exception
def handle_process_command(command_name,args):
    try:
        if command_name == "list_proc":
            command_instance = ListProcessCommand()
        elif command_name == "kill_proc":
            command_instance = KillProcessCommand(int(args[0]))
            if (len(args) > 1):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(1,args,ce)
        else:
            raise CustomError (
                ErrorType.INVALID_COMMAND,
                f"Invalid command or missing arguments for command '{command_name}'"
            )
        result = command_instance.execute()
        print(result)
    except CustomError as ce :
        handle_exception(ce)
    except Exception as e:
        handle_exception(CustomError(ErrorType.UNKNOWN_ERROR , str(e)))