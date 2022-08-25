from parameters import *

import wave, math, contextlib
from moviepy.editor import AudioFileClip


def video_to_speech(video_path: str) -> AudioFileClip:
    '''converts video file to .wav and saves in project directory'''
    audioclip = AudioFileClip(video_path)
    audioclip.write_audiofile(PARSED_SPEECH)
    return audioclip


def parse_speech_duration(parsed_speech_path: str) -> float:
    '''returns duration of audio file'''
    with contextlib.closing(wave.open(parsed_speech_path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    total_duration = math.ceil(duration / 60)
    return total_duration


