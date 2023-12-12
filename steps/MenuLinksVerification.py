from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import logging

# @given(u'The user is on home page')
# def homePage(context):
#     print("The user is on home page")
#
# @when(u'Get the menu Links')
# def menuLinks(context):
#     try:
#         wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         why_volt = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1584"]/a')
#         hover = ActionChains(context.driver).move_to_element(why_volt)
#         hover.perform()
#
#         context.no_compromises = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22563"]/a')))
#         context.volt_for_5g = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-20627"]/a')))
#         context.capabilities = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22591"]/a')))
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         use_cases = context.driver.find_element(By.XPATH, '//*[@id="menu-item-22593"]/a')
#         hover = ActionChains(context.driver).move_to_element(use_cases)
#         hover.perform()
#
#         context.geo_replication = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22590"]/a')))
#         context.high_availability = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-20968"]/a')))
#         context.monetizing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22587"]/a')))
#         context.oem_friendly = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22667"]/a')))
#         context.real_time = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22667"]/a')))
#         context.cloud = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-21024"]/a')))
#         context.edge = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-20886"]/a')))
#         context.kafka = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-23050"]/a')))
#         context.billing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-19423"]/a')))
#         context.bss = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-18233"]/a')))
#         context.data_platform = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-22963"]/a')))
#         context.fraud_prevention = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-18231"]/a')))
#         context.hyper_personalization = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-18232"]/a')))
#         context.iot = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-19289"]/a')))
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         resources = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1582"]/a')
#         hover = ActionChains(context.driver).move_to_element(resources)
#         hover.perform()
#
#         context.resource_library = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-18012"]/a')))
#         context.blog = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-16565"]/a')))
#         context.partner_program = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-18013"]/a')))
#         context.webinar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-20696"]/a')))
#         context.support = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-16856"]/a')))
#         context.professional_services = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-20650"]/a')))
#         context.documentation = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-17375"]/a')))
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         company = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1578"]/a')
#         hover = ActionChains(context.driver).move_to_element(company)
#         hover.perform()
#
#         context.about = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-18011"]/a')))
#         context.carrers = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-17396"]/a')))
#         context.news = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-16545"]/a')))
#         context.press_release = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-16549"]/a')))
#         context.team = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-1585"]/a')))
#         context.contact = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-17103"]/a')))
#
#         context.try_volt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-1583"]/a')))
#
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# @then(u'Verify that the links are enable and clickable')
# def verifyLniks(context):
#     try:
#         def verify_element(element):
#             return element.is_enabled() and element.is_displayed()
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         why_volt = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1584"]/a')
#         hover = ActionChains(context.driver).move_to_element(why_volt)
#         hover.perform()
#
#         assert verify_element(context.no_compromises) is True
#         assert verify_element(context.volt_for_5g) is True
#         assert verify_element(context.capabilities) is True
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         use_cases = context.driver.find_element(By.XPATH, '//*[@id="menu-item-22593"]/a')
#         hover = ActionChains(context.driver).move_to_element(use_cases)
#         hover.perform()
#
#         assert verify_element(context.geo_replication) is True
#         assert verify_element(context.high_availability) is True
#         assert verify_element(context.monetizing) is True
#         assert verify_element(context.oem_friendly) is True
#         assert verify_element(context.real_time) is True
#         assert verify_element(context.cloud) is True
#         assert verify_element(context.edge) is True
#         assert verify_element(context.kafka) is True
#         assert verify_element(context.billing) is True
#         assert verify_element(context.bss) is True
#         assert verify_element(context.data_platform) is True
#         assert verify_element(context.fraud_prevention) is True
#         assert verify_element(context.hyper_personalization) is True
#         assert verify_element(context.iot) is True
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         resources = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1582"]/a')
#         hover = ActionChains(context.driver).move_to_element(resources)
#         hover.perform()
#
#         assert verify_element(context.resource_library) is True
#         assert verify_element(context.blog) is True
#         assert verify_element(context.partner_program) is True
#         assert verify_element(context.webinar) is True
#         assert verify_element(context.support) is True
#         assert verify_element(context.professional_services) is True
#         assert verify_element(context.documentation) is True
#
#         # Hover the mouse on the main link to trigger sub-links appearance
#         company = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1578"]/a')
#         hover = ActionChains(context.driver).move_to_element(company)
#         hover.perform()
#
#         assert verify_element(context.about) is True
#         assert verify_element(context.carrers) is True
#         assert verify_element(context.news) is True
#         assert verify_element(context.press_release) is True
#         assert verify_element(context.team) is True
#         assert verify_element(context.contact) is True
#
#         assert verify_element(context.try_volt) is True
#
#     except Exception as e:
#         print(f"An error occurred: {e}")

@given(u'The user is on home page')
def step_impl(context):
    print("The User is on Home Page.")


@when(u'Get the menu Links')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed

        # Hover the mouse on the main link to trigger sub-links appearance
        context.why_volt_a = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1584"]/a')
        hover = ActionChains(context.driver).move_to_element(context.why_volt_a)
        hover.perform()

        context.why_volt_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1584"]/ul')
        context.why_volt_ul_a = context.why_volt_ul.find_elements(By.TAG_NAME, 'a')

        # Hover the mouse on the main link to trigger sub-links appearance
        context.use_cases_a = context.driver.find_element(By.XPATH, '//*[@id="menu-item-22593"]/a')
        hover = ActionChains(context.driver).move_to_element(context.use_cases_a)
        hover.perform()

        context.technical_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1580"]/ul')
        context.technical_ul_a = context.technical_ul.find_elements(By.TAG_NAME, 'a')

        context.environment_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-22573"]/ul')
        context.environment_ul_a = context.environment_ul.find_elements(By.TAG_NAME, 'a')

        context.industry_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-22574"]/ul')
        context.industry_ul_a = context.industry_ul.find_elements(By.TAG_NAME, 'a')

        # Hover the mouse on the main link to trigger sub-links appearance
        context.resources_a = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1582"]/a')
        hover = ActionChains(context.driver).move_to_element(context.resources_a)
        hover.perform()

        context.resources_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1582"]/ul')
        context.resources_ul_a = context.resources_ul.find_elements(By.TAG_NAME, 'a')

        context.customer_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-22594"]/ul')
        context.customer_ul_a = context.resources_ul.find_elements(By.TAG_NAME, 'a')

        # Hover the mouse on the main link to trigger sub-links appearance
        context.company_a = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1578"]/a')
        hover = ActionChains(context.driver).move_to_element(context.company_a)
        hover.perform()

        context.company_ul = context.driver.find_element(By.XPATH, '//*[@id="menu-item-1582"]/ul')
        context.company_ul_a = context.resources_ul.find_elements(By.TAG_NAME, 'a')


    except Exception as e:
        print(f"An error occurred: {e}")

@then(u'Verify that the links are enable and clickable')
def step_impl(context):
    try:
        def verify_redirection(context, a_tag):
            a_href_link = a_tag.get_attribute('href')
            a_tag.click()
            context.driver.implicitly_wait(3)
            current_url = context.driver.current_url
            if current_url == a_href_link:
                print(f"Redirection is proper. Current URL: {current_url}, Expected URL: {a_href_link}")
                logging.info(f"Redirection is proper. Current URL: {current_url}, Expected URL: {a_href_link}")
                # context.driver.back()
                context.driver.implicitly_wait(3)
                return True
            else:
                print(f"Redirection is NOT proper. Current URL: {current_url}, Expected URL: {a_href_link}")
                # context.driver.back()
                context.driver.implicitly_wait(3)
                return False

        def verify_element(element):
            return element.is_enabled() and element.is_displayed()

        for a_tag in context.why_volt_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.why_volt_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True

        for a_tag in context.technical_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.use_cases_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True

        for a_tag in context.environment_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.use_cases_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True

        for a_tag in context.industry_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.use_cases_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True

        for a_tag in context.resources_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.resources_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True

        for a_tag in context.customer_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.resources_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True

        for a_tag in context.company_ul_a:
            hover = ActionChains(context.driver).move_to_element(context.company_a)
            hover.perform()
            assert verify_element(a_tag) is True
            assert verify_redirection(context, a_tag) is True


    except Exception as e:
        print(f"An error occurred: {e}")