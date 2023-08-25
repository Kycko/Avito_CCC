### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from functions import read_file
from tkinter   import Text, Tk, WORD

class File():
    def __init__(self, file):
        self.data = read_file(file)
        self.CS   = {}              # CS = call statuses
        for line in self.data:
            L = line['Статус звонка']
            if L in self.CS.keys():
                self.CS[L] += 1
            else:
                self.CS[L]  = 0

class Window(Tk):
    def __init__(self, msg):
        super().__init__()
        self.resizable(0,0)
        self.title('Avito call center counter')
        text = Text(self, height=20, width=60, padx=3, font='Consolas 13', wrap=WORD)
        text.pack(padx=5, pady=5)
        text.insert(1.0, msg)
        self.bind_all('<Key>', self._onKeyRelease, '+')
    def _onKeyRelease(self, event):
        result = ''
        if   event.keycode == 88 and event.keysym.lower() != 'x':
            result = '<<Cut>>'
        elif event.keycode == 86 and event.keysym.lower() != 'v':
            result = '<<Paste>>'
        elif event.keycode == 67 and event.keysym.lower() != 'c':
            result = '<<Copy>>'
        if result and (event.state & 0x4) != 0:
            event.widget.event_generate(result)
