import pywhatkit
number = input("Enter the number with the country code : ")
msg = input("Enter the message : ")
hours = int(input("Enter the hour in railwaytime : "))
minit = int(input("Enter the minutes : "))
def send():
    try:
      pywhatkit.sendwhatmsg(number,msg,hours,minit)
      print("MESSAGE SENT SUCCESSFULLY : )")
    except:
        print('Enter the time before 30 seconds')
send()
