import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dropbox
# from netlify.site import Site
import os
from behave import *
from pytest_bdd.reporting import *
from rocketchat_API.rocketchat import RocketChat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from behave.model_core import Status

# Global variables to store test results
Message = "This is for testing purpose."
TotalTests = 0
NumPassed = 0
NumFailed = 0
NumUndefined = 0
NumSkipped = 0

# Before Scenario Hook
def before_all(context):
    pass

# After Scenario Hook (Optional)
def after_all(context):
    # Adapt the RocketChat integration code here
    global TotalTests, NumPassed, NumFailed, NumUndefined, NumSkipped, Message
    Message = "Test summary \n"
    Message += f"Total Scenarios: {TotalTests} \n"
    Message += f"Passed: {NumPassed} \n"
    Message += f"Failed: {NumFailed} \n"
    Message += f"Errors: {NumUndefined} \n"
    Message += f"Skipped: {NumSkipped} \n"
    # Call the function to upload the zip file to Dropbox and get the URL path
    # share_link  = upload_zip_to_dropbox()

    # Message += f"Test Report: {share_link} \n"
    # Send_To_Channel(Message)
    send_email(Message)


# Before Scenario Hook (Optional)
def before_scenario(context, scenario):
    service = Service('/home/addweb/PycharmProjects/FirstScript/Drivers/chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1280,1024")
    # Set logging preferences
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--pageLoadStrategy=normal")
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set the log level (you can adjust it to your needs)
    logging.basicConfig(level=logging.INFO)

    # You can customize the log format
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

    # You can also add a log file handler to write logs to a file
    logging.basicConfig(filename='test.log', filemode='w', level=logging.INFO)

# After Scenario Hook (Optional)
def after_scenario(context, scenario):
    # Close the browser after each scenario
    global TotalTests, NumPassed, NumFailed, NumUndefined, NumSkipped

    TotalTests += 1

    if scenario.status == Status.failed:
        NumFailed += 1

    elif scenario.status == Status.passed:
        NumPassed += 1

    elif scenario.status == Status.undefined:
        NumUndefined += 1

    elif scenario.status == Status.skipped:
        NumSkipped += 1

    context.driver.quit()

# Before Step Hook
def before_step(context, step):
    pass

# After Step Hook
def after_step(context, step):
    pass

def Send_To_Channel(Message):
    # Set the channel or user to whom you want to send the zip file
    TeamRoom = 'wp-voltactivedata'
    rocket = RocketChat('uvesh@addwebsolution.in', 'Uvesh@890', server_url='https://chat.addwebsolution.in/')
    # rocket.chat_post_message(room_id=TeamRoom, text=Message)

def send_email(Message):
    # Example usage of the send_email function:
    sender = "uvesh@addwebsolution.in"
    password = "vqjk prgb ioyn kdsx"
    receiver = "riddhi@addwebsolution.in"
    subject = "Test Email with Attachment"
    body = Message
    attachment_path = "reports/19-09-2023_12-25-13/index.html"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    attachment_path = attachment_path

    # Attach the zip file
    attachment = open(attachment_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
    msg.attach(part)

    # with open(attachment_path, "rb") as report_file:
    #     html_content = report_file.read()
    #     print(html_content)  # Print the HTML content to check if it's correct before sending

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

# def upload_zip_to_dropbox():
#
#     # Specify the local zip file path, Dropbox folder name, and access token
#     zip_filename = "reports/18-09-2023_13-56-56.zip"
#     dropbox_folder_name = "Test Reports"
#     dropbox_access_token = "sl.BmRoSfNs5XA7-sfb95lc7w3dJGJR9j4kXamMTEoLRDBrhZZNbkQLqH-JNm3wL8N0YQLfqzBJWDfFpyeWFHz3zi59kOPtZu6qzg482eyX3NkSQm4O6j0biIGBwVWukd47MaauI7Yw2LZ9k9Q4cUacMi8"
#
#     dbx = dropbox.Dropbox(dropbox_access_token)
#
#     # Specify the Dropbox path where you want to upload the zip file
#     dropbox_file_path = f"/{dropbox_folder_name}/{os.path.basename(zip_filename)}"
#     # {os.path.basename(zip_filename)}
#
#     # Upload the zip file to Dropbox
#     with open(zip_filename, "rb") as f:
#         try:
#             dbx.files_upload(f.read(), dropbox_file_path)
#             # mode = dropbox.files.WriteMode("overwrite")
#             print(f"Uploaded: {os.path.basename(zip_filename)} to Dropbox")
#
#             # Get the sharing link for the uploaded file
#             sharing_link = dbx.sharing_create_shared_link(dropbox_file_path)
#             url_path = sharing_link.url
#             print(f"File URL: {url_path}")
#         except Exception as e:
#             print(f"Error uploading {os.path.basename(zip_filename)} to Dropbox: {e}")
#
#     print("Zip file uploaded to Dropbox successfully.")
#     return sharing_link


# def upload_zip_to_netlify():
#     # Replace with your Netlify access token and site ID
#     access_token = "your_access_token"
#     site_id = "your_site_id"
#     folder_path = "path_to_report_folder"
#
#     # Initialize a Netlify site
#     site = Site(access_token=access_token, site_id=site_id)
#
#     # Upload the folder to Netlify
#     site.upload_directory(folder_path)
#
#     print(f"Folder '{folder_path}' uploaded to Netlify.")


