### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from functions import dict_counter, read_file
from tkinter   import Text, Tk, WORD

class File():
    def __init__(self, file):
        self.data     = read_file(file)
        self.CS       = {}              # CS = call statuses
        self.SS       = {}              # SS = successful survey

        self.cars     = {}              # автосервисы
        self.goods    = {}
        self.services = {}

        for line in self.data:
            CS        = line['Статус звонка']
            SS        = line['Конечная категория']
            goods     = line['Категория клиента от КЦ (товары)']
            services  = line['Категория клиента от КЦ (услуги)']

            self.CS = dict_counter(self.CS, CS)
            if CS == 'Опрос состоялся':
                self.SS = dict_counter(self.SS, SS)
            if SS == 'Согласие':
                if goods   == 'Автосервис':
                    self.cars     = dict_counter(self.cars,     goods)
                elif goods == 'Ответ не сохранен':
                    self.services = dict_counter(self.services, services)
                else:
                    self.goods    = dict_counter(self.goods,    goods)

class Window(Tk):
    def __init__(self, msg):
        super().__init__()
        self.attributes('-topmost', True)
        self.title('Avito call center counter')
        text = Text(self, height=35, width=51, padx=3, font='Consolas 13', wrap=WORD)
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
