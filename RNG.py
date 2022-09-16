import random
import time

def rand_generator(lower, upper, n = 1):
    seed = int(time.time())
    random.seed(seed)

    out = f'<b><u>{n} random number(s) between {lower} and {upper}</u></b>'
    out += f'\nseed: {seed}'
    for _ in range(n):
        out += '\n' + str(random.randint(lower, upper))
    return [out]

def main(args):
    if len(args) < 2:
        return ['Too few arguments']
    if len(args) > 3:
        return ['Too many arguments']

    args_int = []
    for i in args:
        try:
            args_int.append(int(i))
        except:
            return ['Error parsing ints from args']

    lower = args_int[0]
    upper = args_int[1]
    if upper < lower:
        return ['Upper bound less than lower bound']

    if len(args_int) == 2:
        return rand_generator(lower, upper)
    n = args_int[2]
    return rand_generator(lower, upper, n)
