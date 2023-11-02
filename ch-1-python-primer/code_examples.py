def compute_gpa(grades: list, points: dict) -> float:
    """Takes in a list containing grades

    Args:
        grades (list): list containing all the grade points
        points (dict): list containing default values for the grade alphabets

    Returns:
        float: GPA value for the supplied grades
    """
    total_courses: int = 0
    total_gpa: float = 0.0
    for grade in grades:
        if grade in points:
            total_gpa += points[grade]
            total_courses += 1
    return float(total_gpa / total_courses)
