from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in dict_jobs:
        assert "salary" in job
        assert "type" in job
        assert "salario" not in job
        assert "tipo" not in job
