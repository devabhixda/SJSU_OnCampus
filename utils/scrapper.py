from typing import Any

import requests
import json

from parsers.associated_students import parse_associated
from parsers.compass import parse_compass
from parsers.student_union import parse_union


def scrap_sources() -> list[list[dict[str, Any]]]:
    jobs = []
    with open('constants/sources.json', 'r') as file:
        sources = json.load(file)
        for source in sources:
            url = sources[source]
            response = requests.get(url)

            if source == 'associated_students':
                jobs.append(parse_associated(response.json()))
            elif source in ['compass', 'compass_pf']:
                jobs.append(parse_compass(response.content))
            elif source == 'student_union':
                jobs.append(parse_union(response.text))
            else:
                print("Source is not supported")
    return jobs
