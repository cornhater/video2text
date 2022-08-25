from convertation_utils import *
from directory_utils import *
from parameters import *

from tkinter import filedialog


@clear_workspace
def button() -> None:
    video_file_path = filedialog.askopenfilename(initialdir = "/",
                                        title = "Выберите видео")
    video_to_speech(video_file_path)
    speech_to_text(PARSED_SPEECH)