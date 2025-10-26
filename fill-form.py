from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# hnju lleh eacx atec

def fill_google_form():
    # Setup Chrome
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the form
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
    time.sleep(3)

    # Find all input fields (should be 7 now)
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')

    # Find the textarea (for address)
    textarea = driver.find_element(By.CSS_SELECTOR, 'textarea.KHxj8b.tL9Q4c')

    # Data to fill
    data = {
        "fullname": "Hadi Badami",
        "contact": "9974964814",
        "email": "hadibadami14@gmail.com",
        "address": "Makarba, Ahmedabad",
        "pincode": "380055",
        "dob": "2006-01-14",  # YYYY-MM-DD format for date input
        "gender": "Male"
    }

    # Fill the fields sequentially (7 inputs + 1 textarea)
    inputs[0].send_keys(data["fullname"])
    inputs[1].send_keys(data["contact"])
    inputs[2].send_keys(data["email"])
    textarea.send_keys(data["address"])
    inputs[3].send_keys(data["pincode"])
    inputs[4].send_keys(data["dob"])
    inputs[5].send_keys(data["gender"])

    # Extract the verification code (inside <b> tag)
    code = driver.find_element(By.XPATH, '//span[@class="M7eMe"]/b').text.strip()
    print(f"Detected code: {code}")

    # Fill the last input (code field)
    inputs[6].send_keys(code)

    # ✅ Corrected: Click submit button using proper selector
    submit_button = driver.find_element(By.XPATH, '//div[@role="button" and @jsname="M2UYVd"]')
    driver.execute_script("arguments[0].click();", submit_button)

    # Wait for confirmation page and take screenshot
    time.sleep(4)
    driver.save_screenshot("form_confirmation.png")
    print("✅ Form submitted successfully. Screenshot saved as form_confirmation.png")

    driver.quit()

if __name__ == "__main__":
    fill_google_form()
