from datetime import datetime

def driverPath():
    return r'C:\Users\xua\Downloads\chromedriver_win32\chromedriver.exe'

def baseUrl():
    return "https://www.google.com/"

#change time to str

def getCurrentTime():
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)

# Get time diff
def timeDiff(starttime,endtime):
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(endtime,format) - datetime.strptime(starttime,format)