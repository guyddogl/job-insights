from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(salary["max_salary"])
        for salary in jobs
        if salary["max_salary"].isnumeric()
    ]
    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(salary["min_salary"])
        for salary in jobs
        if salary["min_salary"].isnumeric()
    ]
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if (
            not str(job["max_salary"]).isnumeric()
            or not str(job["min_salary"]).isnumeric()
            or int(str(job["max_salary"])) < int(str(job["min_salary"]))
        ):
            raise TypeError()
        else:
            return (
                int(str(job["min_salary"]))
                <= int(salary)
                <= int(str(job["max_salary"]))
            )
    except TypeError:
        raise ValueError(
            """O valores não são números ou o salário máximo
             é menor do que o salário mínimo"""
        )
    except KeyError:
        raise ValueError(
            "A chave min_salary ou max_salary não foi localizada no dicionário"
        )


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filter = []
    try:
        for job in jobs:
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                filter.append(job)
    except TypeError:
        raise ValueError(
            "Salary é uma string que não representa um número válido"
        )
    finally:
        return filter
