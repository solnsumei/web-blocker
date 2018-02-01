import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "skysports.com", "www.skysports.com"]
written = False
app_started = False


def check_time():
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) \
            < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        return True
    return False


while True:
    if check_time():
        if not app_started or not written:
            print("Working hours...")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
            written = True
            app_started = True
    else:
        if not app_started or written:
            print("Flexing time...")
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                    else:
                        file.truncate()
                file.truncate()
            written = False
            app_started = True

    time.sleep(30)
