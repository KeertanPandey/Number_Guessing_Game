def calculate_score(attempts):

    if attempts <= 2:
        return 100
    elif attempts <= 4:
        return 75
    elif attempts <= 6:
        return 50
    elif attempts == 7:
        return 25
    else:
        return 0