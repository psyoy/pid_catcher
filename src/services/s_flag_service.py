import psutil
from ..models.process_counter import ProcessCounter

def s_flag_service():
    process_counter = ProcessCounter()

    pids = psutil.pids()

    for pid in pids:
        proc = psutil.Process(pid)

        if proc.status() == psutil.STATUS_RUNNING:
            process_counter.increase_running()
        elif proc.status() == psutil.STATUS_WAITING:
            process_counter.increase_waiting()
        elif proc.status() == psutil.STATUS_DEAD:
            process_counter.increase_dead()
        elif proc.status() == psutil.STATUS_SLEEPING:
            process_counter.increase_sleeping()
        elif proc.status() == psutil.STATUS_ZOMBIE:
            process_counter.increase_zombie()

    print(process_counter)