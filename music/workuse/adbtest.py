"""
Created on Thu Oct 10 19:13:21 2018

@author: fishyoukun
"""
import  os
import time
# import adb
## to use adb throuth python for testing
# generate log file name
time_flag = time.strftime('%Y_%m_%d__%H_%M_%S',time.localtime(time.time()))
file_dir = r'D:\adblog'
filename = 'log'+time_flag+'.txt'
logfilename = file_dir + '\\' + str(filename)

# configure adb
command0 = ["adb root",
           "adb remount",
           # "adb shell",
           "adb logcat -G 100M"
           ]
command1 = "adb logcat -s AudioProcessing"


for i in range(len(command0)):
    os.system(command0[i])
    time.sleep(3)
logcat = os.popen(command1)
while True:
    data = logcat.readline()
    f = open(logfilename, 'a+')
    f.write(data)
    f.close()
    print data,








