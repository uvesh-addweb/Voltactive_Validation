from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from urllib.parse import urlparse
import logging


@given('The sitemap URL is "{sitemap_url}"')
def set_sitemap_url(context, sitemap_url):
    context.driver.get(sitemap_url)
    context.sitemap_url = sitemap_url


@when('I check for console errors in sitemap pages')
def check_for_console_errors(context):
    context.pages_with_errors = []

    # Define a function to check console errors
    def check_console_errors(driver, url):
        console_errors = []
        logs = driver.get_log('browser')
        console_errors = [log['message'] for log in logs if log['level'] == 'SEVERE']
        print("Console Error : " , logs)
        if logs != []:
            page_slug = urlparse(url).path.split('/')[-1]
            allure.attach(f"Page : {url} \n \nConsole Error : {logs}", f"Error on {url} Page", allure.attachment_type.TEXT)
            allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {url} Page",
                          attachment_type=allure.attachment_type.PNG)
        return console_errors

    url_array = []

    # Iterate through sitemap pages and check console errors
    ul_element = context.driver.find_element(By.XPATH, '//*[@id="post-17282"]/div/section/div/div/div/div/li/ul')
    urls = ul_element.find_elements(By.TAG_NAME, 'a')
    for url in urls:
        page_a_tag_url = url.get_attribute('href')
        url_array.append(page_a_tag_url)

    for url in url_array:
        # page_url = url.get_attribute('href')
        print("Navigating Page : ", url)
        context.driver.get(url)

        wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed

        # Wait for the page to load completely
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        wait.until(lambda driver: driver.execute_script("return document.readyState === 'complete';"))
        wait.until(lambda driver: driver.execute_script("return jQuery.active === 0;"))

        # Scroll down to the bottom of the page
        # context.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

        console_errors = check_console_errors(context.driver, url)

        if console_errors:
            context.pages_with_errors.append((url, console_errors))
            allure.attach(f"Console Error : {context.pages_with_errors}", "", allure.attachment_type.TEXT)
            allure.attach(f"Console errors on {url}:", "\n".join(console_errors),
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)


@then('I should see the console errors for each page, if any')
def report_console_errors(context):
    for page_url, errors in context.pages_with_errors:
        page_slug = urlparse(page_url).path.split('/')[-1]
        allure.attach(f"Console errors on {page_url}:", "\n".join(errors), attachment_type=allure.attachment_type.TEXT)
        # Take a screenshot for this specific page
        context.driver.get(page_url)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
