import requests
from bs4 import BeautifulSoup
import os
import sys
import json

save_dir = sys.argv[1] if len(sys.argv) > 1 else "images"
element = sys.argv[2] if len(sys.argv) > 2 else None

# lisäys, kaikkien titlejen ja testien elementin palautus myös.

def web_scraper(element):
    url = "http://localhost/robot"
    response = requests.get(url)
    formatted = []
    if response.status_code == 200:
        elements = get_element(response, element, url)
        if element == "images":
            return
        for item in elements:
            if isinstance(item, str):
                formatted.append(item.strip())
            else:
                formatted.append(item.text.strip())
        return formatted
    else:
        print(f"failed to retrieve the webpage statuscode: {response.status_code}")

def get_element(response, element, url):
    soup =  BeautifulSoup(response.text, "html.parser")
    if element == "titles":
        titles = []
        for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            titles.extend(soup.find_all(tag))
        return titles
    elif element == "links":
        return [link.get("href") for link in soup.find_all("a") if link.get("href")]  
    elif element == "texts":
        texts = []
        for tag in ["p", "span"]:
            texts.extend(soup.find_all(tag))
        return texts
    elif element == "images":
        get_images(soup, url)
        return 
    elif element == "lists":
        lists = []
        for tag in ["ol", "ul"]:
            for list_tag in soup.find_all(tag):
                items = [li.text.strip() for li in list_tag.find_all("li")]
                lists.extend(items)
        return lists
    else:
        return []
    
def get_images(soup, url, save_dir=save_dir):
    """
    Scrape images
    :param soup: bs4
    :param url: website url
    :param save_dir: directory where to save, default "images" folder
    """

    os.makedirs(save_dir, exist_ok=True)
    images = soup.find_all("img")
    

    for img in images:
        img_url = img.get("src")

        if img_url and not img_url.startswith("http"):
            img_url = url + "/" + img_url

        if img_url:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_name = os.path.join(save_dir, img_url.split("/")[-1])

                with open(img_name, "wb") as f:
                    f.write(img_response.content)

if element:
    formatted = web_scraper(element)
    if formatted:
        print(json.dumps(formatted))
else:
    print(json.dumps({"error": "No element specified. Pass a avalid element argument"}))