import os

class OSManager:

    def __init__(self):
        pass

    def clear_console_log(self):
        os.system('cls' if os.name == 'nt' else 'clear')