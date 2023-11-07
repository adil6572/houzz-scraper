import requests
from bs4 import BeautifulSoup
import re

def is_valid_email(email):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(email_pattern, email)

def extract_emails(soup):
    email_addresses = set()
    for tag in soup.find_all(['a', 'p', 'span', 'div']):
        text = tag.get_text()
        for email in re.findall(r'\S+@\S+', text):
            if is_valid_email(email):
                email_addresses.add(email)
    return list(email_addresses)

def extract_emails_from_url(url):
    try:
        response = requests.get(f"https://{url}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            email_addresses = extract_emails(soup)

            if email_addresses:
                return email_addresses
            else:
                return '' 
        else:
            return ''  
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None 

