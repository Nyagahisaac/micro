def mail_message(subject,template,to,**kwargs):
    sender_email = nyagahisaac21@gmail.com

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
