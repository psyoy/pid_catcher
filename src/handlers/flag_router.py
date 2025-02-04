import argparse
from ..services.a_flag_service import a_flag_service
from ..services.s_flag_service import s_flag_service

def router():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", help="show all process")
    parser.add_argument("-s", "--sum", action="store_true", help="sum of all processes")

    args = parser.parse_args()

    if args.all:
        a_flag_service()

    if args.sum:
        s_flag_service()