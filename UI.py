import parameters
from convertation_utils import button

from tkinter import *
from tkinter import filedialog


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x300")
        self.title('Конвертёр видео в текст')

        self.ask = Button(text='Выберите видео',
                            height = 3,
                            width = 27,
                            command=self.ask_file)
        self.ask.pack(padx=10, pady=15)

        self.label = Label(text='Доброго полудня!')
        self.label.pack(padx=10, pady=5)

        self.convert = Button(text='Конвертировать видео',
                            height = 3,
                            width = 27,
                            command=button)
        self.convert["state"] = "disabled"
        self.convert.pack(padx=10, pady=15)

        self.exit = Button(text='Выход',
                            height = 3,
                            width = 27,
                            command=self.destroy)
        self.exit.pack(padx=10, pady=15)


    def ask_file(self) -> None:
        parameters.VIDEO_FILE = filedialog.askopenfilename(initialdir = "/",
                                    title = "Выберите видео")
        if parameters.VIDEO_FILE[-4:] in ['.mp4', '.wav', '.mov']:
            self.convert["state"] = "normal"
            self.label["text"] = parameters.VIDEO_FILE
        else:
            self.convert["state"] = "disabled"
            self.label["text"] = 'Это не видео, долбаёб.'


    def update_label(self, text) -> None:
        self.label["text"] = text

