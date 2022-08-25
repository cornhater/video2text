from parameters import *

import wave, math, contextlib
from moviepy.editor import AudioFileClip
import speech_recognition as sr
from tqdm import tqdm


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


def speech_to_text(parsed_speech_path: str) -> None:
    r = sr.Recognizer()
    total_duration = parse_speech_duration(parsed_speech_path)
    for i in tqdm(range(total_duration)):
        with sr.AudioFile(parsed_speech_path) as source:
            audio = r.record(source, offset=i*60, duration=60)
        f = open(PARSED_TEXT, "a")
        f.write(r.recognize_google(audio, language='ru-RU'))
        f.write(" ")
    f.close()

