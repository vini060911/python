from tkinter import *
from App import *

class App:
    def __init__(self) -> None:
        class ScreenConfigs:
            def __init__(self) -> None:
                self.size = int()
                self.name = str()
                self.baseName = str()
                self.className = str()
                self.title = str()
        self.screen = Tk()
        self.screenConfigs = ScreenConfigs()
        self.screen.geometry(self.screenConfigs.size)
        self.screen.title(self.screenConfigs.title)

        class Input:
            def __init__(self) -> None :
                click = []
                class button:
                    def __init__(self) -> None:
                        pass
                self.button = button   
                self.text = Text
                self.radio = Radiobutton
                self.checkbox = Checkbutton
        self.Input = Input
app = App()
bt = app.Input().button()
