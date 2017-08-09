#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'little4bigcz@163.com'  # 发件人邮箱账号
my_pass = 'nvoc102011'  # 发件人邮箱密码

#my_user = 'little4bigcz@163.com'  # 收件人邮箱账号，我这边发送给自己
my_user = 'binghunxuluo@qq.com'  # 收件人邮箱账号，我这边发送给自己

def mail():
    ret = True
    stringOne = '''haghfghdfghdfg34563453haha 1'''
    stringTwo = ''' 	  ------------------------------------
	       AutoFlowchart Version 1.0
	  ------------------------------------

what's is AutoFlowchart?
--------------------------------------------------------------------
    AutoFlowchart v1.0,the Professional sourcecode flowcharting tool.

    AutoFlowchart is a excellent tool to generate flowchart from
    sourcecode.Its flowchart can expand and shrink. and you can
    pre-define the  the  width , height,Horizontal spacing and
    vertical spacing. Move and zoom is also very easy.  It can
    export the flowchart as a Microsoft Word file or a  bitmap
    file.    It can help programmers understand,  document and
    visualize source code.

    It supports C,C++,VC++(Visual C++ .NET),Delphi(Object Pascal).
    In the future,It will support more languages.

    You can use it on Windows 9X/NT/me/XP.

    You can trial it for 30 times.  Registration fee is $79.
    http://www.ezprog.com/order.htm


Get Started
--------------------------------------------------------------------
    1. Open a *.pas/*.c/*.cpp file;
    2. Double click the begin row of any statement ,then you
       can see a flowchart;
    3. Click a apart of the FlowChart ,you can see the part
       of sentence of this block;
    4. change the value of the first spinedit,you can see the
       current block.


Register Notes:

    If you are a registered user, please put the license file
    to the install path.


Check out our WWW Home Page:

    http://www.ezprog.com


AutoFlowchart can be ordered for $79 from:

    CompuServe:	ShareIt (#197238)
    Direct:	http://www.shareit.com/product.html?productid=197238&languageid=1


Contact
--------------------------------------------------------------------
	support	: support@ezprog.com
	sales	: sals@ezprog.com
	Msn	: support@ezprog.com


          _______
     ____|__     |               (R)
  --|       |    |-------------------
    |   ____|__  |  Association of
    |  |       |_|  Shareware
    |__|   o   |    Professionals
  -----|   |   |---------------------
       |___|___|    MEMBER

'''
    try:
        msg = MIMEText(stringOne, 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "陈卓发送邮件测试"  # 邮件的主题，也可以说是标题
        print("run smtp")
        #server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        print("run login")
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失2败")