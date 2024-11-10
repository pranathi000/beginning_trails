from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyttsx3

# CUSTOM MODULES
import main
from webdriver_manager.chrome import ChromeDriverManager


def whatsapp_send(name, msg):
    # Initialize Chrome driver with ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com')
    
    # Wait for QR code to be scanned (adjust sleep time if necessary)
    time.sleep(10)  # Give extra time for QR scan if needed
    
    try:
        # Wait until the contact is visible, then find the user
        user = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@title="{name}"]'))
        )
        user.click()
        
        # Wait for the message box to appear
        msg_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]'))
        )
        msg_box.send_keys(msg)
        
        # Wait for the send button and click it
        msg_send = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button'))
        )
        msg_send.click()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(5)  # Wait to confirm the message is sent before closing
        driver.quit()


def askinfo(r):  # Accept the recognizer instance as a parameter
    main.respond("Whom do you want to send a message?")
    user = main.listen(r)  # Pass the recognizer instance to listen
    main.respond(f"Please tell me the message to send to {user}.")
    message = main.listen(r)  # Pass the recognizer instance to listen
    main.respond("Scan the QR code on the next screen to continue login to WhatsApp.")
    whatsapp_send(user, message)
    main.respond("Message sent as you said, sir!")

