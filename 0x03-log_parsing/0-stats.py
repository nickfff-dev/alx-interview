#!/usr/bin/python3
""" Log parsing """
import sys
import re
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                      404: 0, 405: 0, 500: 0}


# Function to handle keyboard interruption
def signal_handler(sig, frame):
    """ Signal handler """
    print_statistics()
    sys.exit(0)


# Function to print statistics
def print_statistics():
    """ Print statistics """
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code,
                                  status_code_counts[status_code]))


# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
for line in sys.stdin:
    # Regular expression to match the input format
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'  # nopep8
    match = re.match(pattern, line)

    if match:
        # Extract file size and status code
        file_size = int(match.group(3))
        status_code = int(match.group(2))

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    # Print statistics every 10 lines
    if (total_file_size // 10) * 10 < total_file_size:
        print_statistics()
        total_file_size = 0
        for status_code in status_code_counts.keys():
            status_code_counts[status_code] = 0

# Print final statistics if any
if total_file_size > 0:
    print_statistics()
