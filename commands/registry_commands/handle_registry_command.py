from .create_registry_command import CreateRegistryCommand
from .delete_registry_command import DeleteRegistryCommand
from .modify_registry_command import ModifyRegistryCommand
from .list_registry_command import ListRegistryCommand
from utils import continue_after_arguments
from exceptions import CustomError,ErrorType,handle_exception

def handle_registry_command(command_name, args):
    try:
        if command_name == "list_reg":
            command_instance = ListRegistryCommand(args[0])
            if (len(args) > 1):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(1,args,ce)
        elif command_name == "create_reg":
            command_instance = CreateRegistryCommand(args[0], args[1])
            if (len(args) > 2):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(2,args,ce)
        elif command_name == "modif_reg":
            command_instance = ModifyRegistryCommand(args[0], args[1], args[2])
            if (len(args) > 3):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(3,args,ce)
        elif command_name == "delete_reg":
            command_instance = DeleteRegistryCommand(args[0], args[1])
            if (len(args) > 2):
                ce : CustomError = CustomError(ErrorType.INVALID_COMMAND, command_instance.usage)
                continue_after_arguments(2,args,ce)
        else:
            raise CustomError (
                ErrorType.INVALID_COMMAND,
                f"Invalid command or missing arguments for command '{command_name}'"
            )
        
        return command_instance.execute()
    except CustomError as ce :
        handle_exception(ce)
    except Exception as e:
        handle_exception(CustomError(ErrorType.UNKNOWN_ERROR , str(e)))