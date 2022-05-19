import smtplib


class sendEmail:
    def __init__(self, myEmail:str, toEmail:str, myPassword: str, subject:str, message: str):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(myEmail, myPassword)
        self.connection.sendmail(
            from_addr= myEmail,
            to_addrs= toEmail,
            msg= f"Subject: {subject} \n\n"
                 f"{message}"
        )
