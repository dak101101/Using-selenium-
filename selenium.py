from selenium import webdriver
from selenium.webdriver.common.by import By #web driver is a part of selenium that controls browsers 
import schedule
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Scan the QR code and press Enter...")
   
group_name = "Test group" 
message = "Hello everyone, this is the weekly reminder!"

def send_message():

    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(group_name)

    time.sleep(3)


    group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
    group.click()

    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    msg_box.send_keys(message)

    time.sleep(2)

    msg_box.send_keys("\n")
    print("Message sent to group!")

# Schedule the message
schedule.every(1).minutes.do(send_message)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(30)