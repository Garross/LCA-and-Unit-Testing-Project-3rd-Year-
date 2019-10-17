import DAG_LCA
import unittest




class TestDag(unittest.TestCase):

    def test_basicDAGPrinting(self):
        correct = {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': []}
        testDag = DAG_LCA.DAG()
        testDag.add_vertex("A")
        testDag.add_vertex("B")
        testDag.add_vertex("C")
        testDag.add_vertex("D")

        testDag.add_edge(["A", "B"])
        testDag.add_edge(["B", "C"])
        testDag.add_edge(["C", "D"])

        dictionary = testDag.graphDict()
        self.assertEqual(correct, dictionary, "Incorrect result:" + str(dictionary))


if __name__ == '__main__':
    unittest.main()
