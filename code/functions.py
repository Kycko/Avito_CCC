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
    data = {'total' : 0,
            'CS'    : {}}
    for file in files:
        data['total'] += len(file.data)
        for key in file.CS.keys():
            if key:
                if key not in data['CS'].keys():
                    data['CS'][key] = 0
                data['CS'][key] += file.CS[key]
    return data
def construct_final_msg(data):
    lines = ['-Всего контактов за день: ' + str(data['total'])]
    lines.append('-' * len(lines[0]))

    lines.append('-Статусы звонков:')
    for key in sorted(data['CS'].keys()):
        lines.append(' -' + key + ': ' + str(data['CS'][key]))

    msg = ''
    for line in lines:
        if msg:
            msg += '\n'
        msg += line
    return msg
