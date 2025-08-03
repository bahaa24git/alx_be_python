def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        return numerator / denominator
    except ValueError as e:
        print(e)
        return None
    except ZeroDivisionError as e:
        print(e)

safe_divide(10,7)        