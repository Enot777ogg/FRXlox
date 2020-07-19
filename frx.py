print ("HE ДОБРО ПOжAЛOBATЬ") 
import os 
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
print (Fore.RED + 'Запуск Нейросети')
time.sleep(5)
print (Fore.RED + 'Нейросеть запущена')
time_count = 10 
for i in range(time_count, 0, -1): 
  print("осталось {} секунд".format(i))
  time.sleep(1)
print("питон спиздили")
