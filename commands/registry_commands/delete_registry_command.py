from .base_registry_command import RegistryCommand
import winreg
from ..command_types import CommandType
from exceptions import CustomError,ErrorType


class DeleteRegistryCommand(RegistryCommand):
    def __init__(self, key_path, subkey_name):
        super().__init__(CommandType.DELETE_REG,"delete_reg <key_path> <subkey_name>")
        self.key_path = key_path
        self.subkey_name = subkey_name

    def execute(self):
        if not self.key_path or not self.subkey_name:
            raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.key_path, 0, winreg.KEY_WRITE) as key:
                winreg.DeleteKey(key, self.subkey_name)
            return f"Subkey '{self.subkey_name}' deleted under '{self.key_path}'."
        except FileNotFoundError:
            raise Exception(f"Registry subkey not found: {self.subkey_name}")
        except Exception as e:
            raise Exception(f"Failed to delete registry key: {e}")