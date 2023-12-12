from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import logging

# @given(u'The user is on the home page')
# def step_impl(context):
#     print("The User is on Home Page.")


@when(u'Get the Buttons and links from the page')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed

        # First array to store the web elements
        context.web_elements = [
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[1]/div/div/div/div/div/div/div/div[4]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[1]/div/div/div/div/div/div/div/div[5]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[5]/div/div/div/div[4]/div/div/div/div[3]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[3]/div[1]/div/div/div[3]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[3]/div[2]/div/div/div[3]/a'))),
            # wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[3]/div[3]/div/div/div[3]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[1]/div/div/div[3]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[2]/div/div/div[3]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[3]/div/div/div[3]/a'))),
            # wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[4]/div/div/div[3]/a'))),
            wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[10]/div/div/div/div[3]/a'))),
            wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="resources-list"]/div[1]/div/div/div[2]/a'))),
            wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="resources-list"]/div[2]/div/div/div[2]/a'))),
            wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="resources-list"]/div[3]/div/div/div[2]/a'))),
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="text-4"]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/a')))
        ]

        # Second array to store the links
        context.links = [
            "https://www.voltactivedata.com/try-volt/",
            "https://www.voltactivedata.com/partners/",
            "https://www.voltactivedata.com/no-compromises/",
            "https://www.voltactivedata.com/real-time-data-processing/",
            "https://www.voltactivedata.com/capabilities/",
            # "https://www.voltactivedata.com/use-cases/activesd-kafka-streaming/",
            "https://www.voltactivedata.com/use-cases/cloud-native/",
            "https://www.voltactivedata.com/use-cases/high-availability/",
            "https://www.voltactivedata.com/use-cases/geo-replication/",
            # "https://www.voltactivedata.com/use-cases/edge-optimized-architecture/",
            "https://www.voltactivedata.com/capabilities/",
            "https://dev.voltactivedata.com/resource/tm-forum-report-iot-at-the-edge/",
            "https://dev.voltactivedata.com/resource/guide-to-streaming-data-platforms/",
            "https://dev.voltactivedata.com/resource/stl-partners-report-revenue-opportunities-at-the-intersection-of-edge-iot/",
            "https://dev.voltactivedata.com/capabilities/"
        ]

    except Exception as e:
        print(f"An error occurred: {e}")

@then(u'Verify that the links and buttons are enable and clickable')
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
