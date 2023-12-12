import subprocess
import os
from datetime import datetime
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Run Behave tests with options")

# Add command-line arguments for tags and environment
parser.add_argument("--environment", default="", help="Specify the environment")

# Parse the command-line arguments
args = parser.parse_args()

if args.environment == "dev":
    # Define the command to run Behave with AllureFormatter
    behave_command = "behave -f allure_behave.formatter:AllureFormatter -o reports/ features/DevSiteTesting.feature"
elif args.environment == "live":
    # Define the command to run Behave with AllureFormatter
    behave_command = "behave -f allure_behave.formatter:AllureFormatter -o reports/ features/LiveSiteTesting.feature"
elif args.environment == "stg":
    # Define the command to run Behave with AllureFormatter
    behave_command = "behave -f allure_behave.formatter:AllureFormatter -o reports/ features/StageSiteTesting.feature"
elif args.environment == "console":
    # Define the command to run Behave with AllureFormatter
    behave_command = "behave -f allure_behave.formatter:AllureFormatter -o reports/ features/ConsoleErrors.feature"

# Execute the Behave command
subprocess.run(behave_command, shell=True)

# Get the current date and time
current_datetime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Define the command to serve the Allure report
allure_command = f"allure generate --clean reports/ -o reports/{current_datetime}/"

# Execute the Allure command
subprocess.run(allure_command, shell=True)

# Remove all .json files from the reports directory
for file in os.listdir('reports'):
    if file.endswith('.json') or file.endswith('.png') or file.endswith('.txt'):
        os.remove(os.path.joaddwebsolutionin('reports', file))