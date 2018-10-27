# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:13:21 2018

@author: fish
"""

## to generate vbs script used in SecureCrt for dummp blackbox

import time
file_object = open('script.vbs','w')
file_object.write('# $language = "VBScript"\n')
file_object.write('# $interface = "1.0"\n')
file_object.write('Sub Main  \n')
addr_org_gptMntBlackBox = 0x81225d0
sample_time = 65536/256
for i in range(0,sample_time):
    addr = addr_org_gptMntBlackBox + i*256
    command = '\tcrt.Screen.Send "./md '+ hex(addr) + ' " & vbCR\n'
    print (command)
    file_object.write(command)

    command = '\tcrt.Sleep 1500\n'
    print (command)
    file_object.write(command)
addr_org_gtBspExcInfo = 0xB080E64
sample_time = 256/256
for i in range(0,sample_time):
    addr = addr_org_gtBspExcInfo + i*256
    command = '\tcrt.Screen.Send "./md '+ hex(addr) + ' " & vbCR\n'
    print (command)
    file_object.write(command)

    command = '\tcrt.Sleep 1500\n'
    print (command)
    file_object.write(command)
file_object.write('End Sub   \n')
file_object.close()

