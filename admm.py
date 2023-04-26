import os
import webbrowser
os.system('cmd /k "python manage.py runserver"')



url = 'http://127.0.0.1:8000/'

# MacOS
#chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# Windows
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
# Linux
#chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get("google-chrome").open("elearning.wsldp.com/python3/")
#webbrowser.get(chrome_path).open(url)
