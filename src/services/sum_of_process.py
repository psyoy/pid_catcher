import psutil
from ..models.process_counter import ProcessCounter

def sum_of_process():
    process_counter = ProcessCounter()

    pids = psutil.pids()

    for pid in pids:
        proc = psutil.Process(pid)

        if proc.status() == psutil.STATUS_RUNNING:
            process_counter.increment_running()
        elif proc.status() == psutil.STATUS_WAITING:
            process_counter.increment_waiting()
        elif proc.status() == psutil.STATUS_DEAD:
            process_counter.increment_dead()
        elif proc.status() == psutil.STATUS_SLEEPING:
            process_counter.increment_sleeping()
        elif proc.status() == psutil.STATUS_ZOMBIE:
            process_counter.increment_zombie()

    print(process_counter)