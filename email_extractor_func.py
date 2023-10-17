import requests 
from bs4 import BeautifulSoup 

from urllib.parse import urlparse


import re 

def send_reqeusts(link):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

    response = requests.get(link, headers = headers)


    

    soup = BeautifulSoup(response.text, "html.parser")

    return soup

def get_all_links(soup, init_link):
    links = []
    facebook = None
   

    # Find all 'a' (anchor) tags in the HTML
    links = soup.find_all('a')

    # Extract and print the links
    for link in links:
        try:
            href = link.get('href')
            if href != None:
            
                    if href.startswith('https://') :
                        if "facebook" in href:
                            facebook = href
                            continue
                    
                        links.append(href)
                
                    elif href.startswith('/'):
                     
                        links.append(init_link + href)
                    
                    else: 

                      
                        links.append(init_link +"/" +href)
        except: continue
     
            

    return links, facebook

def find_emails(text_info):
 
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text_info)

    return match

def get_domain(link):
    # Parse the URL
    parsed_url = urlparse(link)

    # Extract and print the domain
    domain = parsed_url.netloc
 

    return domain

def most_common(lst):
    return max(set(lst), key=lst.count)


def extract_emails(site_url):
    print("Extraction has started")

    all_emails = []
    company_domain = get_domain('site_url')
    urls_dslashed  = site_url.rstrip("/")


    soup = send_reqeusts(site_url)


    all_links, facebook = get_all_links(soup, urls_dslashed)
    
    for link in all_links:
        
        if company_domain in link:
            try:
                page_soup = send_reqeusts(link)
            except:
                continue

            emails = find_emails(page_soup.text)

            if len(emails) > 0 :
                for email in emails:
                    
                    all_emails.append(email)

    try:
        most_common_email = most_common(all_emails)
    except: 
        most_common_email = None

    print('The email is: ', most_common_email, 
          "\nfacebook is: ", facebook)
    
    return most_common_email , facebook


   






