import requests
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium import webdriver

# Replace with your sitemap URL
sitemap_url = "stg.alignorgstg:e3f1ccf1@a-lign.com/sitemap.xml"

@given('The user is on the Sitemap page')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize the webdriver
    context.driver.get(sitemap_url)

@when('The user verifies all URLs')
def step_impl(context):
    # Get all the <a> elements in the sitemap
    ul = context.driver.find_elements(By.XPATH, "//*[@id=\"wrapper\"]/div[2]/div/div/div/div[1]/div[1]/ul")
    a_elements = ul.find_elements(By.TAG_NAME, "a")

    context.failed_urls = []

    for a in a_elements:
        url = a.get_attribute("href")
        if url:
            # Verify URL redirection
            context.driver.get(url)
            current_url = context.driver.current_url
            if current_url != url:
                context.failed_urls.append(url)
                context.driver.save_screenshot(f"screenshot_{url}.png")

    context.driver.quit()

@then('All URLs should be redirected correctly')
def step_impl(context):
    assert not context.failed_urls, f"Failed URLs: {context.failed_urls}"

    # for url in context.failed_urls:
    #     allure.attach(f"Screenshot of failed URL: {url}", context.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

