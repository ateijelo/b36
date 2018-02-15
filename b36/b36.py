from __future__ import print_function

from baseconv import base36
import sys

def b36(n):
    if isinstance(n, str):
        return int(base36.decode(n))
    if isinstance(n, int):
        return base36.encode(n)


if __name__=="__main__":
    s = sys.argv[1]

    try:
        n = int(s)
        to_b36 = base36.encode(int(s))
    except ValueError:
        to_b36 = "-"

    try:
        to_b10 = base36.decode(s)
    except ValueError:
        to_b10 = "-"
    print("base 10   base 36")
    print("-------   -------")
    print("{:>7}   {:>7}".format(s, to_b36))
    print("{:>7}   {:>7}".format(to_b10, s))
