from email.message import EmailMessage
import smtplib, getpass
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

mess = EmailMessage()

send = "me@example.com"
receive = "you@example.com"
mess["From"] = send
mess["To"] = receive
mess["Subject"] = "Greetings from {} to {}!".format(send, receive)
body = """Hey there!
I'm learning to send mails using python."""
mess.set_content(body)

print(mess)

mail_server = smtplib.SMTP_SSL("smtp.example.com")
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass("Password? ")
print(mail_pass)
mail_server.login(send, mail_pass)
mail_server.send_message(mess)
mail_server.quit()


fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13,
}
report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

