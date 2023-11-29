def get_assessment_mark(assessment_name, mark_min, mark_max):
    # {
    """
    Ask user to enter assessment mark and return the mark.
    Raise ValueError if one of the following occurs:
    - mark is not an integer
    - mark is out of range
    """

    # ask user to enter mark
    user_input = input(
        "Enter {0} mark ({1}-{2}): ".format(assessment_name, mark_min, mark_max)
    )

    # check if mark is integer
    try:
        mark = int(user_input)
    except ValueError as e:
        raise ValueError("{0} mark is invalid".format(assessment_name))

        # check mark between max and min
    if mark > mark_max:
        raise ValueError(
            "{0} mark must be between {1} and {2}".format(
                assessment_name, mark_min, mark_max
            )
        )

    if mark < mark_min:
        raise ValueError(
            "{0} mark must be between {1} and {2}".format(
                assessment_name, mark_min, mark_max
            )
        )

    return mark


# }

# write your code here
try:
    assignment_mark = get_assessment_mark("assignment", 0, 20)
    project_mark = get_assessment_mark("project", 0, 30)
    final_exam_mark = get_assessment_mark("final exam", 0, 50)

    total_mark = assignment_mark + project_mark + final_exam_mark
    print("Total mark:", total_mark)

except ValueError as e:
    print("Error:", e)
