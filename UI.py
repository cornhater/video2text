from controller import button

from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x150")
        self.title('Конвертёр видео в текст')

        self.button = Button(text='Выберите видео',
                            height = 3,
                            width = 27,
                            command=button)
        self.button.pack(padx=10, pady=15)

        self.t = Label(text='Hi there!')
        self.t.pack(padx=10, pady=7)

        self.mainloop()


if __name__ == '__main__':
    app = App()

