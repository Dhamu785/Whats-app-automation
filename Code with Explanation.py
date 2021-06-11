#import the module
import pywhatkit

#It will ask your for the mobile number
number = input("Enter the number with the country code : ")

#It will ask your for the message
msg = input("Enter the message : ")

#It will ask you for the time in hours (From 00 to 23)
hours = int(input("Enter the hour in railwaytime : "))

#It will ask you for the minites (From 00 to 59)
minit = int(input("Enter the minutes : "))

#Function to send the message according to the given inputs
def send():
    
    #If there is no erroe ir will get into the next strp in the try method
    try:
        
      #Here is the main part sending message with the module
      pywhatkit.sendwhatmsg(number,msg,hours,minit)
        
      #If message send successfully it will print this
      print("MESSAGE SENT SUCCESSFULLY : )")
        
    #If any errors occured it will get into the except method.
    except:
        print('Enter the time before 30 seconds')
        
#For calling the function
send()
