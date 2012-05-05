
def check_float(num):
    try:
        num = float(num)
    except ValueError:
        return False, None
    else:
        return True, num

def check_int(num):
    try:
        num = int(num)
    except ValueError:
        return False, None
    else:
        return True, num