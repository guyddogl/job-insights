from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        data = csv.DictReader(file)
        return [datafile for datafile in data]


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    return {type["job_type"] for type in jobs}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
