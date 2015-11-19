__author__ = 'sergey'



from smsapi import SmsApi

username = "<USERNAME>"
password = "<PASSWORD>"

sms = SmsApi(username, password)

total_points = sms.get_points()['points']
print "You have %s points left" % total_points