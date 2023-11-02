import code_examples as ce


def test_compute_gpa():
    grades = ["A", "B+", "C-"]
    points = {"A": 4.0, "B+": 3.33, "C-": 1.67}
    gpa = ce.compute_gpa(grades, points)
    assert gpa == 3.0
