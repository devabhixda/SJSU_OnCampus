from typing import Any

from bs4 import BeautifulSoup

from constants.const import compass_base_url
from utils.utils import date_convert_str


def parse_compass(content: bytes) -> list[dict[str, Any]]:
    soup = BeautifulSoup(content, 'html.parser')
    data = soup.find('ul', id='job-tile-list')
    job_listings = []

    if data:
        for job in data.find_all('li', class_='job-tile'):
            title = job.find('span', class_='title').text.strip()
            date = job.find('div', id=lambda x: x and x.endswith('-section-date-value')).text.strip()
            link = job.find('a', class_='jobTitle-link')['href']

            job_listings.append({
                'title': title,
                'date': date_convert_str(date),
                'id': link.split('/')[-2],
                'link': compass_base_url + link
            })

    return job_listings