# O2WebTextScript
Script using Selenium Web Driver to login to O2 and auto send text messages to anyone.

This project started some time back with the idea of creating a community text alert scheme (for free) for Residents Association I'm part of and for which I do a lot of the IT bits and bobs for. In any case, I figured, if I can do soem webscraping, how hard can it be to create a script to login and send a web text. Well as it turns out, not that hard although not that easy either.

Key to this little project was the Selenium Web Driver as the O2 Website contains a lot of Javascript and so I needed to emulate a real browser to get past this. Either that or I'd need to create a far more complex engine that would support JS otherwise. Perhaps it would be possible to call some of the JS elements directly but I simply don't know enough about JS to do that.

The script basically has two main functions "checkAndSendEmail()" and "sendTextMessage()"

checkAndSendEmail()
The first function needs both the emaila and also the O2 account login details passed to it for it to do it's business. It uses the poplib framework to get all the recent messages from the email account using PoP3 and then for each messages kicks off the next stage of the process. The message is trunkated to 319 characters and Sent through to "sendTextMessage()"

Note* there is an option to include or no some of the message details like date and subject etc. Also, there is an option to supply a list of numbers, if this is set at the end of the code in the main section, the each number in the list must be separated by a comma and a space.

sendTextMessage()
This is where the magic happens and was the most fiddly bit to get working. The code actually fires up the Firefox web browser and has to loop through a couple of login pages before you actually get to the WebText Screen. I've left a lot of the failed attempts from the code in there for anyone else that might be looking to experiment.

Note* Just to note, I had to do a bit of troubleshooting with this when we were using it for a work text alert system to notify us of any critical issues or outages. "EnumProcesses()" was added to make sure that loads of concurrent versions of the script didn't kick off as I was using it 

You'll need an O2 account to use this and will obviously need to have Python installed and an email account to use. Also key as mentioned is the Firefox browser and Selenium Webdriver: http://selenium-python.readthedocs.org/en/latest/getting-started.html

Overall, there are still a few kinks in the system, like the fact that it doesn't handle emails with non standard mime types and so on but if you send it basic html or text based emails, it works a treat.
