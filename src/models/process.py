import psutil
from colorama import init, Fore, Back, Style

class Process:
    def __init__(self, pid, name, path, status):
        self._pid = pid
        self._name = name
        self._path = path
        self._status = status
        self._status_running = 0
        self.status_stopped = 0
        self._status_waiting = 0
        self._status_dead = 0
        self._status_sleeping = 0
        self._status_zombie = 0
        init()

    def get_edited_pid(self):
        return Fore.BLACK + Back.WHITE + f'{self._pid}:' + Style.RESET_ALL

    def get_edited_name(self):
        return Fore.BLUE + self._name + Style.RESET_ALL

    def get_path(self):
        return self._path

    def get_edited_status(self):
        if self._status == psutil.STATUS_RUNNING:
            self._status_running += 1
            return Fore.GREEN + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_WAITING:
            self._status_waiting += 1
            return Fore.YELLOW + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_STOPPED:
            self.status_stopped += 1
            return Fore.RED + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_DEAD:
            self._status_dead += 1
            return Fore.RED + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_SLEEPING:
            self._status_sleeping += 1
            return Fore.YELLOW + self._status + Style.RESET_ALL
        elif self._status == psutil.STATUS_ZOMBIE:
            self._status_zombie += 1
            return Fore.CYAN + self._status + Style.RESET_ALL

    def get_status_counter(self):
        running =  Fore.GREEN + "Running: " + Style.RESET_ALL
        running + str(self._status_running)
