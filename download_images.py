"""Python script to download all the images in a page."""

#Python
import re
import sys
import os
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve

#Third party
from bs4 import BeautifulSoup


def main(url):
    html = check_permission(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images:
        image = image['src']
        image_name = image.split('/')[-1]
        download_image(image, image_name)
        

def download_image(image, image_name):
    """Downloads an image"""
    try:
        urlretrieve(image, 'images/{}'.format(image_name))
        print('Downloading: {}'.format(image_name))
    except Exception as e:
        print(str(e))
        print('Can\'t download {}'.format(image_name))

def check_permission(url):
    """Check is the page allows scrapers"""
    try:
        return urlopen(url)
    except HTTPError:
        print('Permission denied')


if __name__ == "__main__":
    url = sys.argv[1]
    import os
    if not os.path.exists('images'):
        os.makedirs('images')
    main(url)