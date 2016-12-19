import RPi.GPIO as GPIO
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
true = 1
while(true):
                try:
                        response1 = urllib2.urlopen('http://salfarsmarthome.azurewebsites.net/buttonStatus.php')
                        status1 = response1.read()
                        response2 = urllib2.urlopen('http://salfarsmarthome.azurewebsites.net/buttonStatus2.php')
                        status2 = response2.read()
                        response3 = urllib2.urlopen('http://salfarsmarthome.azurewebsites.net/buttonStatus3.php')
                        status3 = response1.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                print("Status 1:",status1)
                if status1=='ON':
                                GPIO.output(5,True)
                elif status1=='OFF':
                                GPIO.output(5,False)
                print("Status 2:",status2)
                if status2=='ON':
                                GPIO.output(15,True)
                elif status2=='OFF':
                                GPIO.output(15,False) 
                print("Status 3:",status1)
                if status3=='ON':
                                GPIO.output(29,True)
                elif status3=='OFF':
                                GPIO.output(29,False)
