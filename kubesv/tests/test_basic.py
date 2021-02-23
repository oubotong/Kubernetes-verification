from kubesv.constraint import build, get_datalog, get_answer
from .context import sample

import z3
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_egress_traffic(self):
        sample.setup_z3_printer()

        pods, pols, nams = sample.paper_example()
        gi = build(pods, pols, nams, 
            check_self_ingress_traffic=True, 
            check_select_by_no_policy=False)
        selected_by_none = gi.get_relation_core("selected_by_none")
        selected_by_any = gi.get_relation_core("selected_by_any")
        egress_traffic = gi.get_relation_core("egress_traffic")
        src = gi.declare_var('src-1', gi.pod_sort)
        dst = gi.declare_var('dst-1', gi.pod_sort)

        with open('tests/output/sample.smt2', 'w+') as f:
            f.write(get_datalog(gi.fp, [selected_by_none(src)]))

        sat, answer = get_answer(gi.fp, [egress_traffic(src, dst)])
        assert sat == z3.sat
        with open('tests/output/answer.z3', 'w+') as f:
            f.write(z3.z3printer.obj_to_string(answer))

        pairs = sample.parse_z3_or_and(answer)
        with open('tests/output/pairs.out', 'w+') as f:
            for p in pairs:
                dst, src = p
                f.write(str(pods[src].to_dict()) + " -> " + str(pods[dst].to_dict()) + "\n")


if __name__ == '__main__':
    unittest.main()