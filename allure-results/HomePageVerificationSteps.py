from pytest_bdd import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'The user is on the home page')
def homePageVerification(context):
    print("The User is on Home Page.")


@when(u'Get the Buttons and links from the page')
def getButtonsAndLinks(context):
    wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed

    context.get_started = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[1]/div/div/div/div/div/div/div/div[4]/a')))
    context.partners = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[1]/div/div/div/div/div/div/div/div[5]/a')))
    context.learn_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[5]/div/div/div/div[4]/div/div/div/div[3]/a')))
    context.business = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[3]/div[1]/div/div/div[3]/a')))
    context.zero_lag = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[3]/div[2]/div/div/div[3]/a')))
    context.monetized = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[3]/div[3]/div/div/div[3]/a')))
    context.cloud = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[1]/div/div/div[3]/a')))
    context.high_availability = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[2]/div/div/div[3]/a')))
    context.xdcr = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[3]/div/div/div[3]/a')))
    context.edge = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[9]/div/div/div/div[5]/div[4]/div/div/div[3]/a')))
    context.capabilities = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-18176"]/div/section/div[10]/div/div/div/div[3]/a')))
    context.learn_more_footer = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text-4"]/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/a')))


@then(u'Verify that the links and buttons are enable and clickable')
def verifyButtonsAndLinks(context):
    def verify_element(element):
        return element.is_enabled() and element.is_displayed()

    def verify_redirection(element):
        element.click()
        context.driver.implicitly_wait(3)
        current_url = context.driver.current_url
        anchor_url = element.get_attribute("href")
        if current_url == anchor_url:
            print(" '" +anchor_url+ "' Page Redirection is proper.")
            context.driver.back()
            context.driver.implicitly_wait(3)
            return True

    # Verify the Button and links
    assert verify_element(context.get_started) is True
    assert verify_element(context.partners) is True
    assert verify_element(context.learn_more) is True

    assert verify_element(context.business) is True
    assert verify_element(context.zero_lag) is True
    assert verify_element(context.monetized) is True

    assert verify_element(context.cloud) is True
    assert verify_element(context.high_availability) is True
    assert verify_element(context.xdcr) is True

    assert verify_element(context.edge) is True
    assert verify_element(context.capabilities) is True
    assert verify_element(context.learn_more_footer) is True

    # Verify the redirection of the Links and Button
    assert verify_redirection(context.get_started) is True
    assert verify_redirection(context.partners) is True
    assert verify_redirection(context.learn_more) is True

    assert verify_redirection(context.business) is True
    assert verify_redirection(context.zero_lag) is True
    assert verify_redirection(context.monetized) is True

    assert verify_redirection(context.cloud) is True
    assert verify_redirection(context.high_availability) is True
    assert verify_redirection(context.xdcr) is True

    assert verify_redirection(context.edge) is True
    assert verify_redirection(context.capabilities) is True
    assert verify_redirection(context.learn_more_footer) is True


# @given(u'The user is at home page')
# def step_impl(context):
#     print("sdfdsfdsf")
#
# @when(u'Get the Buttons and links on the page')
# def step_impl(context):
#     print("sdfdsfdsf")
#
# @then(u'Verify that the links and buttons are enable and clickable')
# def step_impl(context):
#     print("sdfdsfdsf")
#
#     @given(u'The user is at home page')
#     def step_impl(context):
#         raise NotImplementedError(u'STEP: Given The user is at home page')
#
#     @when(u'Get the Buttons and links on the page')
#     def step_impl(context):
#         raise NotImplementedError('When Get the Buttons and links on the page')
#
#     @then(u'Verify that the links and buttons are enable and clickable')
#     def step_impl(context):
#         raise NotImplementedError(u'STEP: Then Verify that the links and buttons are enable and clickable')
#
