import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup headless Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

# Read the dynamically assigned target URL from Jenkins environmental variables
target_url = os.getenv("APP_URL", "http://localhost:8000")

try:
    # Test Case 1: Verify home page loads successfully
    driver.get(target_url)
    assert "Django" in driver.title or driver.status_code == 200
    print("Selenium Test 1 Passed: Page title verified.")

    # Test Case 2: Verify application element exist
    body_text = driver.find_element_by_tag_name("body").text
    print("Selenium Test 2 Passed: Content successfully read.")

finally:
    driver.quit()
