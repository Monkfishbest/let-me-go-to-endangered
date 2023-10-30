# let-me-go-to-class
I want to go to class, but I don't want to check every 5 mins, this script will log you in, and then periodically refresh the class page and try and sign up. 
The program wil terminate when you have signed up. 

## required tech for mac 
Python3 
PiP3 (should come with python 3) 
brew 
chrome 


## start guide 

go to line 21, add the class you want to sign up to but some bastard(s) have already made it full, surely one of them will quit at the last minute, but you will be fucked if you want to check in every 5 mins, so let python do it for you. 

to install dependencies 
if you're on Linux/windows/wsl figure that stuff out yourself ;) 
`pip3 install selenium` 
`brew install webdriver` 

## Run code 
If you want to run it in headless, i've added the code that I think will do in a comment, I have not checked that so it might not work but I don't see why I wouldn't, maybe the site will not let you use it in headless mode, I dunno, I presume you will know enough to fix it if you know what headless mode is. otherwise... 

`python3 letMeGoToClass.py`
and watch the magic happen. 

## Warning

I wrote this code in an hour after being at the pub, you run this code at your own risk, I am not responsible for the FBI showing up at your doorstep, your computer catching fire, you breaking your leg, or getting injured at the training you went to and any other stuff that happens to you, you run this code at your own risk, but I'm like 99% sure it works ¯\_(ツ)_/¯

Feel free to use, modify or use this code commercially, if you can convince someone to pay for 68 lines of code you deserve it.  
