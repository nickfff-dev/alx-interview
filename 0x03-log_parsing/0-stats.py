#!/usr/bin/python3
""" Log parsing """
import sys
import re


if __name__ == "__main__":
    # Function to print statistics
    def print_statistics(log_data: dict) -> None:
        """ Print statistics """
        print("File size: {}".format(log_data['total_file_size']))
        for status_code in sorted(log_data['status_code_dict']):
            if log_data['status_code_dict'][status_code]:
                code = log_data['status_code_dict'][status_code]
                print("{}: {}".format(status_code, code))
    num_lines = 0
    log_data = {'total_file_size': 0, 'status_code_dict':
                {str(x): 0 for x in [
                    200, 301, 400, 401, 403, 404, 405, 500
                ]}
                }

    # Process each line from stdin
    try:
        for line in sys.stdin:
            line = line.strip()
            # Regular expression to match the input format
            pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'  # nopep8
            match = re.match(pattern, line)

            if match:
                num_lines += 1
                # Extract file size and status code
                file_size = int(match.group(2))
                status_code = int(match.group(1))

                # Update metrics
                log_data['total_file_size'] += file_size
                if isinstance(status_code, int) and \
                        (str(status_code) in log_data['status_code_dict']):
                    log_data['status_code_dict'][str(status_code)] += 1
            # Print statistics every 10 lines
                if num_lines % 10 == 0:
                    print_statistics(log_data)
        print_statistics(log_data)
    except (KeyboardInterrupt, EOFError):
        print_statistics(log_data)
        raise
