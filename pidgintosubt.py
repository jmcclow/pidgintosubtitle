#!/usr/bin/python                                                                                                                                                                 
from datetime import datetime
import time
import re
def repl(string):
    substring = re.findall('(\d{2}:\d{2}:\d{2})', string) 
    for i in substring:
        blah = i.split(':')
        dt_obj = datetime(2012, 11, 23, int(blah[0]), int(blah[1]), int(blah[2]))
        # Edit next line for epoch time offset from where you start to be 00:00:00
        epoch_to_adjust = 24867
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
subtitle_num = 1 
for line in inf:
    print subtitle_num
    print re.sub('\((\d{2}:\d{2}:\d{2})\)', repl(line), line)
    subtitle_num += 1
