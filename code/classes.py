### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from datetime  import date, datetime
from functions import dict_counter, read_file
from tkinter   import Text, Tk, WORD

class File():
    def __init__(self, file):
        self.init_data = read_file(file)
        self.data      = []
        self.max_date  = date(2023, 1, 1)

        self.CS        = {}     # CS = call statuses
        self.SS        = {}     # SS = successful survey
        self.cars      = {}     # автосервисы
        self.goods     = {}
        self.services  = {}

        # filter only today calls
        str = 'Время начала звонка'
        for line in self.init_data:
            if line[str]:
                line[str] = datetime.strptime(line[str], '%Y-%m-%d %H:%M:%S')
                cur       = line[str].date()
                if cur > self.max_date:
                    self.max_date = cur
        for line in self.init_data:
            if line[str] and line[str].date() == self.max_date:
                self.data.append(line)

        for line in self.data:
            CS         = line['Статус звонка']
            SS         = line['Конечная категория']
            goods      = line['Категория клиента от КЦ (товары)']
            services   = line['Категория клиента от КЦ (услуги)']

            self.CS = dict_counter(self.CS, CS)
            if CS in ('Опрос состоялся', 'Дозвон успешный'):
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
        self.resizable(0,0)
        self.title('Avito call center counter')
        text = Text(self, height=34, width=60, padx=3, font='Consolas 13', wrap=WORD)
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
