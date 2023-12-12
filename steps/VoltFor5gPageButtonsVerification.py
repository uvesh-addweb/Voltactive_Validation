from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import logging


@given(u'The user is on the Volt for 5g page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # Hover the mouse on the main link to trigger sub-links appearance
    context.driver.execute_script('window.scrollTo(0, 0);')
    context.driver.implicitly_wait(3)
    why_volt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-1584"]/a')))
    context.driver.execute_script('arguments[0].scrollIntoView();', why_volt)
    why_volt.click()
    ActionChains(context.driver).move_to_element(why_volt).perform()

    context.volt_for_5g = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-20627"]/a')))
    context.volt_for_5g.click()
    context.driver.implicitly_wait(5)

    print("The user is on the No Compromises page")

@when(u'Get the Buttons and links from the Volt for 5g page')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed

        # First array to store the web elements
        context.web_elements = [
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-20300"]/div/section/div[7]/div/div/div/div[2]/div[1]/div/div/div[2]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-20300"]/div/section/div[9]/div/div/div/div[2]/div[2]/div/div/div[2]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-20300"]/div/section/div[11]/div/div/div/div[2]/div[1]/div/div/div[2]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-20300"]/div/section/div[13]/div/div/div/div[2]/div[2]/div/div/div[2]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-20300"]/div/section/div[25]/div/div/div/div[3]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="resources-list"]/div[1]/div/div/div[2]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="resources-list"]/div[2]/div/div/div[2]/a'))),
        ]

        # Second array to store the links
        context.links = [
            "https://www.voltactivedata.com/use-cases/business-support-systems-bss/",
            "https://www.voltactivedata.com/resource/activen_lossless_xdcr/",
            "https://www.voltactivedata.com/resource/customer-management-infographic/",
            "https://www.voltactivedata.com/resource/revenue-assurance-business-overview/",
            "https://www.voltactivedata.com/try-volt/",
            "https://dev.voltactivedata.com/resource/5g-policy-survey-results/",
            "https://dev.voltactivedata.com/resource/powering-real-time-mediation-for-telcos/"
        ]

    except Exception as e:
        print(f"An error occurred: {e}")


@then(u'Verify that the links and buttons are enable and clickable on Volt for 5g page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        def verify_redirection(context, element, link):
            element.click()
            context.driver.implicitly_wait(3)
            current_url = context.driver.current_url
            if current_url == link:
                print(f"Redirection is proper. Current URL: {current_url}, Expected URL: {link}")
                logging.info(f"Redirection is proper. Current URL: {current_url}, Expected URL: {link}")
                context.driver.back()
                context.driver.implicitly_wait(3)
                return True
            else:
                print(f"Redirection is NOT proper. Current URL: {current_url}, Expected URL: {link}")
                context.driver.back()
                context.driver.implicitly_wait(3)
                return False

        def verify_element(element):
            return element.is_enabled() and element.is_displayed()

        for element, link in zip(context.web_elements, context.links):
            assert verify_element(element) is True
            assert verify_redirection(context, element, link) is True

    except Exception as e:
        print(f"An error occurred: {e}")

