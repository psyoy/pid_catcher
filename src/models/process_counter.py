from colorama import init, Fore, Style

class ProcessCounter:
    def __init__(self):
        self._running = 0
        self._waiting = 0
        self._stopped = 0
        self._dead = 0
        self._sleeping = 0
        self._zombie = 0
        init()

    def increment_running(self):
        self._running += 1

    def increment_waiting(self):
        self._waiting += 1

    def increment_stopped(self):
        self._stopped += 1

    def increment_dead(self):
        self._dead += 1

    def increment_sleeping(self):
        self._sleeping += 1

    def increment_zombie(self):
        self._zombie += 1

    def __str__(self):
        result = ''
        running = Fore.GREEN + 'Running' + Style.RESET_ALL
        waiting = Fore.YELLOW + 'Waiting' + Style.RESET_ALL
        stopped = Fore.RED + 'Stopped' + Style.RESET_ALL
        dead = Fore.RED + 'Dead' + Style.RESET_ALL
        sleeping = Fore.BLUE + 'Sleeping' + Style.RESET_ALL
        zombie = Fore.CYAN + 'Zombie' + Style.RESET_ALL
        result += f'{running}: {self._running}\n{waiting}: {self._waiting}\n{stopped}: {self._stopped}\n'
        result += f'{dead}: {self._dead}\n{sleeping}: {self._sleeping}\n{zombie}: {self._zombie}'
        return result