#!/usr/bin/python3
""" Log parsing """
import sys
import re


# Function to print statistics
def print_statistics(log_data: dict) -> None:
    """ Print statistics """
    print("File size: {}".format(log_data['total_file_size']))
    for status_code in sorted(log_data['status_code_dict']):
        if log_data['status_code_dict'][status_code]:
            code = log_data['status_code_dict'][status_code]
            print("{}: {}".format(status_code, code))


def extract_line(line: str) -> tuple:
    """ Extracts file size and status code """
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'  # nopep8
    match = re.match(pattern, line)
    if match:
        file_size = int(match.group(2))
        status_code = int(match.group(1))
        return (file_size, status_code)
    return (0, 0)


def update_stats(log_data: dict, file_size: int, status_code: int) -> None:
    """ Update statistics """
    log_data['total_file_size'] += file_size
    if status_code and isinstance(status_code, int) and \
            (str(status_code) in log_data['status_code_dict']):
        log_data['status_code_dict'][str(status_code)] += 1


def run_log_stats():
    """ Run log statistics """
    num_lines = 0
    log_data = {'total_file_size': 0, 'status_code_dict':
                {str(x): 0 for x in [
                    200, 301, 400, 401, 403, 404, 405, 500
                ]}
                }
    try:
        for line in sys.stdin:
            num_lines += 1
            file_size, status_code = extract_line(line)
            update_stats(log_data, file_size, status_code)
            if num_lines % 10 == 0:
                print_statistics(log_data)
            print_statistics(log_data)
    except KeyboardInterrupt:
        print_statistics(log_data)
        raise


if __name__ == "__main__":
    run_log_stats()
