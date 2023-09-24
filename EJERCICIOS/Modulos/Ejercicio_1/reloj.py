import datetime
import os
import time
while True:
    dt= datetime.datetime.now()
    print (f"{dt.hour}:{dt.minute}:{dt.second}")
    time.sleep(1)
    os.system('cls')
