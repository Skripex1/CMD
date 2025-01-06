from .base_registry_command import RegistryCommand
import winreg
from ..command_types import CommandType
from exceptions import CustomError,ErrorType

class ListRegistryCommand(RegistryCommand):
    def __init__(self,key_path):
        super().__init__(CommandType.LIST_REG, "list_reg <key_path>")
        self.key_path = key_path
    def execute(self):
        if not self.key_path:
            raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.key_path) as key:
                i = 0
                subkeys = []
                while True:
                    try:
                        subkey = winreg.EnumKey(key, i)
                        subkeys.append(subkey)
                        i += 1
                    except OSError:
                        break
                return f"Subkeys: {', '.join(subkeys) if subkeys else 'No subkeys found.'}"
        except FileNotFoundError:
            raise Exception(f"Registry key not found: {self.key_path}")