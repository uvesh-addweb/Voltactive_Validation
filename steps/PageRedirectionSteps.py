# features/steps/home_steps.py
import base64
import urllib
from selenium.webdriver.common.action_chains import ActionChains
import allure
# from pyextent import ExtentTest, ExtentReports
from urllib.parse import urlparse
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mappings import xpath_mapping, url_mapping
assertion_failed = False

@given('The user is on the "{url}" site')
def step_impl(context, url):
    try:
        # Your password
        password = 'oI5L!YKmQ@1gOvqQ@M7w'
        url = xpath_mapping[url]
        # Encode the password
        encoded_password = base64.b64encode(password.encode()).decode()
        context.driver.get(url)

        # Add your code to navigate to the Home page
        # context.driver.get("https://voltDEV:ww9E1ShSNAGLD@M7w@dev.voltactivedata.com")
        # context.driver.get("https://voltSTG:oI5L!YKmQ@1gOvqQ@M7w@stg.voltactivedata.com")
        # context.driver.get("https://www.voltactivedata.com")

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        raise


@when('The user hovers over the "{menu_name}" menu')
def step_impl(context, menu_name):
    try:
        # Hover over the menu element
        xpath = xpath_mapping[menu_name]
        menu_element = context.driver.find_element(By.XPATH, xpath)
        assert menu_element.is_enabled() and menu_element.is_displayed(), "Menu is not enabled and visible"
        hover = ActionChains(context.driver).move_to_element(menu_element)
        hover.perform()

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
            attachment_type=allure.attachment_type.PNG)
        raise


@when('The user clicks on the "{submenu_link}" submenu link and verify the redirection "{page}" page')
def step_impl(context, submenu_link, page):
    try:
        # Click on the submenu link
        xpath = xpath_mapping[submenu_link]
        pre_url = context.driver.current_url
        submenu_element = context.driver.find_element(By.XPATH, xpath)
        submenu_element.click()

        attempt = 0

        while (context.driver.current_url != pre_url):
            context.driver.implicitly_wait(5)
            attempt = attempt + 1
            if attempt > 6:
                break

        # Add your code to verify the redirection to the expected page
        expected_url = url_mapping[page]
        expected_url_slug = expected_url.split("/")[-1]
        current_url = context.driver.current_url
        current_url_slug = current_url.split("/")[-1]
        assert current_url_slug == expected_url_slug, f"Expected URL: {expected_url_slug}, Actual URL: {current_url_slug}"
        # assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
            attachment_type=allure.attachment_type.PNG)
        raise


@when('The user clicks on the "{element}" button')
def step_impl(context, element):
    try:
        wait = WebDriverWait(context.driver, 5)
        # Add your code to click on the specified button
        xpath = xpath_mapping[element]
        pre_url = context.driver.current_url
        button_element = context.driver.find_element(By.XPATH, xpath)
        actions = ActionChains(context.driver)
        # actions.move_to_element(button_element).perform()
        button_element.send_keys(Keys.ARROW_DOWN)
        button_element.send_keys(Keys.ARROW_DOWN)
        button_element.send_keys(Keys.ARROW_DOWN)
        assert button_element.is_enabled() and button_element.is_displayed(), "Button is not enabled and visible"
        button_element.click()
        time.sleep(2)

        attempt = 0

        while(context.driver.current_url != pre_url):
            context.driver.implicitly_wait(5)
            attempt = attempt + 1
            if attempt > 6:
                break

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        raise


@when('The user clicks on the "{element}" button verify the page redirection')
def step_impl(context, element):
    try:
        # Add your code to click on the specified button
        xpath = xpath_mapping[element]
        pre_url = context.driver.current_url
        button_element = context.driver.find_element(By.XPATH, xpath)
        assert button_element.is_enabled() and button_element.is_displayed(), "Button is not enabled and visible"
        expected_url = button_element.get_attribute('href')
        button_element.send_keys(Keys.ARROW_DOWN)
        button_element.send_keys(Keys.ARROW_DOWN)
        button_element.send_keys(Keys.ARROW_DOWN)
        button_element.click()
        time.sleep(2)

        attempt = 0

        while (context.driver.current_url != pre_url):
            context.driver.implicitly_wait(5)
            attempt = attempt + 1
            if attempt > 6:
                break

        if len(context.driver.window_handles) > 1:
            window_handles = context.driver.window_handles
            expected_url_slug = expected_url.split("/")[-1]
            time.sleep(3)
            context.driver.switch_to.window(window_handles[-1])
            current_url = context.driver.current_url
            current_url_slug = current_url.split("/")[-1]
            assert current_url_slug == expected_url_slug, f"Expected URL: {expected_url_slug}, Actual URL: {current_url_slug}"
            # assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

            context.driver.close()
            time.sleep(3)
            context.driver.switch_to.window(window_handles[-2])

        else:
            # Add your code to verify the redirection to the expected page
            expected_url_slug = expected_url.split("/")[-1]
            current_url = context.driver.current_url
            current_url_slug = current_url.split("/")[-1]
            assert current_url_slug == expected_url_slug, f"Expected URL: {expected_url_slug}, Actual URL: {current_url_slug}"
            # assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"
            context.driver.back()

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        raise


@then('The user should be redirected to the "{page}" page')
def step_impl(context, page):
    global assertion_failed

    try:
        expected_url = url_mapping[page]
        if len(context.driver.window_handles) > 1:
            window_handles = context.driver.window_handles
            expected_url_slug = expected_url.split("/")[-1]
            time.sleep(3)
            context.driver.switch_to.window(window_handles[-1])
            current_url = context.driver.current_url
            current_url_slug = current_url.split("/")[-1]
            assert current_url_slug == expected_url_slug, f"Expected URL: {expected_url_slug}, Actual URL: {current_url_slug}"
            # assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

            context.driver.close()
            time.sleep(3)
            context.driver.switch_to.window(window_handles[-2])

        else:
            # Add your code to verify the redirection to the expected page
            expected_url_slug = expected_url.split("/")[-1]
            current_url = context.driver.current_url
            current_url_slug = current_url.split("/")[-1]
            assert current_url_slug == expected_url_slug, f"Expected URL: {expected_url_slug}, Actual URL: {current_url_slug}"
            # assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"
            context.driver.back()
            time.sleep(2)

    except AssertionError as e:
        assertion_failed = True
        error_message = f"Assertion error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True
        raise


@when('The user selects "{option}" from the "{dropdown}" dropdown in "{Type_UL}"')
def step_impl(context, option, dropdown, Type_UL):
    dropdown_xpath = xpath_mapping[dropdown]

    type_dropdown_btn = context.driver.find_element(By.XPATH, dropdown_xpath)
    type_dropdown_btn.send_keys(Keys.ARROW_DOWN)
    type_dropdown_btn.click()
    type_ul = xpath_mapping[Type_UL]
    type_dropdown_ul = context.driver.find_element(By.XPATH, type_ul)
    type_dropdown_li = type_dropdown_ul.find_elements(By.TAG_NAME, "li")

    for li in type_dropdown_li:
        li_txt = li.text
        if li_txt == option:
            li.click()

    time.sleep(5)


@then('The "{resource_list_element}" should be filtered by "{filter_value}" type')
def step_impl(context,resource_list_element, filter_value):
    # filter_value = "Wrong value"
    try:
        # Assuming that the filtered results are displayed in a list
        resource_list_xpath = xpath_mapping[resource_list_element]
        resource_list = context.driver.find_element(By.XPATH, resource_list_xpath)
        resource_type = resource_list.find_elements(By.CLASS_NAME, 'type')
        resource_title = resource_list.find_elements(By.CLASS_NAME, 'title')

        for type, title in zip(resource_type, resource_title):
            # Implement logic to verify that each resource matches the expected filter
            type_txt = type.text

            if type_txt == "":
                continue

            assert type_txt == filter_value

    except AssertionError as e:
        error_message = f'Expected type of Resource : "{filter_value}" Actual Type of Resource : "{type_txt}" on the "{title.text}" Resource'
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True
        raise

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True


@when('The user Click on "{fraud_prevention_category}" Category from the Category section')
def step_impl(context, fraud_prevention_category):
    try:
        fraud_prevention_category = xpath_mapping[fraud_prevention_category]
        category = context.driver.find_element(By.XPATH, fraud_prevention_category)
        category.click()

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True


@then('The Page title should be filtered by "{category_name}" type on "{category_tag}"')
def step_impl(context, category_name, category_tag):
    # category_name = "Wrong value"
    try:
        category_name = xpath_mapping[category_name]
        # category_name = "Wrong value"
        category_tag = xpath_mapping[category_tag]
        category_tag_text = context.driver.find_element(By.XPATH, category_tag).text

        assert category_tag_text == category_name

    except AssertionError as e:
        error_message = f'Expected Category for Blog : "{category_name}" Actual Category for Blog : "{category_tag_text}" on Blog page'
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True
        raise

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True


@when(u'The user enters the resource title "{Resource_Title}" in the "{search_bar}"')
def step_impl(context, Resource_Title, search_bar):
    try:
        Resource_Title = xpath_mapping[Resource_Title]
        search_bar = xpath_mapping[search_bar]
        search_bar = context.driver.find_element(By.XPATH, search_bar)
        search_bar.send_keys(Resource_Title)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True

@then(u'The "{resource_list_element}" should be filtered by "{Resource_Title}" resource')
def step_impl(context, resource_list_element, Resource_Title):
    try:
        # Assuming that the filtered results are displayed in a list
        resource_list_xpath = xpath_mapping[resource_list_element]
        Resource_Title = xpath_mapping[Resource_Title]
        # Resource_Title = "Wrong Value"
        resource_list = context.driver.find_element(By.XPATH, resource_list_xpath)
        resource_type = resource_list.find_elements(By.CLASS_NAME, 'type')
        resource_title = resource_list.find_elements(By.CLASS_NAME, 'title')

        for type, title in zip(resource_type, resource_title):
            # Implement logic to verify that each resource matches the expected filter
            title_txt = title.text

            if title_txt == "":
                continue

            assert title_txt == Resource_Title

    except AssertionError as e:
        error_message = f'Expected type of Resource : "{Resource_Title}" Actual Type of Resource : "{type.text}" on the "{title.text}" Resource'
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True
        raise

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {context.driver.current_url} Page",
                      attachment_type=allure.attachment_type.PNG)
        context.step_failed = True


@then('Check for the console error on the page')
def report_console_errors(context):
    console_errors = []
    time.sleep(5)
    logs = context.driver.get_log('browser')
    console_errors = [log['message'] for log in logs if log['level'] == 'SEVERE']
    print("Console Error : ", logs)
    # if logs != []:
    #     page_slug = urlparse(url).path.split('/')[-1]
    #     allure.attach(f"Page : {url} \n \nConsole Error : {logs}", f"Error on {url} Page", allure.attachment_type.TEXT)
    #     allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {url} Page",
    #                   attachment_type=allure.attachment_type.PNG)
    # If there are console errors, fail the step
    if console_errors != []:
        # Get the current page URL
        url = context.driver.current_url

        # Attach the URL, console error messages, and a screenshot to the Allure report
        allure.attach(f"Page: {url}\n\nConsole Error: {console_errors}", f"Error on {url} Page",
                      allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name=f"Screenshot of {url} Page",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        # Fail the step
        assert False, f"Console errors found on the page: {url}"

    return console_errors
