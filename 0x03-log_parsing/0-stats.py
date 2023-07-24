#!/usr/bin/python3
"""
Module 0-status.py
"""
from sys import stdin


def status_printer(total_size, status):
    """A method to print the status with the format given"""
    print('File size: {}'.format(total_size))
    for code, count in sorted(status.items()):
        if count > 0:
            print('{}: {:d}'.format(code, count))


def main():
    """Main method"""
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total = 0
    count = 0
    try:
        for line in stdin:
            splited = line.split()
            if count % 10 == 0 and count != 0:
                status_printer(total_size=total, status=status_codes)
            try:
                code = splited[-2]
                if code in status_codes.keys():
                    status_codes[code] = status_codes[code] + 1
            except Exception:
                pass
            try:
                total += int(splited[-1])
            except Exception:
                pass
            count += 1
        status_printer(total_size=total, status=status_codes)
    except KeyboardInterrupt:
        status_printer(total, status_codes)
        raise


if __name__ == '__main__':
    main()
