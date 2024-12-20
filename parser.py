import re
from typing import Any

from bs4 import BeautifulSoup

from const import associated_base_url, compass_base_url
from utils import date_convert_str


def parse_associated(data) -> list[dict[str, Any]]:
    job_listings = []
    for job in data['jobRequisitions']:
        if job['workLevelCode']['shortName'] == 'Student':
            title = job['requisitionTitle']
            post_date = job['postDate']
            external_job_id = None
            for field in job['customFieldGroup']['stringFields']:
                if field['nameCode']['codeValue'] == 'ExternalJobID':
                    external_job_id = field['stringValue']
            job_listings.append({
                'title': title,
                'date': post_date,
                'id': external_job_id,
                'link': associated_base_url + external_job_id
            })

    return job_listings

def parse_compass(content: bytes) -> list[dict[str, Any]]:
    soup = BeautifulSoup(content, 'html.parser')
    data = soup.find('ul', id='job-tile-list')
    job_listings = []

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
