#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import signal


def interrupt_handler(signal, frame):
    """interrupt handler to exit gracefully on ctrl-c or kill command."""
    print_stats()
    sys.exit(0)


def print_stats():
    """prints accumulates metrics"""
    print("File size: ", file_size)
    for status in sorted(statcodecount.keys()):
        count = statcodecount[status]
        print(f"{status}: {count}")


signal.signal(signal.SIGINT, interrupt_handler)

try:
    line_count = 0
    file_size = 0
    statcodecount = {}

    for line in sys.stdin:
        line = line.strip()

        parts = line.split(" ")
        size = int(parts[-1])
        status = parts[-2]

        file_size += size
        statcodecount[status] = statcodecount.get(status, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()
            file_size = 0
            statcodecount.clear()
except KeyboardInterrupt:
    print_stats()
