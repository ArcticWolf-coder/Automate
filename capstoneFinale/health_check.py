import  shutil,emails,email,psutil,socket

def err_mail(sub):
    send="automation@example.com"
    receive="student-04-a16fc9e8738a@example.com"
    body="Please check your system and resolve the issue as soon as possible."
    mail=email.message.EmailMessage()
    mail["From"]=send
    mail["To"]=receive
    mail["Subject"]=sub
    mail.set_content(body)
    emails.send(mail)

#checking for free space in disk
def check_disk_usage():
    du = shutil.disk_usage("/")
    free_percent = du.free/du.total*100
    if free_percent < 20:
        subject_line = "Error - Available disk space is less than 20%"
        err_mail(subject_line)

#check for cpu usage for 1 second
def check_cpu_percent():
    usage = psutil.cpu_percent(1)
    if usage > 80:
        subject_line = "Error - CPU usage is over 80%"
        err_mail(subject_line)

#check for Available RAM
def check_RAM_mem():
    RAM_data = psutil.virtual_memory()
    avail_mem = RAM_data.available/(1024**2)
    if avail_mem < 500:
        subject_line = "Error - Available memory is less than 500MB"
        err_mail(subject_line)

#check for "localhost" ip address resolved to "127.0.01"
def check_ip():
    ip_addr = socket.gethostbyname("localhost")
    if ip_addr != "127.0.0.1":
        subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
        err_mail(subject_line)

   

if __name__ == "__main__":
    check_disk_usage()
    check_cpu_percent()
    check_RAM_mem()
    check_ip()