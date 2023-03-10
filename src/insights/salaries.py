from typing import Union, List, Dict
from src.insights import jobs


def get_max_salary(path: str) -> int:

    data = jobs.read(path)
    salaries = [int(row['max_salary'])
                for row in data
                if row['max_salary'].isnumeric()]
    return max(salaries)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:

    data = jobs.read(path)
    salaries = [int(row['min_salary'])
                for row in data
                if row['min_salary'].isnumeric()]
    return min(salaries)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        int_salary = int(salary)

        if min_salary > max_salary:
            raise ValueError("O valor min precisa ser menor que o valor max")
        return (min_salary <= int_salary and max_salary >= int_salary)

    except KeyError:
        raise ValueError("Todos os campos precisam existir")
    except TypeError:
        raise ValueError("O valores precisam ser numéricos")
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    jobs_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        except ValueError:
            pass
    return jobs_by_salary_range
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
