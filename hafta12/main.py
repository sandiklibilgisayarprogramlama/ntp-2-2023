"""

- buildin(dahili) 
ilk python kurulumunda kurulan paketler
os
random
string
math
- 

import os

# eğer deneme çalışma dizininde yoksa klasör oluştur
if "deneme" not in os.listdir():
    os.mkdir("deneme")
#print(os.listdir())


import random

#print(int(random.random()*100)) # 0 ile 100 (100 dahil değil) arasında rastgele sayı uretir
#print(random.randint(0,10)) # 0 ile 10 arasında rastgele sayı üretir


import string


print(string.punctuation)


import math

print(math.sqrt(25))






Python masaüstü uygulama geliştirme
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()






# dahili sqlite paketi
import sqlite3


# 1. yok 
import os

os.listdir()

#2. yok
import sqlite3 as sq

sq.connect()

# 3. yol
from os import listdir


# 4. yol
from os import *


import os 
# modul içerisindeki tüm değişken ve fonksiyonları görüntüleyebiliriz.
print(dir(os))

"""