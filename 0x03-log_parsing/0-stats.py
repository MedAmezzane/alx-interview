#!/usr/bin/python3
"""
Log parsing script that reads from standard input, processes log data,
and prints statistics about the status codes and file size.
"""
import sys

# Initialize line count and total size of logs
line_count = 0
total_file_size = 0

# Dictionary to store the count of various status codes
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_status():
    """
    Helper function to print the current statistics of the log.
    Outputs the total file size and the count of status codes.
    """
    print(f"File size: {total_file_size}")

    # Print only status codes that have non-zero counts
    for status_code, count in status_code_counts.items():
        if count > 0:
            print(f"{status_code}: {count}")


try:
    for log_line in sys.stdin:
        # Print the status after every 10 lines
        if line_count == 10:
            print_status()
            line_count = 0

        # Strip the trailing whitespace and split the log line into parts
        log_line = log_line.rstrip()
        log_parts = log_line.split()

        if len(log_parts) > 4:
            status_code = log_parts[-2]
            try:
                file_size = int(log_parts[-1])
                total_file_size += file_size
            except ValueError:
                continue

            # Update the count for the encountered status code
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Increment the log line count
            line_count += 1

except KeyboardInterrupt:
    # Handle the case of a keyboard interruption (Ctrl+C)
    print_status()
    raise
finally:
    # Always print the final status when done
    print_status()
