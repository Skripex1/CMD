from abc import ABC , abstractmethod
from commands.command_types import CommandType

class ProcessCommand (ABC):
    def __init__ (self,command_type: CommandType,usage: str):
        self.usage = usage
        self.commad_type = command_type
    
    @abstractmethod
    def execute(self):
        pass