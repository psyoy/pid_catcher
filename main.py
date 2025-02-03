import psutil
from src.models.process import Process

if __name__ == "__main__":
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'status']):
        if proc.pid == 0:
            continue
        try:
            process = Process(proc.pid, proc.name(), proc.exe(), proc.status())
            print(process.get_edited_pid(), process.get_edited_name(), process.get_path(), process.get_edited_status())
        except psutil.AccessDenied:
            print(f"Access denied for PID {proc.pid} ({proc.name()})")
        except psutil.NoSuchProcess:
            pass


