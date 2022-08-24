import os


def remove(filename: str):
    os.system(f'rm {filename}')


def clear_workspace(func):
    '''
    decorator, cleaning workspace while main function working
    '''
    def wrapper():
        if 'transcription.txt' in os.listdir(os.getcwd()):
            remove('transcription.txt')
        func()
        remove('parsed_speech.wav')
    return wrapper