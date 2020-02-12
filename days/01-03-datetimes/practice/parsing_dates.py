
from datetime import datetime

SHUTDOWN_EVENT = "Shutdown initiated."


def convert_to_datetime(line):
    line = line.rsplit(' ')[1]
    return datetime.strptime(line, "%Y-%m-%dT%H:%M:%S")


def in_line(line, pattern):
    if pattern in line:
        return True
    return False


def time_between_shutdowns(loglines):
    lines = []
    for i in loglines:
        if in_line(i, SHUTDOWN_EVENT):
            lines.append(convert_to_datetime(i))
    return lines[1] - lines[0]


line = "INFO 2014-07-03T23:27:51 supybot Shutdown initiated."
line2 = "ERROR 2014-07-03T23:24:31 supybot Invalid user."
print(convert_to_datetime(line))
print(in_line(line, "Shutdown initiated."))
print(in_line(line2, "Shutdown initiated."))
