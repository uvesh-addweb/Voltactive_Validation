from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'The browser is launched')
def launchedBrowser(context):
    print("The Browser is launched")

@when(u'Open Voltactive homepage')
def openHomepage(context):
    try:
        context.driver.get("https://voltDEV:ww9E1ShSNAGLD@M7w@dev.voltactivedata.com/")

    except Exception as e:
        print(f"An error occurred: {e}")

@then(u'Verify that the logo present on the page')
def verifyLogo(context):
    try:
        wait = WebDriverWait(context.driver, 30)  # Set an appropriate timeout value
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'header-branding')))
        logo_element = context.driver.find_element(By.CLASS_NAME, 'header-branding')
        status = logo_element.is_displayed() and logo_element.is_enabled()
        assert status is True

    except Exception as e:
        print(f"An error occurred: {e}")