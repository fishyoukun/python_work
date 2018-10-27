"""PyAudio Example: Play a wave file."""

import pyaudio
# import wave
import sys
from pydub import AudioSegment

# file=r'1.mp3'

def playmp3(file):
    # read audio file different style,now mp3 style
    # song = AudioSegment.from_mp3(sys.argv[0])
    song = AudioSegment.from_mp3(file)
    CHUNK = 1024
    # wf = wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                 channels=wf.getnchannels(),
    #                 rate=wf.getframerate(),
    #                 output=True)
    stream = p.open(format=p.get_format_from_width(song.sample_width),
                                               channels=song.channels,
                                               rate=song.frame_rate,
                                               output=True)

    # read data
    data = song.raw_data
    # data = wf.readframes(CHUNK)

    # play stream (3)
    # while len(data) > 0:
    #     stream.write(data)
    # data = wf.readframes(CHUNK)
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