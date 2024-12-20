from typing import Any

import requests
import json
from parser import parse_associated, parse_compass

def scrap_sources() -> list[list[dict[str, Any]]]:
    jobs = []
    with open('sources.json', 'r') as file:
        sources = json.load(file)
        for source in sources:
            url = sources[source]
            response = requests.get(url)

            if source == 'associated_students':
                jobs.append(parse_associated(response.json()))
            elif source in ['compass', 'compass_pf']:
                jobs.append(parse_compass(response.content))
            else:
                print("Source is not supported")
    return jobs
