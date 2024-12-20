from scrapper import scrap_sources


def get_jobs():
    jobs = scrap_sources()
    print(jobs)

if __name__ == "__main__":
    get_jobs()