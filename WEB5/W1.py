import sys
import schedule
import datetime


def Signal():
    print('Ку' * datetime.datetime.now().hour)


schedule.every().hour.do(Signal)
