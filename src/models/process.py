import psutil
from colorama import init, Fore, Back, Style

class Process:
    def __init__(self, pid, name, path, status):
        self._pid = pid
        self._name = name
        self._path = path
        self._status = status
        init()

    def __str__(self):
        return f'{self.get_edited_pid()} {self.get_edited_name()} {self.get_path()} {self.get_edited_status()}'

    @classmethod
    def from_psutil_proc(cls, proc):
        if proc.pid in (0, 1):
            return None
        try:
            return cls(proc.pid, proc.name(), proc.exe(), proc.status())
        except psutil.AccessDenied:
            print(f'Access denied for PID {proc.pid} ({proc.name()})')
            return None
        except psutil.NoSuchProcess:
            print(f"Can't find PID {proc.pid}")
            return None

    def get_edited_pid(self):
        return Fore.BLACK + Back.WHITE + f'{self._pid}:' + Style.RESET_ALL

    def get_edited_name(self):
        return Fore.BLUE + self._name + Style.RESET_ALL

    def get_path(self):
        return self._path

    def get_edited_status(self):
        if self._status == psutil.STATUS_RUNNING:
            return Fore.GREEN + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_WAITING:
            return Fore.YELLOW + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_STOPPED:
            return Fore.RED + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_DEAD:
            return Fore.RED + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_SLEEPING:
            return Fore.YELLOW + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_ZOMBIE:
            return Fore.CYAN + self._status + Style.RESET_ALL