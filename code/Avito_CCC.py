### Anthony Samartsev <ant.samarcev@gmail.com>
### GNU GPL 3 or higher; http://www.gnu.org/licenses/gpl.html

from classes            import *
from functions          import *
from tkinter.filedialog import askopenfilenames

files = []
for file in askopenfilenames():
    files.append(File(file))

if files:
    window = Window(construct_final_msg(count_final_numbers(files)))
    window.mainloop()
