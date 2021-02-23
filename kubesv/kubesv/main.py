from z3 import *

if __name__ == "__main__":
    fp = Fixedpoint()
    fp_options = {
        "ctrl_c": True,
        "engine": "datalog",
        "datalog.generate_explanations": True,
    }
    fp.set(**fp_options)

    s = BitVecSort(3)
    edge = Function('edge', s, s, BoolSort())
    path = Function('path', s, s, BoolSort())
    a = Const('a', s)
    b = Const('b', s)
    c = Const('c', s)

    fp.register_relation(path,edge)
    fp.declare_var(a, b, c)
    fp.rule(path(a, b), Not(edge(a, b)))
    fp.rule(path(a ,b), [edge(a, c), path(c, b)])

    v1 = BitVecVal(1, s)
    v2 = BitVecVal(2, s)
    v3 = BitVecVal(3, s)
    v4 = BitVecVal(4, s)

    fp.fact(edge(v1, v2))
    fp.fact(edge(v1, v3))
    fp.fact(edge(v2, v4))

    print(fp.to_string([path(v1, v4)]))

    print(fp.query(path(v1, v4)))
    print(fp.get_answer())
