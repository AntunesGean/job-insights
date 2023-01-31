from src.pre_built.counter import count_ocurrences


def test_counter():
    result_python = count_ocurrences('data/jobs.csv', 'Python')
    assert result_python == 1639

    result_javascript = count_ocurrences('data/jobs.csv', 'javascript')
    assert result_javascript == 122
