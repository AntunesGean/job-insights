from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path) as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        jobs_list1 = []
        for jobs in jobs_list:
            jobs_list1.append(jobs)
        return jobs_list1
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:

    data = read(path)
    unic_job_type = []
    for row in data:
        if row['job_type'] not in unic_job_type:
            unic_job_type.append(row['job_type'])
    return unic_job_type
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    jobs_list = [job for job in jobs if job['job_type'] == job_type]
    return jobs_list
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
