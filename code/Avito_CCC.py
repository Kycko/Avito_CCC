### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from my_class           import File
from tkinter.filedialog import askopenfilenames

files = []
for file in askopenfilenames():
    files.append(File(file))
