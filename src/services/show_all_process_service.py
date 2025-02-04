import psutil
from ..models.process import Process

def show_all_processes():
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'status']):
        process = Process.from_psutil_proc(proc)
        print(process)