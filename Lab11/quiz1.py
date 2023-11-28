def get_assessment_mark(assessment_name, mark_min, mark_max):
    user_input = input(f"Enter {assessment_name} mark ({mark_min}-{mark_max}): ")
    try:
        user_input = int(user_input)
        if mark_min <= user_input <= mark_max:
            return user_input
        else:
            return f"{assessment_name} mark must be between {mark_min} and {mark_max}"
    except ValueError:
        return f"{assessment_name} mark is invalid"