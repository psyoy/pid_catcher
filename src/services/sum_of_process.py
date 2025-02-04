import psutil
from ..models.process_counter import ProcessCounter

def sum_of_process():
    process_counter = ProcessCounter()

    pids = psutil.pids()

    for pid in pids:
        proc = psutil.Process(pid)
        status = proc.status()

        if status == psutil.STATUS_RUNNING:
            process_counter.increment_running()
        elif status == psutil.STATUS_STOPPED:
            process_counter.increment_stopped()
        elif status== psutil.STATUS_WAITING:
            process_counter.increment_waiting()
        elif status == psutil.STATUS_DEAD:
            process_counter.increment_dead()
        elif status == psutil.STATUS_SLEEPING:
            process_counter.increment_sleeping()
        elif status == psutil.STATUS_ZOMBIE:
            process_counter.increment_zombie()

    print(process_counter)