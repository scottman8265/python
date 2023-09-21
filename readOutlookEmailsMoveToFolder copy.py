import win32com.client
import pandas as pd
import datetime
import os

#folder path for where the emails are saved
folder = r'C:\Users\scrip\emails\Emails'

#folder path of where results files will be saved
result_folder = r'C:\Users\XX\Desktop\Result'

#open outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#iterate over emails in folder
emails = []
for email_file in os.listdir(folder):
    if email_file.endswith('.msg'): #only process .msg files
        email_path = os.path.join(folder, email_file)
        msg = outlook.OpenSharedItem(email_path)
        emails.append({
            'Filename': email_file,
            'To': msg.To,
            'Cc': msg.Cc,
            'From': msg.SenderName,
            'Subject': msg.Subject,
            'Body': msg.body,
            'SentDateTime': datetime.datetime.fromtimestamp(timestamp=msg.SentOn.timestamp(), tz=msg.SentOn.tzinfo).strftime('%Y-%m-%d %H:%M')
        })

#convert list of dictionaries to DataFrame
data = pd.DataFrame(emails)