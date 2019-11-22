from mail import Mail

def main():
    mail = Mail("admin@apiimail.ayome.ch", "Ayomi75010@")
    mail.sendMail("admin@apiimail.ayome.ch", "Hello", "Is it me your looking for ?")
    mail.closeConnection()
if __name__ == '__main__':
    main()
