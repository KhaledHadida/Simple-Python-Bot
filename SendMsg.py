import smtplib
import praw
from tkinter import *


#send mail 
def send_mail(text):
	#Create our object for sending msgs, first param domain, port (always 587)
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

	#Establish a connection with Gmail 
	smtpObj.starttls()
	#login creditentials 
	smtpObj.login(e3.get(),e4.get())

	#send email, first param from, to, subject
	smtpObj.sendmail(e3.get(),e3.get(), text)
	#quit 
	print(text)
	smtpObj.quit()

#accessing our reddit topics and storing it in "text"
def redditApi(text):
	
	reddit = praw.Reddit(client_id ='private',
					client_secret = 'private',
					user_agent= 'private')

	searchField = "[" + e1.get() + "]"

	#for loop searches subreddits subs
	for submission in reddit.subreddit('bapcsalescanada').new(limit=20):
		
		if searchField in submission.title.lower():
			text += submission.title
			text += '\n'
			text += submission.url
			text += '\n'

	return text	

#compares text file to current data from api
def compareStrings(current):
	
	try:
		f = open("Output.txt","r")
		message = f.read()
		

		if(message != current):
		
			text_file = open("Output.txt", "w")
			text_file.write(current)
			send_mail(current)
			

	except:
		print("ERROR: You do not have an Output.txt, Let me create you one for you..")
		f = open('Output.txt','w')
		print("done!")

	


def task():
    print("test")
    compareStrings(redditApi(text))
    #time is in mili seconds    
    gui.after(e2.get(), task)
    
	

#creating window 
gui = Tk()

text =""

#Resolution
gui.geometry('200x130')

#creating label (like top part)
label = Label(gui,text="Keyword (lower)")
#position x,y
label.grid(row=1,column=2)

time_label = Label(gui,text="Time (mili-seconds)")

time_label.grid(row=3,column=2)

user_label = Label(gui,text="Email")
user_label.grid(row=4,column=2)

pass_label = Label(gui,text="password")
pass_label.grid(row=5,column=2)


#creating button, gui, text, function
B = Button(gui, text ="Start", command=lambda:task())

#position
B.grid(row=2,column=3)

#field and position 
e1 = Entry(gui)
e1.grid(row=1, column=3)
e2 = Entry(gui)
e2.grid(row=3,column=3)

e3 = Entry(gui)
e3.grid(row=4,column=3)

e4 = Entry(gui,show="*")
e4.grid(row=5,column=3)



#loop the gui, keep it running
gui.mainloop()







