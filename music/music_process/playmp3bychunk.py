"""PyAudio Example: Play a mp3 file. once a chunk"""

import pyaudio
import sys
from pydub import AudioSegment
from matplotlib import pyplot as plt
# file = r'1.mp3'

def plotaudio(data):
    plt.plot(data)
    plt.xlabel('time')
    plt.ylabel('amp')
    plt.title('time domain')
    plt.grid('true')
    plt.show(block=False)

def playmp3(file):
    # read audio file different style,now mp3 style
    song = AudioSegment.from_mp3(file)
    CHUNK = 2048
    # wf = wave.open(sys.argv[1], 'rb')
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    # open stream (2)
    stream = p.open(format=p.get_format_from_width(song.sample_width),
                                               channels=song.channels,
                                               rate=song.frame_rate,
                                               output=True)
    # read data
    length = len(song.raw_data)
    # print 'length = ',length
    # num = length/CHUNK+1
    piece = 1
    if length < CHUNK:
        data = song.raw_data
    else:
        data = song.raw_data[0:CHUNK*piece]

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        left = length - CHUNK*piece
        # print "left = ",left

        if left < CHUNK:#last chunk
            data = song.raw_data[CHUNK*piece:length]
        else:
            data = song.raw_data[CHUNK*piece:CHUNK*(piece+1)]

        piece = piece + 1
        # print "piece = ",piece
        if left < 0:
            break

    stream.write(data)
    # stop stream (4)
    stream.stop_stream()
    stream.close()


    # close PyAudio (5)
    p.terminate()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Plays a mp3 file.\n\nUsage: %s filename.mp3" % sys.argv[0])
        sys.exit(-1)
    playmp3(sys.argv[1])
    # playmp3(file)