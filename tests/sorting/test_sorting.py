from src.pre_built.sorting import sort_by

jobs_dict = [
    {"min_salary": 20000, "max_salary": 25000, "date_posted": "2023-08-12"},
    {"min_salary": 10000, "max_salary": 15000, "date_posted": "2023-04-27"},
    {"min_salary": 30000, "max_salary": 35000, "date_posted": "2023-10-17"},
]

jobs_dict_min = [
    {"min_salary": 10000, "max_salary": 15000, "date_posted": "2023-04-27"},
    {"min_salary": 20000, "max_salary": 25000, "date_posted": "2023-08-12"},
    {"min_salary": 30000, "max_salary": 35000, "date_posted": "2023-10-17"},
]

jobs_dict_max = [
    {"min_salary": 30000, "max_salary": 35000, "date_posted": "2023-10-17"},
    {"min_salary": 20000, "max_salary": 25000, "date_posted": "2023-08-12"},
    {"min_salary": 10000, "max_salary": 15000, "date_posted": "2023-04-27"},
]

jobs_dict_date = [
    {"min_salary": 30000, "max_salary": 35000, "date_posted": "2023-10-17"},
    {"min_salary": 20000, "max_salary": 25000, "date_posted": "2023-08-12"},
    {"min_salary": 10000, "max_salary": 15000, "date_posted": "2023-04-27"},
]


def test_sort_by_criteria():
    sort_by(jobs_dict, "min_salary")
    assert jobs_dict == jobs_dict_min
    sort_by(jobs_dict, "max_salary")
    assert jobs_dict == jobs_dict_max
    sort_by(jobs_dict, "date_posted")
    assert jobs_dict == jobs_dict_date
