import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("sender's email", "sender's password")


msg = MIMEMultipart('alternative')
msg['Subject'] = "IIT DELHI | REGISTRATION FOR BECON'21 | URGENT"
msg['From'] = "arnavsudan314@gmail.com"
msg['To'] = "CC of the mail"
name = []
email = ['arnavsudan314@gmail.com', 'rajgolhani03@gmail.com'] #BCC of mail
number = ['8882331701' , '8435302591']
names = ['Arnav Sudan' , 'Raj']
for i in range (0,434):
    time.sleep(10)

    link_to_razorpay = "https://pages.razorpay.com/pl_GscV4VHY1EjW4D/view?email=" + email[i] + "&phone=" + number[i]
    name = names[i]

    # Create the body of the message (a plain-text and an HTML version).
    text = "Pay 149rs here to complete your registration: https://pages.razorpay.com/pl_GscV4VHY1EjW4D/view"
    html = """\
    <html>
    <head></head>
    <body>
     <strong>Greetings from Entrepreneurship Development Cell, IIT Delhi</strong>
    <br><br>
    <b>Congratulations {name}! </b> on your successful registration for BECon'21. You are just a click away from experiencing a magnificent 4-day entrepreneurial extravaganza at the annual Business and Entrepreneurship Conclave BECon 2021. Seats are filling faster than ever, for the first time that it is happening in the virtual mode.
    <br><br>

    <b>About BECon:</b> eDC IITD is hosting its <b>Annual Business and Entrepreneurship Conclave 2021</b> (BECON), from <b>1st to 4th April 2021</b>, with the theme of <b>Revolutionizing the Paradigm: Going Beyond!</b> BECon is North India’s biggest E-Summit, with numerous events, keynote lectures of eminent personalities, workshops, panel discussions, and much more! Some notable guests in the past include <b>Mark Zuckerberg (CEO, Facebook), Jack Dorsey (CEO, Twitter), Dara Khosrowshahi (CEO, Uber), and Elie Seidman (CEO, Tinder)</b> and many more. You will have an astonishing experience of <b>townhall sessions, panel talks, networking sessions, creators conclave, founders talk and numerous competitions.</b>
<br><br>
You will receive <b>participation certificates</b> for all the events you attend, along with an opportunity for <b>one-on-one interaction with the guest speakers.</b>


<br><br>
To confirm your seat for the conclave, you are kindly requested to pay the required fees of <b>Rs 149</b>.
<br><br>
Complete your payment now using <a href= {link_to_razorpay}>Pay Now </a> 
<br><br>
Offical website of Becon 2021: <a href="https://edc.iitd.ac.in/becon/index.html"> https://edc.iitd.ac.in/becon </a>


<br><br>

You may contact the undermentioned in case of any queries. For more details, you can also visit our <a href="https://www.facebook.com/edciitdelhi">Facebook</a> /
<a href="https://www.linkedin.com/company/edc-iit-delhi/">LinkedIn</a> / 
<a href="https://www.instagram.com/edc_iitd/">Instagram</a> pages. 


<br><br> Regards,

<br> Arnav Sudan <br> Technical Executive, eDC IIT Delhi
<br><br>
<table style="width:100%">
  <tr>
    <th>Uddipan Debnath</th>
    <th>Ayush Pandey </th> 
  </tr>
  <tr>
    <td style="text-align:center"> Coordinator </td>
    <td style="text-align:center"> Coordinator </td>
  </tr>
  <tr>
    <td style="text-align:center"> eDC IIT Delhi   </td>
    <td style="text-align:center"> eDC IIT Delhi   </td>
  </tr>
  <tr>
    <td style="text-align:center"> +91 9366155938    </td>
    <td style="text-align:center">  +91 8290927498  </td>
  </tr>
</table>


  </body>
</html>
    """ .format(name = name ,link_to_razorpay=link_to_razorpay )


# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)


    s.sendmail("sender's email", email[i], msg.as_string())


s.quit()
