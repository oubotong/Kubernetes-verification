from z3 import BoolRef, BitVecRef
from .example import paper_example

def setup_z3_printer():
    from z3 import z3printer
    z3printer._Formatter.max_depth = 10000
    z3printer._Formatter.max_args = 100000
    z3printer._Formatter.max_visited = 1000000
    z3printer._PP.max_width = 200
    z3printer._PP.bounded = False
    z3printer._PP.max_lines = 1000000


def parse_z3_or_and(answer: BoolRef):
    # assume the answer is Or(And(Var0, Var1, ...), ...)
    all_answer = set()
    for i in range(answer.num_args()):
        arg = answer.arg(i)
        ans = [-1 for j in range(arg.num_args())]
        for j in range(arg.num_args()):
            # Var(0) == 1
            num = arg.arg(j).arg(1)
            ans[j] = num.as_long()
        all_answer.add(tuple(ans))
    return all_answer
