# This script was created by Mary Sheahen of Eramis Technologies on 5/16/2013
# The script is meant to run periodically and send text alerts when rimfire .22 caliber
# ammunition is in stock on Cabela's website

import urllib.request
import smtplib

# open the ammo variable file for reading a writing, this should be the path 
f = open('C:/Users/Mary/Desktop/Eramis/ammobotscript/a.txt', 'r+')
text = f.read()
print(text)

# rewind the file
f.seek(0)

# clear file content 
f.truncate()

# an ammo value of 0 means no ammo, 1 means ammo.  if we switch from 0 to 1, an event happens and we send the email.

# Mary Sheahen's personal email, && recipients
sender = 'sheahen.m@gmail.com'
receivers = ['5732891359@txt.att.net', 'sheahen.m@gmail.com']

# Generic message that there is something in stock
message = """Remington .22 LR caliber ammo has been found on Cabela!!"""

#itemName is the variable cabela's uses in their HTML when there is an item to show on their website.  
words = ['Remington']

# lets open the url and read it, then turn it into a string
linestr = urllib.request.urlopen("http://www.cabelas.com/catalog/browse/rimfire-ammunition/_/N-1100192+4294758999/Ne-4294758999/Ns-CATEGORY_SEQ_104536080?WTz_l=Unknown%3Bcat104792580%3Bcat104691780&WTz_st=GuidedNav&WTz_stype=GNU").read()
site = str( linestr, encoding='utf8' )

# Search the page's text for word
for word in words:

    #we found the word
    if word in site:
        
        # if this is a new product, we change ammo variable and send an email
        if(int(text)==0):
            f.write('1')
            f.close()
            print("we found some")
            try:
               smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
               smtpObj.ehlo()
               smtpObj.starttls()
               smtpObj.login('sheahen.m@gmail.com', 'born2$wim')
               smtpObj.sendmail(sender, receivers, message)
               print("email sent!")
               smtpObj.close()
               
            except smptEXCEPTION:
               print("Error: unable to send email")
               
        # we've already notified you about the product
        else:
            f.write('1')
            f.close()
            print("We didnt send anything cuz we already know")
            
    #we didnt find the word
    else:
        print(word, "not found")
        f.write('0')
        f.close
