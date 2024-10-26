from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (make sure to specify the path to your ChromeDriver)
driver = webdriver.Chrome()

# Navigate to the demo e-commerce site
driver.get('https://eu.dookan.com/account/login?country=fr')  # Replace with an actual demo site URL

# Locate the username and password fields and log in
username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'customer[email]')))
password = driver.find_element(By.NAME, 'customer[password]')


# username = driver.find_element(By.NAME, 'email')  # Change the locator as needed
# password = driver.find_element(By.NAME, 'password')  # Change the locator as needed

username.send_keys('harsht202@gmail.com')  # Replace with a demo username
password.send_keys('Password1234')    # Replace with a demo password

# password.send_keys(Keys.RETURN)        # Press Enter to log in

 # Locate the login button using By.ID (or By.NAME, By.XPATH, etc., based on your inspection)
login_button = driver.find_element(By.ID, 'customer_login')  # Adjust the locator as needed
login_button.click()  # Click the login button

# Wait for the login to process
time.sleep(15)  # Adjust the sleep time as needed

# Validate successful login by checking for a specific element
try:
    welcome_message = driver.find_element(By.ID, 'welcome')  # Adjust locator as needed
    print("Login Successful:", welcome_message.text)
except:
    print("Login Failed!")

# Close the browser
driver.quit()
