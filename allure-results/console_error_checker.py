import requests
from bs4 import BeautifulSoup

def get_sitemap_urls(sitemap_url):
    # Fetch the site map content
    response = requests.get(sitemap_url)
    print("I am inside the get_sitemap_urls")
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all URLs from the site map
    urls = []
    for loc in soup.find_all('loc'):
        urls.append(loc.text)

    return urls

def get_pages_with_console_errors(context, sitemap_url):
    # Get all URLs from the site map
    print("I am inside the get_pages_with_console_errors before")
    urls = get_sitemap_urls(sitemap_url)
    print("I am inside the get_pages_with_console_errors After")
    pages_with_errors = []

    try:
        for page in urls:
            context.driver.get(page)
            console_errors = check_console_errors(context.driver)

            if console_errors:
                pages_with_errors.append((page, console_errors))

    finally:
        # Do not close the browser here, as it will be closed in the after_all hook.
        print("This is finally block")

    return pages_with_errors

def check_console_errors(driver):
    # Get all the log entries from the browser's console
    print("I am inside the check_console_errors before")
    logs = driver.get_log('browser')
    print("I am inside the check_console_errors after")

    # Filter the log entries for errors
    console_errors = [log['message'] for log in logs if log['level'] == 'SEVERE']

    return console_errors
