# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:13:21 2018

@author: fishyoukun
"""

## to generate vbs script used for audio test
testcmdarray = [
{'CmdNotes': 'sink 0 link to source 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '0,0,0'}
]

i = 0
### write file head
file_object = open('disconnectall.vbs','w')
file_object.write('# $language = "VBScript"\n')
file_object.write('# $interface = "1.0"\n')
file_object.write('Sub Main  \n')

source_num = 15
sink_num = 4
for j in range(source_num):
    for k in range(sink_num):
        CmdData = str(j) + ',0,'+ str(k)
        testcmdarray = [
            {'CmdNotes': 'disconnect all source to all sink', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0202,
             'InstanseId': 0, 'CmdData': CmdData}
        ]
        for i in range(len(testcmdarray)):
            CmdNotes = testcmdarray[i]['CmdNotes']
            Cmdname = testcmdarray[i]['Cmdname']
            CmdId = testcmdarray[i]['CmdId']
            InstanseId = testcmdarray[i]['InstanseId']
            CmdData = testcmdarray[i]['CmdData']
            cmddata1= CmdData.split(',')
            CmdLen = len(cmddata1)
            command = '\tcrt.Screen.Send "'+Cmdname + '-C ' +str(hex(CmdId))+ ' -I '+str(InstanseId)+ ' -L '+str(CmdLen) +' -D '+ CmdData +'" & vbCR\n'
            # command = Cmdname + '-C ' +str(hex(CmdId))+ ' -I '+str(InstanseId)+ ' -L '+str(CmdLen) +' -D '+ CmdData +" & vbCR\n"
            print(' \''),
            print (CmdNotes)
            print (command)
            file_object.write(' \'')
            file_object.write(CmdNotes)
            file_object.write('\n')
            file_object.write(command)

### write file end
file_object.write('End Sub   \n')
file_object.close()

