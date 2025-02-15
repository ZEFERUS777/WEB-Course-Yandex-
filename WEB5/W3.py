import sys
import schedule
import datetime

start_h, end_h = map(int, input().split('-', maxsplit=1))


def Signal():
    hour = datetime.datetime.now().hour
    if start_h < hour < end_h:
        print('Ку' * hour)


schedule.every().hour.do(Signal)
