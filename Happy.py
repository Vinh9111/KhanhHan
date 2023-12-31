import os



import requests,os,time,re,json,uuid,random,sys



from concurrent.futures import ThreadPoolExecutor

import sys,subprocess

from colorama import Fore, Back, Style

from colorama import init, AnsiToWin32

init(wrap=False)

subprocess.run("clear", shell=True)

stream = AnsiToWin32(sys.stderr).stream

default = print(Fore.MAGENTA + """

 .----------------.  .----------------.  .----------------.  .----------------. 

| .--------------. || .--------------. || .--------------. || .--------------. |

| |    _____     | || |     ____     | || |    _____     | || |   _    _     | |

| |   / ___ `.   | || |   .'    '.   | || |   / ___ `.   | || |  | |  | |    | |

| |  |_/___) |   | || |  |  .--.  |  | || |  |_/___) |   | || |  | |__| |_   | |

| |   .'____.'   | || |  | |    | |  | || |   .'____.'   | || |  |____   _|  | |

| |  / /____     | || |  |  `--'  |  | || |  / /____     | || |      _| |_   | |

| |  |_______|   | || |   '.____.'   | || |  |_______|   | || |     |_____|  | |

| |              | || |              | || |              | || |              | |

| '--------------' || '--------------' || '--------------' || '--------------' |

 '----------------'  '----------------'  '----------------'  '----------------' 

""", file=stream)

default = input(Fore.CYAN + """[ ♡ ] Nay là ngày 31/12 (Dương lịch)



Ngày cuối cùng năm 2023



Chúc em, cô gái anh thương bước sang năm mới thật vui vẻ, hạnh phúc, luôn xinh đẹp nè, gặp nhiều may mắn, và điều đặc biệt hãy luôn đồng hành cùng anh trên con đường mà hai ta đã chọn nha.



YÊU EMM : Enter dii vk """) 

ban = Fore.MAGENTA + """

\037  _____①①①______❶❶❶_____

\036  ___①__*_*_①__❶_*_*__❶___

\035  ___①_*_*_*_*❶*_*_*_*_❶___

\034  ____①_*_*_*_**_*_*_*_❶____

\033   ______①_*_*_**_*_*_❶______

\032  _________①__**__❶_________

\031  _____________❶_____________ ︎︎︎︎

 ︎︎︎︎︎︎

\030  

 __      __                          ________               

|  \    /  \                        |        \              

 \$$\  /  $$______   __    __       | $$$$$$$$ ______ ____  

  \$$\/  $$/      \ |  \  |  \      | $$__    |      \    \ 

   \$$  $$|  $$$$$$\| $$  | $$      | $$  \   | $$$$$$\$$$$\

                           \$$$$ | $$    $$| $$  | $$      | $$$$$   | $$ | $$ | $$

    | $$  | $$$$$$$$| $$__/ $$      | $$_____ | $$ | $$ | $$

    | $$   \$$     \ \$$    $$      | $$     \| $$ | $$ | $$

     \$$    \$$$$$$$  \$$$$$$        \$$$$$$$$ \$$  \$$  \$$

                                                            

                                                            

                                                            



"""

def banner():



  os.system("clear")



  for h in ban:

    sys.stdout.write(h)

    sys.stdout.flush()

    time.sleep(0.0003)   

banner()

amount = 5000

default = input(Fore.MAGENTA + """ Hihi ♡ """)
