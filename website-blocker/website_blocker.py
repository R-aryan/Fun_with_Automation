import time
from datetime import datetime as dt

hosts_path= r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","fb.com","facebook.com","www.hotmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16) :
        print("working hours..")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            print(content)

    
    else:
        print("fun hours....")
    time.sleep(5)


