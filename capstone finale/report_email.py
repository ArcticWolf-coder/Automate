import os, datetime, reports, emails

times=datetime.date.today().strftime("%B %d, %Y")
title="Processed Update on {}".format(times)
path=""
path+="supplier-data/descriptions/"
sum=""
for i in os.listdir(path):
    with open(path+i,"r") as f:
        reads=f.read().split("\n")
        sum+="Name: {}<br/> Weight:{}<br/>".format(reads[0],reads[1])



if __name__ == "__main__":
    send="automation@example.com"
    receive="student-04-a16fc9e8738a@example.com"
    sub="Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attach="/tmp/processed.pdf"
    
    reports.generate_report(attach, title, sum)
    mail=emails.generate(send,receive,sub,body,attach)
    emails.send(mail)