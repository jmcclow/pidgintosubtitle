#!/usr/bin/python                                                                                                                                                                 
from datetime import datetime
import time
import re
def repl(string, begin):
    substring = re.findall('(\d{2}:\d{2}:\d{2})', string) 
    for i in substring:
        semicolon_split = i.split(':')
        dt_obj = datetime(2012, 11, 23, int(semicolon_split[0]), int(semicolon_split[1]), int(semicolon_split[2]))
        # Edit next line for epoch time offset from where you start to be 00:00:00
        epoch_to_adjust = begin 
        epoch_date = int(dt_obj.strftime("%s")) - epoch_to_adjust 
        begin = time.strftime("%H:%M:%S,000", time.localtime(epoch_date))
        end = time.strftime("%H:%M:%S,000", time.localtime(epoch_date + 10))
        stamp =  begin + " --> " + end + "\n"
        return stamp
#-------------------------------------------------
# conversions to strings
#-------------------------------------------------
# datetime object to string
inf = open('Subtitles.txt')
warning = inf.readline()
stamp = re.match('\((\d{2}:\d{2}:\d{2})\)', warning)
begin = stamp.group(0)
begin_split = re.findall('(\d{2}:\d{2}:\d{2})', begin)
for d in begin_split:
    semic_split = d.split(':')
    dt_obj = datetime(2012, 11, 23, int(semic_split[0]), int(semic_split[1]), int(semic_split[2]))
    zero_dt_obj = datetime(2012, 11, 22, 23, 59, 30)
    epoch_dt = int(dt_obj.strftime("%s")) - int(zero_dt_obj.strftime("%s")) 
subtitle_num = 1 
for line in inf:
    print subtitle_num
    print re.sub('\((\d{2}:\d{2}:\d{2})\)', repl(line, epoch_dt), line)
    subtitle_num += 1
