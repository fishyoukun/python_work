# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:13:21 2018

@author: fishyoukun
"""


def gencmdbyzone(zoneid):
    i = 0
    for i in range(len(zoneid)):
        CmdNotes = zoneid[i]['CmdNotes']
        Cmdname = zoneid[i]['Cmdname']
        CmdId = zoneid[i]['CmdId']
        InstanseId = zoneid[i]['InstanseId']
        CmdData = zoneid[i]['CmdData']
        cmddata1 = CmdData.split(',')
        CmdLen = len(cmddata1)
        Cmd = Cmdname + '-C ' + str(hex(CmdId)) + ' -I ' + str(InstanseId) + ' -L ' + str(CmdLen) \
              + ' -D ' + CmdData
        command = '\tcrt.Screen.Send "' + Cmd + '" & vbCR\n'
        print(' \''),
        print (CmdNotes)
        print (command)
        file_object.write(' \'')
        file_object.write(CmdNotes)
        file_object.write('\n')
        file_object.write(command)
        # file_object.write('\n')
    return 0


def dumpfunction(time):
    time_duration = time
    dumpcmd = 'padump2file  -t ' + str(time_duration)
    command = '\tcrt.Screen.Send "' + dumpcmd + '" & vbCR\n'
    print (command)
    file_object.write(command)
    # file_object.write('\n')
    return 0


def predump():
    dumpcmd = 'rm -rf /mnt/pulseaudio/dump/ '
    command = '\tcrt.Screen.Send "' + dumpcmd + '" & vbCR\n'
    print (command)
    file_object.write(command)
    # file_object.write('\n')
    return 0


def audioplay(audio, source):
    file_dir = '/data/test_env'
    audioname = file_dir + '/' + str(audio)
    # playcmd = 'alsa_aplay -DMedia -r48000 -c2 -fS32_LE --period-size=64 /data/test_env/chirp_48K_20hz_20khz_2CH_40s_-15dB.wav &'
    # playcmd = 'alsa_aplay -DpcmTTS_p -r48000 -c2 -fS32_LE --period-size=64 /data/test_env/chirp_48K_20hz_20khz_2CH_40s_-15dB.wav &'
    playcmd = 'alsa_aplay -D' + source + ' -r48000 -c2 -fS32_LE --period-size=64 ' + audioname + ' &'
    command = '\tcrt.Screen.Send "' + playcmd + '" & vbCR\n'
    print (command)
    file_object.write(command)
    # file_object.write('\n')


def call_delay(time_ms):
    command = '\tcrt.Sleep ' + str(time_ms) + '\n'
    print (command)
    file_object.write(command)
    # file_object.write('\n')


####################################################################
if __name__ == '__main__':
    playflag = True
    dumpflag = False
    source = 0
    zone = 0
    sink = 0

    ## filename to saved
    file_dir = r'D:\test_scripts\audioworx'
    filename = r'audiocmd_dynamic mixer.vbs'
    filefull_name = file_dir + '\\' + filename
    file_object = open(filefull_name, 'w')

    ### write file head
    file_object.write('# $language = "VBScript"\n')
    file_object.write('# $interface = "1.0"\n')
    file_object.write('Sub Main  \n')
    ## to generate vbs script used for audio test
    zone0cmd = [
        {'CmdNotes': 'sink y link to source x', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0,
         'CmdData': str(source) + ',' + str(zone) + ',' + str(sink)},
        # {'CmdNotes': 'set autodect para', 'Cmdname': '/data/test_env/tinyCmd -N 15 -V -c 0 ', 'CmdId': 0x2262,
        #  'InstanseId': 0, 'CmdData': '0,0,0x13,0x88,0'},
        # {'CmdNotes': 'mute with autodect', 'Cmdname': '/data/test_env/tinyCmd -N 15 -V -c 0 ', 'CmdId': 0x2262,
        #  'InstanseId': 0, 'CmdData': '0,1,0x13,0x88,0'},

        # {'CmdNotes': 'sink 0 link to source 1', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '1,0,0'},
        # {'CmdNotes': 'disconnect sink 0 link to source 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0202, 'InstanseId': 0, 'CmdData': '0,0,0'},
        # {'CmdNotes': 'disconnect sink 0 link to source 1', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0202, 'InstanseId': 0, 'CmdData': '1,0,0'},
        # {'CmdNotes': 'mute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,1,0,100'},
        # {'CmdNotes': 'unmute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,0,0,100'},
        # {'CmdNotes': 'volume -30db ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'volume 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0, 'CmdData': '0,0,0,0,100'},
        # {'CmdNotes': 'gain offset 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0,0,0,200'},
        # {'CmdNotes': 'gain offset -30db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,200'},
        # {'CmdNotes': 'ramp exponent', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2242, 'InstanseId': 0, 'CmdData': '0,1,1,5'},
        # {'CmdNotes': 'ramp 100ms', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'fade 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0, 'CmdData': '0,0x0,0x10,0,0,0,0,0,0,0,0,0x0,0x0,0,0,0,0'}
        # {'CmdNotes': 'balance 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x08,0,0,0,0,0,0,0,0,0,0,0,0,0,0'}
        # {'CmdNotes': 'delay 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2222, 'InstanseId': 0,
        #  'CmdData': '0x03,0xE8,0x00,0x00,0x00,0x00,0x00,0x00'}
        # {'CmdNotes': 'limit ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2205, 'InstanseId': 0,
        #  'CmdData': '0x04,0,0,0xe1,0x0a,0x02,0x58,0xfb,0x14,0,0,0xe1,0x0a,0x02,0x58,0xfb,0x14,0,0,0xe1,0x0a,0x02,0x58,0xfb,0x14,0,0,0xe1,0x0a,0x02,0x58,0xfb,0x14'}
        # {'CmdNotes': 'white niose  ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x221B, 'InstanseId': 0,
        #  'CmdData': '1,1,0x0,0x0,0x0,0x01,0,0,0,100,0x01,0xf4,0,0,0xfe,0xc0'},
        # {'CmdNotes': 'pink niose  ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x221B, 'InstanseId': 0,
        #   'CmdData': '2,1,0x0,0x0,0x0,0x01,0,0,0,100,0x01,0xf4,0,0,0xfe,0xc0'},
        # {'CmdNotes': 'niose gen on ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x221B, 'InstanseId': 0, 'CmdData': '1'}
    ]
    zone1cmd = [
        {'CmdNotes': 'dynamic mixer to rear', 'Cmdname': '/data/test_env/tinyCmd -N 15 -V -c 0 ', 'CmdId': 0x2263,
         'InstanseId': 0, 'CmdData': ' 0,0,0,0,4,0,0,0,8'},
        # {'CmdNotes': 'unmute without zero-detect 5s', 'Cmdname': '/data/test_env/tinyCmd -N 15 -V -c 0 ',
        #  'CmdId': 0x2262, 'InstanseId': 0, 'CmdData': '0,0,0x13,0x88,0'},
        # {'CmdNotes': 'unmute with zero-detect 5s', 'Cmdname': '/data/test_env/tinyCmd -N 15 -V -c 0 ',
        #  'CmdId': 0x2262, 'InstanseId': 0, 'CmdData': '0,0,0x13,0x88,1'},
        # {'CmdNotes': 'sink 0 link to source 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '0,0,0'},
        # {'CmdNotes': 'sink 0 link to source 1', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '1,0,0'},
        # {'CmdNotes': 'disconnect sink 0 link to source 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0202,
        #  'InstanseId': 0, 'CmdData': '0,0,0'},
        # {'CmdNotes': 'mute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,1,0,100'},
        # {'CmdNotes': 'unmute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,0,0,100'},
        # {'CmdNotes': 'volume -30db ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0,'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'volume 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0, 'CmdData': '0,0,0,0,100'},
        # {'CmdNotes': 'gain offset 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0,0,0,200'},
        # {'CmdNotes': 'gain offset -30db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,200'},
        # {'CmdNotes': 'ramp exponent', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2242, 'InstanseId': 0,
        #  'CmdData': '0,1,1,5'},
        # {'CmdNotes': 'ramp linear', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2242, 'InstanseId': 0,
        #  'CmdData': '0,0,0,0'},
        # {'CmdNotes': 'ramp 100ms', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0,
        #  'CmdData': '0,0xFE,0x20,0,100'}
        # {'CmdNotes': 'fade + 32767', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x10,0,0,0,0,0,0,0,0,0x7F,0xFF,0,0,0,0'},
        # {'CmdNotes': 'balance + 32767', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x08,0,0,0,0,0,0,0x7F,0xFF,0,0,0,0,0,0'},
        # {'CmdNotes': 'white niose  ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x221B, 'InstanseId': 0,
        #  'CmdData': '1,1,0x0,0x0,0x0,0x01,0,0,0,100,0x01,0xf4,0,0,0xfe,0xc0'}
    ]

    zone2cmd = [
        {'CmdNotes': 'dynamic mixer to front', 'Cmdname': '/data/test_env/tinyCmd -N 15 -V -c 0 ', 'CmdId': 0x2263,
         'InstanseId': 0, 'CmdData': ' 0,0,0,0,1,0,0,0,2'},
        # {'CmdNotes': 'sink 0 link to source 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '0,0,0'},
        # {'CmdNotes': 'sink 0 link to source 1', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '1,0,0'},
        # {'CmdNotes': 'mute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,1,0,100'},
        # {'CmdNotes': 'unmute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,0,0,100'},
        # {'CmdNotes': 'volume -30db ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'volume 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0,         'CmdData': '0,0,0,0,100'},
        # {'CmdNotes': 'gain offset 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0,0,0,200'},
        # {'CmdNotes': 'gain offset -30db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,200'},
        # {'CmdNotes': 'ramp exponent', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2242, 'InstanseId': 0,
        #  'CmdData': '0,1,1,5'},
        # {'CmdNotes': 'ramp 100ms', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0,
        #  'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'fade - 32768', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x10,0,0,0,0,0,0,0,0,0x80,0x00,0,0,0,0'},
        # {'CmdNotes': 'balance -32768', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x08,0,0,0,0,0,0,0x80,0,0,0,0,0,0,0'},
        # {'CmdNotes': 'pink niose  ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x221B, 'InstanseId': 0,
        #  'CmdData': '2,1,0x0,0x0,0x0,0x01,0,0,0,100,0x01,0xf4,0,0,0xfe,0xc0'}
    ]
    zone3cmd = [
        # {'CmdNotes': 'sink 0 link to source 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '0,0,0'},
        # {'CmdNotes': 'sink 0 link to source 1', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x0201, 'InstanseId': 0, 'CmdData': '1,0,0'},
        # {'CmdNotes': 'mute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,1,0,100'},
        # {'CmdNotes': 'unmute', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2201, 'InstanseId': 0, 'CmdData': '0,0,0,100'},
        # {'CmdNotes': 'volume -30db ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'volume 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0,         'CmdData': '0,0,0,0,100'},
        # {'CmdNotes': 'gain offset 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0,0,0,200'},
        # {'CmdNotes': 'gain offset -30db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2204, 'InstanseId': 0, 'CmdData': '0,0xFE,0x20,0,200'},
        # {'CmdNotes': 'ramp exponent', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2242, 'InstanseId': 0,
        #  'CmdData': '0,1,1,5'},
        # {'CmdNotes': 'ramp 100ms', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2203, 'InstanseId': 0,
        #  'CmdData': '0,0xFE,0x20,0,100'},
        # {'CmdNotes': 'fade 0db', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x10,0,0,0,0,0,0,0,0,0x0,0x0,0,0,0,0'},
        # {'CmdNotes': 'balance 0', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x08,0,0,0,0,0,0,0,0,0,0,0,0,0,0'},
        # {'CmdNotes': 'balance -32768', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x2202, 'InstanseId': 0,
        #  'CmdData': '0,0x0,0x08,0,0,0,0,0,0,0x80,0,0,0,0,0,0,0'},
        # {'CmdNotes': 'pink/0x0,0x01,0,0,0,100,0x01,0xf4,0,0,0xfe,0xc0'},
        # {'CmdNotes': 'niose gen off ', 'Cmdname': 'dummy_audiomanagement ', 'CmdId': 0x221B, 'InstanseId': 0,
        #  'CmdData': '0'}
    ]

##routine begin here
# zone0 cmd
gencmdbyzone(zone0cmd)
# between zone0 and zone1
call_delay(5000)

if (playflag == True):
    if (source == 1):
        audioplay('chirp_48K_20hz_20khz_2CH_40s_-15dB.wav', 'pcmTTS_p')
    elif (source == 0):
        # audioplay('chirp_48K_20hz_20khz_2CH_40s_-15dB.wav', 'Media')
        # audioplay('sin_1000Hz_11s019s1_0dB_48k_2ch_le32.wav', 'Media')
        audioplay('Someone_girl_48k_2ch.wav', 'Media')
    else:
        print('Error\n')

if (dumpflag == True):
    predump()
    call_delay(2000)
    dumpfunction(20)

# between zone0 and zone1
call_delay(10000)

# zone1 cmd
gencmdbyzone(zone1cmd)

# between zone1 and zone2
call_delay(15000)

# zone2 cmd
gencmdbyzone(zone2cmd)

# between zone2 and zone3
call_delay(5000)

# zone3 cmd
gencmdbyzone(zone3cmd)

### write file end
file_object.write('End Sub   \n')
file_object.close()
