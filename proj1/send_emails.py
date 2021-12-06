import os
import pandas as pd 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




def sendingemails():

    current_path = os.getcwd()
    response_path= current_path+'/sample_input'
    os.chdir(response_path)
    
    Responses_df = pd.read_csv('responses.csv',index_col='Timestamp')
    
    email_list = Responses_df["Email address"].values.tolist()
    IITP_webmail_list =Responses_df["IITP webmail"].values.tolist() 
    roll_list = Responses_df["Roll Number"].values.tolist()
    list=[]
    for i in range(0,len(roll_list)):
        list.append([roll_list[i],email_list[i],IITP_webmail_list[i]])
    os.chdir(current_path) 
    myoutput_path = current_path+'/sample_output'+'/marksheet'
    os.chdir(myoutput_path)
    for i in range(0,len(list)): 
        for j in range(1,3):  
            fromaddr = "prabhasnaik16@gmail.com"
            toaddr = list[i][j]
            msg = MIMEMultipart() 
            msg['From'] = fromaddr 
            msg['To'] = toaddr 
            msg['Subject'] = "Quiz marks"
            body = "Your Quiz marks"
            msg.attach(MIMEText(body, 'plain')) 
            filename = "{}.xlsx".format(list[i][0])
            attachment = open("{}.xlsx".format(list[i][0]), "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "N@IK15326prabhas")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            s.quit()