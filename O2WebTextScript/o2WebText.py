###################
# LOAD FRAMEWORKS #
###################
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# for calling JS in code
#JavascriptExecutor js = (JavascriptExecutor) webDriver();

import time

# Used for email pop check
import poplib
from email import parser

#####################
# EMAIL ALERT CHECK #
#####################

def checkAndSendEmail(loginUsername,loginPassword,popServer,emaailAddress,emailpassword,numberList,incDetails="yes"):

	# s = raw_input()
	# try:
	#     i = int(s)
	# except ValueError:
	#     i = 0

	#try:
	
	loginUsername = loginUsername
	loginPassword = loginPassword
	incDetails = incDetails

	print "Checking Connecting to Account"
	pop_conn = poplib.POP3_SSL(popServer)
	pop_conn.user(emaailAddress)
	pop_conn.pass_(emailpassword)

	(numMsgs, totalSize) = pop_conn.stat()
	print "Message Count: " + str(numMsgs)
	if numMsgs == 0:
			print "No new emails"
			return
	


	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)] 	# Get messages from server:
	messages = ["\n".join(mssg[1]) for mssg in messages]							# Concat message pieces:
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]				# Parse message into an email object:

	#numberList = ""

	for message in messages:

		txtMessage = ""
		txtMessage += "From: " + message["From"]
		print "From: " + message["From"] 

		txtMessage += " | Date: " + message["Date"] 
		print "Date: " + message["Date"] 

		txtMessage += " | Subject: " + message['subject']
		print "Subject: " + message['subject'] + "  | Message: "

		if incDetails == "no":
				txtMessage = ""

		print "Message Contents: "
		#print message.get_payload(decode=True)
		
		# Handle differnt email content types
		try: 
			print message.get_payload()[ 0 ].get_payload()
			txtMessage += str(message.get_payload()[ 0 ].get_payload())
		except:
			print message.get_payload()
			txtMessage += str(message.get_payload())
			
		

		txtMessage = txtMessage[0:319]

		if numberList is "":	# If no numbers are passed through then we want the phone number from the subject 
			phoneNumber = message['subject'] + " "
			print "no numbers passed thro"
		else:
			phoneNumber = numberList
			print "phone list supplied"
			
		print "!!!TEXT MESSAGE!!! = " 
		textmessagetest = phoneNumber + " " + txtMessage
		textmessagetest= textmessagetest[0:319]
		print textmessagetest

		sendTextMessage(loginUsername, loginPassword, txtMessage, phoneNumber)

	#sys.exit(0)

	print pop_conn.stat()
	pop_conn.list(1)
	pop_conn.retr(1)
	pop_conn.quit()

	# except (ValueError, AttributeError, RuntimeError, TypeError, NameError):
	# 	print "Exception in account check, might be because there are No New Emails"
	# 	traceback.print_exc(file=sys.stdout)

	




#############################
# SEND TEXT MESSAGE SECTION #
#############################

def sendTextMessage(loginUsername, loginPassword, txtMessage, phoneNumber="0876831770"):

	loginUsername = loginUsername
	loginPassword = loginPassword
	phoneNumber = phoneNumber
	txtMessage = txtMessage

	browser = webdriver.Firefox()	# Get local session of firefox
	browser.get("http://www.o2online.ie/o2/login/") # Load page
	#browser.get("http://www.o2online.ie/o2/my-o2/")

	assert "unavailable" not in browser.title	# Check to see if O2 is online as is sometimes down for maintenance
	 
	print "Starting Login Procedure!"
	#((JavascriptExecutor)driver).executeScript("document.getElementByClassName(right_side).style.visibility = 'visible';");
	#js.ExecuteScript("document.getElementByClassName(right_side).style.visibility = 'visible';")
	#browser.execute_script("document.getElementByClassName('right_side').style.visibility = 'visible';")
	#browser.execute_script("document.getElementByClassName('o2login_form').style.display='div.right_side';")
	#browser.execute_script("document.getElementByClassName('right_side').style.visibility = 'visible';")

	#browser.execute_script("document.getElementById('o2login_form').style.display='div.right_side';")

	# elem = browser.find_element_by_name("IDToken1") 	# Find the username box
	# elem.send_keys(loginUsername + Keys.RETURN)
	# elem = browser.find_element_by_name("IDToken2") 	# Find the password box
	# elem.send_keys(loginPassword + Keys.RETURN)
	# time.sleep(5.0) # Let the page load, will be added to the API

	# elem = browser.find_element_by_id("businesslogin") 	# Find the username box
	# elem.submit()
	#browser.execute_script("document.getElementById('IDToken1').style.visibility = 'visible';")

	#browser.execute_script("document.getElementById('IDToken2').style.visibility = 'visible';")
	#browser.execute_script("document.getElementById('o2login_form').style.display='div.right_side'")
	#browser.execute_script("document.getElementsByClassName('right_side')[0].style.visibility = 'visible';")

	#browser.execute_script("document.getElementById('fromThisPage').style.visibility = 'visible';")


	#browser.execute_script("document.body.style.display='right_side'")

	# #driver.find_element_by_xpath("//ol[@id='rso']/li[3]/div/h3/a/em").click()

	# #driver.execute_script("document.getElementByClassName('dropdown phone6 align-left').style.display='dropdown-menu hide-phone'")
	# #driver.execute_script("document.getElementByClassName('dropdown phone6 align-left').style.visibility = 'visible'")
	# browser.execute_script("document.getElementById('dLabel').style.display='dropdown-menu.hide-phone'")
	#browser.execute_script("document.getElementById('o2login_form').style.display='right_side'")
	#browser.execute_script("document.getElementsByTagName('div')[0].style.display = 'block';")
	browser.execute_script("document.getElementsByClassName('right_side')[0].style.display = 'block';")


	elem = browser.find_element_by_name("IDToken1") 	# Find the username box
	elem.send_keys(loginUsername + Keys.RETURN)
	elem = browser.find_element_by_name("IDToken2") 	# Find the password box
	elem.send_keys(loginPassword + Keys.RETURN)
	time.sleep(5.0) # Let the page load, will be added to the API


	# # LIST ALL LINKS
	# elements = browser.find_elements_by_xpath("//a")
	# for link in elements:
	# 	print str(link.get_attribute("href"))

	###################
	# LOGGED IN AREA  #
	###################

	print "Successfully Logged In"
	nextPage = browser.find_element_by_partial_link_text("webtext")
	print "Next Page is = " + nextPage.get_attribute("href")
	nextPage = nextPage.get_attribute("href")
	browser.get(nextPage) # Load page
	time.sleep(5.0)

	#########################
	# MESSAGING PAGE PART 1 #
	#########################



	elem = browser.find_element_by_name("username") 	# Find the username box
	elem.send_keys(loginUsername + Keys.TAB)
	elem = browser.find_element_by_name("password") 	# Find the password box
	elem.send_keys(loginPassword + Keys.RETURN)
	time.sleep(5.0) # Let the page load, will be added to the API


	assert "Messaging" in browser.title


	print "Finding iFrame!"
	elements = browser.find_elements_by_xpath("//frame")	# Search for the iFrame that the actual messaging page is contained in.
	for link in elements:
		print "iFrame Page Address is = " + str(link.get_attribute("src"))
		nextPage = str(link.get_attribute("src"))

	browser.get(nextPage) 	# Load Next Page
	time.sleep(10.0)		# Give it time to load, its a pretty slow site.

	#########################
	# MESSAGING PAGE PART 2 #
	#########################

	elem = browser.find_element_by_name("txtA_SMSMessage") 	# Find the Message box
	elem.send_keys(txtMessage + Keys.TAB)# Tab to the next field
	elem = browser.find_element_by_name("txt_SMSRecipient") # Find the Number box
	elem.send_keys(phoneNumber + Keys.RETURN)				# Enter phone number
	time.sleep(5.0)											# Give the Eval form time to run

	elements = browser.find_elements_by_xpath("//input[@alt='Send Web text Now']")	# Find the input value that triggers the send JS

	print "Sending Text Message to " + phoneNumber
	print "Message Contents = " + txtMessage

	for link in elements:
		#print str(link.get_attribute("src"))	# Enable this if you just want to verify that it has the right element
		# nextPage = str(link.get_attribute("src"))
		# nextPage = link
		print "Processing!"
		


	time.sleep(5.0)
	link.click()	# Click the F'in link!
	print "Text Message Sent!"
	time.sleep(5.0)
	browser.close()


#######################################################################



# """
# Enumerates active processes as seen under windows Task Manager on Win NT/2k/XP using PSAPI.dll
# (new api for processes) and using ctypes.Use it as you please.

# Based on information from http://support.microsoft.com/default.aspx?scid=KB;EN-US;Q175030&ID=KB;EN-US;Q175030

# By Eric Koome
# email ekoome@yahoo.com
# license GPL
# """
from ctypes import *
import time
import sys

#PSAPI.DLL
psapi = windll.psapi
#Kernel32.DLL
kernel = windll.kernel32



def EnumProcesses():
	#Keeps a count of how many python processes are running
	pythonRunningCounter = 0

	arr = c_ulong * 256
	lpidProcess= arr()
	cb = sizeof(lpidProcess)
	cbNeeded = c_ulong()
	hModule = c_ulong()
	count = c_ulong()
	modname = c_buffer(30)
	PROCESS_QUERY_INFORMATION = 0x0400
	PROCESS_VM_READ = 0x0010
	
	#Call Enumprocesses to get hold of process id's
	psapi.EnumProcesses(byref(lpidProcess), cb, byref(cbNeeded))
	
	#Number of processes returned
	nReturned = cbNeeded.value/sizeof(c_ulong())
	
	pidProcess = [i for i in lpidProcess][:nReturned]
	
	for pid in pidProcess:
		
		#Get handle to the process based on PID
		hProcess = kernel.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
		if hProcess:
			psapi.EnumProcessModules(hProcess, byref(hModule), sizeof(hModule), byref(count))
			psapi.GetModuleBaseNameA(hProcess, hModule.value, modname, sizeof(modname))
			processName = "".join([ i for i in modname if i != '\x00'])
			print processName
			
			#-- Clean up
			for i in range(modname._length_):
				modname[i]='\x00'
			
			kernel.CloseHandle(hProcess)

			if "python.exe" in processName:
				pythonRunningCounter = pythonRunningCounter + 1
				if int(pythonRunningCounter) > 1:
					print "Text Alert Already Running, try again Later"
					time.sleep(3.0)
					sys.exit(0)
	
if __name__ == '__main__':
	EnumProcesses()



############################################################################




# Initiate Number List
numberList = ""

#checkAndSendEmail()
# Personal Emails
#print "Checking Danger Mouse Account"
#checkAndSendEmail(' - O2 Account Login - ','PASSWORD','EMAIL SERVER',' - EMAIL ACCOUNT - ','PASSWORD',numberList, 'INCLUDE MSG DETAILS') 
#checkAndSendEmail('denisfinnegan@gmail.com','xxxxxxxxx','pop.gmail.com','dangermousealert@gmail.com','xxxxxxxxx',"0876831770")


# Work Check
#print "Checking Tesco Diets Account"
#checkAndSendEmail(' - O2 Account Login - ','PASSWORD','EMAIL SERVER',' - EMAIL ACCOUNT - ','PASSWORD',numberList, 'INCLUDE MSG DETAILS') 
#checkAndSendEmail('0860485223','xxxxxxxxx','pop.gmail.com','tescodietsalert@gmail.com','xxxxxxxxx',"0876831770, 0868563879 ")


# Work Check
#print "Checking Tesco Diets Other Account"
#checkAndSendEmail(' - O2 Account Login - ','PASSWORD','EMAIL SERVER',' - EMAIL ACCOUNT - ','PASSWORD',numberList, 'INCLUDE MSG DETAILS') 
#checkAndSendEmail('0860485223','xxxxxxxxx','pop.gmail.com','tdietalerts@gmail.com','xxxxxxxxx',"0876831770, 0868563879 ")


# Denis Text Account Check
print "Checking Denis Text Account"
#checkAndSendEmail(' - O2 Account Login - ','PASSWORD','EMAIL SERVER',' - EMAIL ACCOUNT - ','PASSWORD',numberList, 'INCLUDE MSG DETAILS') 
checkAndSendEmail('denisfinnegan@gmail.com','xxxxxxxxx','pop.gmail.com','finmixtext@gmail.com','xxxxxxxxx',numberList, "no")
