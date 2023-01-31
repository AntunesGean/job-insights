from typing import List, Dict
from src.insights import jobs


def get_unique_industries(path: str) -> List[str]:

    data = jobs.read(path)
    industries = []
    for row in data:
        if row['industry'] not in industries and row['industry'] != "":
            industries.append(row['industry'])
    return industries
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    jobs_list = [job for job in jobs if job['industry'] == industry]
    return jobs_list
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
