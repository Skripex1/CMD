from .base_process_command import ProcessCommand
import psutil
from ..command_types import CommandType


class ListProcessCommand(ProcessCommand):
    def __init__(self):
        super().__init__(CommandType.LIST_PROC,"list_proc")
    
    def execute(self):
        try:
            processes = []
            for proc in psutil.process_iter(['pid','name']):
                 processes.append(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
            return "\n".join(processes) if processes else "No running processes found."
        except Exception as e :
            raise Exception(f"Failed to list processes: {e}")
