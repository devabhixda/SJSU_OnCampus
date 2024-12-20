from typing import Any

from constants.const import associated_base_url


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