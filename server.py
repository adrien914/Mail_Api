import smtplib, ssl


class Server():
    def __init__(self, addr, port):
        try:
            self.addr = addr
            self.port = port

            try:
                print("Trying to establish an smtp connection to " + str(addr) + " with port " + str(port) + "...\n")
                self.smtp = smtplib.SMTP(addr, port)
                self.context = ssl.create_default_context()
                try:
                    print("Securing the connection...\n")
                    self.smtp.ehlo()
                    self.smtp.starttls(context=self.context)
                    self.smtp.ehlo()
                except Exception as e:
                    print("starttls() raised an exception : " + str(e))
            except Exception as e:
                print("smptlib.SMTP() raised an exception : " + str(e))
        except Exception as e:
            print("The Server object need to have the following arguments in the same order to be instantiated: addr, port")
            
    def getSmtp(self):
        return self.smtp

    def closeSmtp(self):
        try:
            print("Closing the connection to the server...")
            self.smtp.quit()
            print("Successfuly closed connection to the server ... See ya!")
        except Exception as e:
            print("close() raised an exception : " + str(e))