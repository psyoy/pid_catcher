import argparse
from ..services.show_all_process_service import show_all_processes
from ..services.sum_of_process import sum_of_process

def router():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", help="show all process")
    parser.add_argument("-s", "--sum", action="store_true", help="sum of all processes")

    args = parser.parse_args()

    if args.all:
        show_all_processes()

    if args.sum:
        sum_of_process()