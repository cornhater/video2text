from convertation_utils import *
from parameters import *
from directory_utils import remove

import speech_recognition as sr
from tkinter import *
from tkinter import filedialog, ttk
from sys import exit
from tqdm.tk import tqdm, trange
import os


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x100")
        self.title('Конвертёр видео в текст')

        self.button = Button(text='Выберите видео',
                            height = 3,
                            width = 27,
                            command=self.convert)
        self.button.pack(padx=10, pady=15)


    def convert(self) -> None:
        if PARSED_TEXT in os.listdir(os.getcwd()):
            remove(PARSED_TEXT)
        video_file_path = filedialog.askopenfilename(initialdir = "/",
                                            title = "Выберите видео")
        video_to_speech(video_file_path)
        r = sr.Recognizer()
        total_duration = parse_speech_duration(PARSED_SPEECH)
        for i in trange(0, total_duration):
            with sr.AudioFile(PARSED_SPEECH) as source:
                audio = r.record(source, offset=i*60, duration=60)
            f = open(PARSED_TEXT, "a")
            f.write(r.recognize_google(audio, language='ru-RU'))
            f.write(" ")
            app.update_idletasks()
        f.close()
        remove(PARSED_SPEECH)
        exit()


if __name__ == '__main__':
    app = App()
    app.mainloop()
