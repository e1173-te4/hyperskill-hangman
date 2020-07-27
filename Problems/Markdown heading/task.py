def heading(a, b=1):
    if b < 1:
        b = 1
    if b > 6:
        b = 6
    return '#' * b + ' ' + a
