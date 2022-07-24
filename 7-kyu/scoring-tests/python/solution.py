def score_test(tests, right, omit, wrong):
    correct_answer_count = tests.count(0)
    omitted_answer_count = tests.count(1)
    wrong_answer_count = tests.count(2)
    return correct_answer_count * right + omitted_answer_count * omit - wrong_answer_count * wrong
