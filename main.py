import psutil
from src.models.process import Process

if __name__ == "__main__":
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'status']):
        process = Process.from_psutil_proc(proc)
        print(process)
