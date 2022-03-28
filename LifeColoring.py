import datetime
from excel import *
from gui import *

dt_now = datetime.datetime.now()
dir_path = "D:/record"
file_path = f"{dir_path}/{dt_now.date()}.xlsx"

while(1):
    task, category = Doing_what()
    dt_now = datetime.datetime.now()
    time = dt_now.time()
    startTime = f'{time.hour}:{time.minute}:{time.second}'
    save_excel(task, category, startTime)
    if ok_no_msgbox('Will you continue?') == False:
        break

closing_a_day()