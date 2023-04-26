import os
import webbrowser
#os.system('cmd /k "python manage.py runserver"')



# Windows
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
# Linux
#chrome_path = '/usr/bin/google-chrome %s'
#webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open("elearning.wsldp.com/python3/")
#webbrowser.get(chrome_path).open(url)
webbrowser.register('chrome',webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(urL)
