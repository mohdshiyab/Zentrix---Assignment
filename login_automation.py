"""
Selenium script - Task 2
-------------------------
Opens the Laravel project's login page (from Task 1), fills the email and
password fields with randomly generated values, and exits.

Target page  : http://da.adlynk.in:8000/login
Form fields  : #email (name="email_address"), #password (name="password")

Usage:
    python3 login_automation.py

Requirements:
    pip install selenium
    A Chrome/Chromium browser + matching chromedriver on PATH
    (or set CHROMEDRIVER_PATH / CHROME_BINARY_PATH env vars below).
"""

import os
import random
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LOGIN_URL = os.environ.get("LOGIN_URL", "http://da.adlynk.in:8000/login")

# Optional overrides - leave blank to let Selenium auto-detect Chrome/driver.
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH", "")
CHROME_BINARY_PATH = os.environ.get("CHROME_BINARY_PATH", "")

HEADLESS = os.environ.get("HEADLESS", "true").lower() == "true"


def random_email() -> str:
    """Generate a random, plausible-looking email address."""
    local_part = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domains = ["example.com", "test.com", "mail.com", "demo.org"]
    return f"{local_part}@{random.choice(domains)}"


def random_password(length: int = 12) -> str:
    """Generate a random password with letters, digits, and punctuation."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choices(chars, k=length))


def build_driver() -> webdriver.Chrome:
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,900")

    if CHROME_BINARY_PATH:
        options.binary_location = CHROME_BINARY_PATH

    if CHROMEDRIVER_PATH:
        service = Service(executable_path=CHROMEDRIVER_PATH)
        return webdriver.Chrome(service=service, options=options)

    # Let Selenium Manager auto-resolve the driver.
    return webdriver.Chrome(options=options)


def main():
    email_value = random_email()
    password_value = random_password()

    print(f"Opening login page: {LOGIN_URL}")
    driver = build_driver()

    try:
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 15)

        email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
        password_field = driver.find_element(By.ID, "password")

        print(f"Filling email field with: {email_value}")
        email_field.clear()
        email_field.send_keys(email_value)

        print(f"Filling password field with: {password_value}")
        password_field.clear()
        password_field.send_keys(password_value)

        # Small pause so the fill is visible if running non-headless.
        time.sleep(1)

        print("Form filled successfully.")

        if os.environ.get("SAVE_SCREENSHOT"):
            driver.save_screenshot(os.environ["SAVE_SCREENSHOT"])
            print(f"Screenshot saved to {os.environ['SAVE_SCREENSHOT']}")

        # NOTE: The task only asks to fill the fields and exit - not submit.
        # Uncomment the next two lines if you also want to submit the form:
        # submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # submit_btn.click()

    finally:
        driver.quit()
        print("Browser closed. Done.")


if __name__ == "__main__":
    main()
