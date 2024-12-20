from typing import Any

from bs4 import BeautifulSoup
import re

from constants.const import union_base_url
from utils.utils import date_convert_dmy


def parse_union(data) -> list[dict[str, Any]]:
    document_write_pattern = re.compile(r"document\.write\('(.*?)'\);", re.DOTALL)
    matches  = document_write_pattern.findall(data)
    job_listings = []
    if matches :
        for i, match in enumerate(matches, 1):
            cleaned_content = match.replace("\\'", "'").replace("\\n", "\n")
            soup = BeautifulSoup(cleaned_content, 'html.parser')
            heading = soup.find('table', class_='title').text
            title, job_id = heading.split(' JobID: ')
            date_posted = ""
            for li in soup.find_all('li'):
                label_span = li.find('span', class_='label')
                if label_span:
                    label = label_span.get_text(strip=True)
                    value = li.get_text(strip=True).replace(label, "").strip()
                    if label == 'Date Posted:':
                        date_posted = value
                        break
            job_listings.append({
                'title': title,
                'date': date_convert_dmy(date_posted),
                'id': job_id,
                'link': union_base_url + job_id
            })
    else:
        print("No document.write content found")
    return job_listings