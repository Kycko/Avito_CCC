### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from global_funcs import *

class File():
    def __init__(self, file):
        self.data = read_file(file)
        print(self.data)
