from MAIL import mailSendClass
print("Start send mail")
mailOK = mailSendClass.mailSendCz()
SendReturn = mailOK.mail("hahahas224234")

if SendReturn:
    print("邮件发送成功")
else:
    print("邮件发送失2败")

