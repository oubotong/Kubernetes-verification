from kubesv.constraint import build, get_datalog, get_answer
from .context import sample

import z3
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_egress_traffic(self):
        sample.setup_z3_printer()

        pods, pols, nams = sample.paper_example()
        gi = build(pods, pols, nams)
        egress_traffic = gi.get_relation_core("egress_traffic")
        src = gi.declare_var('src', gi.pod_sort)
        dst = gi.declare_var('dst', gi.pod_sort)

        with open('tests/output/sample.smt2', 'w+') as f:
            f.write(get_datalog(gi.fp, [egress_traffic(src, dst)]))

        sat, answer = get_answer(gi.fp, [egress_traffic(src, dst)])
        assert sat == z3.sat
        with open('tests/output/answer.datalog', 'w+') as f:
            f.write(z3.z3printer.obj_to_string(answer))


if __name__ == '__main__':
    unittest.main()