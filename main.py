from convertation_utils import *
from tkinter import *
from tkinter import filedialog
from sys import exit

def speech_to_text(parsed_speech_path: str) -> None:
    '''
    creates file with text, parsed from audio file with speech
    '''
    r = sr.Recognizer()
    total_duration = parse_speech_duration(parsed_speech_path)
    for i in tqdm(range(0, total_duration)):
        with sr.AudioFile(parsed_speech_path) as source:
            audio = r.record(source, offset=i*60, duration=60)
        f = open("transcription.txt", "a")
        f.write(r.recognize_google(audio, language='ru-RU'))
        f.write(" ")
    f.close()


def convert():
    video_file_path = filedialog.askopenfilename(initialdir = "/",
                                           title = "Select a file")
    video_to_speech(video_file_path)
    speech_to_text('parsed_speech.wav')
    clear_workspace()
    exit()


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title('Конвертёр видео в текст')

        self.button = Button(text='Выберите видео',
                            height = 3,
                            width = 27,
                            command=convert)
        self.button.grid(column = 1, row = 1, padx = 10, pady= 10)

if __name__ == '__main__':
    app = App()
    app.mainloop()
    