import smtplib

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from datetime import datetime
import ResultFolder


def send_email(send_from,send_to,subject,text,files=None,server="10.210.41.203"):

    #assert(isinstance(send_to,list),"Send To email should be a list")

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text,'html'))

    with open(files,"rb") as f:
        part = MIMEApplication(f.read(),Name=basename(files))
        msg.attach(part)
    smtp = smtplib.SMTP(server,0)
    smtp.sendmail(send_from,send_to,msg.as_string())
    smtp.quit()

def send_report():
    send_f = "alvin.xu@igt.com"
    send_t = "alvin.xu@igt.com"
    
    subject = "[Automaiton]TestReport_"+str(datetime.today())
    
    files = ResultFolder.GetRunDirectory()+"\TestResult.html" 
    with open(files,'r') as f:
        text = f.read()

    send_email(send_f,send_t,subject,text,files)
