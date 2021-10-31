import sys


def funct(v_t, st, pr):
    print(f"Заработная плата {(float(v_t) * float(st) + float(pr)):.2f}")


v_t = sys.argv[1]
st = sys.argv[2]
pr = sys.argv[3]

funct(v_t, st, pr)
