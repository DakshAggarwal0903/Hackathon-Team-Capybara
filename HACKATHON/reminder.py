import time as tm
from winotify import Notification
import math


toast = Notification(app_id="windows app",
                     title="Reminder",
                     msg="",
                     icon=r"C:\Users\daksh\OneDrive\Desktop\clock.png")

def reminder():
    remtime = input("For what time should the reminder be?")
    remtime = remtime.split(':')
    while True:
        localtime = tm.asctime(tm.localtime(tm.time()))
        localtime = localtime.split()
        localtime = localtime[3]
        localtime = localtime.split(':')
        if remtime[0] == localtime[0] and remtime[1] == localtime[1]:
            toast.show()
            break
        



        
