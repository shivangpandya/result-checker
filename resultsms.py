from twilio.rest import TwilioRestClient #SMS API Package
import urllib2
import re
import time
 
account_sid = "AC05fe50769478b162b83e6fddc6838212" #Your Twilio account ID
auth_token = "eb8403256724d11819f0067cc7a713b9"    #Your secret API Token
 
client = TwilioRestClient(account_sid, auth_token)
 
while 1:
 
    html_content = urllib2.urlopen('https://www.gtu.ac.in/result.aspx').read()
 
    matches = re.findall('BE SEM 6 - Regular', html_content);
 
 
    if len(matches) == 0: 
       print "Yeah, Result Not Declared. Going to sleep" #will not send anything
       time.sleep(7200) #sleep for 2 hours
 
    else:
       msg = client.messages.create(to="Your_number", from_="Your_twilio_number", body="Oops! Resutls out, Best of Luck. Here you go:http://result1.gtu.ac.in") #Will send SMS to your phone number
       print "SMS Sent Thanks"
       quit()