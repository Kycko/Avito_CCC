### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

import csv
from tkinter import filedialog

file   = filedialog.askopenfilename()
reader = csv.DictReader(open(file), delimiter=';')
for row in reader:
    print(row)
