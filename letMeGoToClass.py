from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import argparse
import time
import os

parser = argparse.ArgumentParser(description="Let me go to class")
parser.add_argument("website_url", help="URL of the page")
args = parser.parse_args()

website_url = args.website_url

hello_club_password = os.getenv("HELLO_CLUB_PASS")
hello_club_email = os.getenv("HELLO_CLUB_EMAIL")


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome( options=chrome_options)

driver.get(website_url)


login_portal_button = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > ui-view > portal-route > div > div > login-route > div > section > button.Button.Button--oauth.Button--success.Button--portal.ng-scope"))) 
login_portal_button.click()

username_login_form_input =  WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > ui-view > portal-route > div > div > login-credentials-route > div > section > form > div:nth-child(1) > input"))
)

password_login_form_input =  driver.find_element(By.CSS_SELECTOR, "body > ui-view > portal-route > div > div > login-credentials-route > div > section > form > div:nth-child(2) > input")


username_login_form_input.send_keys(hello_club_email) 
password_login_form_input.send_keys(hello_club_password) 


login_button = driver.find_element(By.CSS_SELECTOR, "body > ui-view > portal-route > div > div > login-credentials-route > div > section > form > div:nth-child(3) > button")
login_button.click()
time.sleep(3)

has_signed_in = True
while has_signed_in:
    try:
        sign_up_button = driver.find_element(By.CSS_SELECTOR, "body > ui-view > app-route > div > main > ui-view > event-view-route > div > div > cards > div > card:nth-child(2) > div > card-event-summary > section > div.EventOptions.ng-scope > div:nth-child(1) > button")
        

        if(sign_up_button.text == "event_available SIGN UP"):
            
            sign_up_button.click()
            print("Slot available! Booking now...")
            
            time.sleep(3)

            sign_up_button_confirm = driver.find_element(By.CSS_SELECTOR, "body > ui-view > app-route > div > main > ui-view > event-signup-route > div > div > cards > div > card:nth-child(2) > div > card-event-signup-details > card-footer > footer > button-bar > div > div > button.Button.Button--success.ng-animate-disabled")
            sign_up_button_confirm.click()
            time.sleep(3)

            has_signed_in = False
            print("Closing letMeGoTOClass...")
        else:
            print("No slots available. Retrying in 5 minutes...")
            time.sleep(295)
            driver.refresh()
            time.sleep(5)


    except Exception as somethingWrong:

        print("it broke, oh dear :(")  
        print("**************ERROR**************")
        print("*********************************")
        print(somethingWrong)
        break          


