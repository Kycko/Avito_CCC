### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from csv import DictReader

# Common functions
def read_file(file):
    data   = []
    for row in DictReader(open(file), delimiter=';'):
        data.append(row)
    return data

# Counting etc.
def count_final_numbers(files):
    data = {'total' : 0}
    for file in files:
        data['total'] += len(file.data)
    return data
def construct_final_msg(data):
    msg = '-Всего контактов за день: ' + str(data['total'])
    return msg
