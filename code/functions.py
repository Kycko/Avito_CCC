### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from csv import DictReader

# Common functions
def read_file(file):
    data   = []
    for row in DictReader(open(file), delimiter=';'):
        data.append(row)
    return data
def dict_counter(dict, key):
    if key in dict.keys():
        dict[key] += 1
    else:
        dict[key]  = 1
    return dict
def sum_dicts(final, cur):
    for key in cur.keys():
        if key:             # just to avoid showing blank '' counter
            if key in final.keys():
                final[key] += cur[key]
            else:
                final[key]  = cur[key]
    return final

# Counting etc.
def count_final_numbers(files):
    data = {'total'    : 0,
            'CS'       : {},
            'SS'       : {},
            'cars'     : {},
            'goods'    : {},
            'services' : {}}
    for file in files:
        data['total']   += len      (file.data)
        data['CS']       = sum_dicts(data['CS'],       file.CS)
        data['SS']       = sum_dicts(data['SS'],       file.SS)
        data['cars']     = sum_dicts(data['cars'],     file.cars)
        data['goods']    = sum_dicts(data['goods'],    file.goods)
        data['services'] = sum_dicts(data['services'], file.services)
    return data
def construct_final_msg(data):
    lines      = ['-Всего контактов за день: ' + str(data['total'])]
    status_len = 50

    if data['CS']:
        lines = final_msg_add_dict('-Статусы звонков:',                          lines, data['CS'], status_len)
    if data['SS']:
        lines = final_msg_add_dict('-Конечные категории для "опрос состоялся":', lines, data['SS'], status_len)

    lines.append('-' * status_len)
    if data['cars']:
        lines.append('-' * status_len)
        lines.append('-Согласия в автосервисах: ' + str(data['cars']['Автосервис']))
    if data['goods']:
        lines = final_msg_add_dict('-Согласия в товарах:', lines, data['goods'],    status_len)
    if data['services']:
        lines = final_msg_add_dict('-Согласия в услугах:', lines, data['services'], status_len)

    for i in range(len(lines)):
        list = lines[i].split(' ')
        try:
            int(list[-1])
            list[-2] += ' ' * (status_len - len(lines[i]))
            lines[i]  = ' '.join(list)
        except:
            list = ''

    msg = ''
    for line in lines:
        if msg:
            msg += '\n'
        msg += line
    return msg
def final_msg_add_dict(title, lines, dict, status_len):
    lines.append('-' * status_len)
    lines.append(title)
    for key in sorted(dict.keys()):
        msg = ' -' + key + ': ' + str(dict[key])
        lines.append(msg)
    return lines
