import re

def check_dice(dice):
    pattern = r'\d[dD]\d+'
    result = re.search(pattern, dice)
    return bool(result)

print(check_dice("8007d+0"))