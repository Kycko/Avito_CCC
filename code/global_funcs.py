### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from csv import DictReader

def read_file(file):
    data   = []
    for row in DictReader(open(file), delimiter=';'):
        data.append(row)
    return data
