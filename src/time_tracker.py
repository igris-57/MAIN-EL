"""
    @author Zhida Li
    @email zhidal@sfu.ca
    @date Apr. 28, 2020
    @version: 1.1.0
    @description:
                Track the timestamp used for the filename from RIPE or Route Views.

    @copyright Copyright (c) Apr. 28, 2020
        All Rights Reserved

    This Python code (versions 3.6 and newer)
"""

# ==============================================
# time_tracker_single(), time_tracker_multi()
# ==============================================
# Last modified: Feb. 19, 2022

#
import time
import datetime


# time.gmtime()
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=27, tm_hour=8, tm_min=10,
# tm_sec=10, tm_wday=0, tm_yday=118, tm_isdst=0)

# Enter RIPE or RouteViews
def time_tracker_single(site):
    now = datetime.datetime.utcnow()
    
    if site == 'RIPE':
        # RIPE updates every 5 mins, but it often takes 5-10 mins for the file to be available.
        # Requesting data from 10 minutes ago avoids 404 Not Found errors.
        target_time = now - datetime.timedelta(minutes=10)
        minute = target_time.minute
        minute = minute - (minute % 5)
    elif site == 'RouteViews':
        # RouteViews updates every 15 mins, with similar delays.
        # Requesting data from 30 minutes ago is safer.
        target_time = now - datetime.timedelta(minutes=30)
        minute = target_time.minute
        minute = minute - (minute % 15)
    else:
        print('Site name is incorrect.')
        exit()

    year = str(target_time.year)
    month = f"{target_time.month:02d}"
    day = f"{target_time.day:02d}"
    hour = f"{target_time.hour:02d}"
    minute = f"{minute:02d}"
    
    return year, month, day, hour, minute


# Return the all the dates in a list.
# format YYYYMMDD
def time_tracker_multi(start_date, end_date):
    # start_date='20030121'
    # end_date='20030125'

    # time.strptime(time_string[, format])
    datestart = datetime.datetime.strptime(start_date, '%Y%m%d')
    dateend = datetime.datetime.strptime(end_date, '%Y%m%d')

    date_list = list()
    while datestart <= dateend:
        date_list.append(datestart.strftime('%Y%m%d'))
        datestart += datetime.timedelta(days=1)

    return date_list
