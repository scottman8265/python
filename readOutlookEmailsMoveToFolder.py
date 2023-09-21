import imaplib
import email

user = "scriptjet@gmail.com"
password = "E^55*mH8GN"
imap_url = "imap.gmail.com"

myMail = imaplib.IMAP4_SSL(imap_url)
myMail.login(user, password)
myMail.select("Inbox")
key="To"
value="You"
result, data = myMail.search(None, key, value)
mailIDlist = data[0].split()

print("Total emails: ", len(mailIDlist))
