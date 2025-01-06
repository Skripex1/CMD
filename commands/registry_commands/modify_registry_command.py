from .base_registry_command import RegistryCommand
import winreg
from ..command_types import CommandType
from exceptions import CustomError,ErrorType

class ModifyRegistryCommand(RegistryCommand):
    def __init__(self, key_path, value_name, value_data):
        super().__init__(CommandType.MODIF_REG,"modif_reg <key_path> <value_name> <value_data>")
        self.key_path = key_path
        self.value_name = value_name
        self.value_data = value_data

    def execute(self):
        if not self.key_path or not self.value_name or not self.value_data:
           raise CustomError(ErrorType.INVALID_COMMAND, f"Missing arguments. Usage : {self.usage}")
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.key_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, self.value_name, 0, winreg.REG_SZ, self.value_data)
            return f"Value '{self.value_name}' set to '{self.value_data}' under '{self.key_path}'."
        except Exception as e:
            raise Exception(f"Failed to modify registry key: {e}")