import unittest
import binaryLCA


# inherited Node from binaryLCA to avoid typing binaryLCA again and again. Additionally it was an excuse to practice inheritance.
class Node(binaryLCA.Node):
    def __init__(self, value):
        super().__init__(value)


class TestLCA(unittest.TestCase):

    def testBasicTree(self):
        print("Test1: Test Basic Tree:")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # visualising the data

        print(root)

        self.assertEqual(3, binaryLCA.findLCA(root, 6, 7), "3 should be the lowest common ancestor of 6 and 7")

    def testEmptyTree(self):
        print("Test2: Test Empty Tree:")
        root = None
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should be -1 since the tree is empty")

    def testBothNodesNotPresent(self):
        print("Test3: testBothNodesNotPresent:")
        root = Node(1)
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should be -1 both nodes are missing")

    def testOneNodeNotPresent(self):
        print("Test4: testOneNodeNotPresent:")
        root = Node(1)
        root.left = Node(6)
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should -1 since one of the nodes is missing")

    def commonAncestorIsTarg(self):
        print("Test5: commonAncestorIsTarget")
        root = Node(1)
        root.left = Node(3)
        root.right = Node(5)
        root.left.left = Node(6)
        root.left.right = Node(8)

        self.assertEqual(1, binaryLCA.findLCA(root, 1, 3),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 1, 5),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 3, 6),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 3, 8),
                         "The output should be 1 since it is both the ancestor node and the target node")


    def testMissingNode(self):
        print("Test6: testMissingNode")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(-1, binaryLCA.findLCA(root, 10, 9), "Missing node returns -1")

    def duplicateNodesLucky(self):
        print("Test7: duplicateNodesLucky")
        root = Node(1)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(50)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(1, binaryLCA.findLCA(root, 1, 2), "Both the common ancestor and target are seperate nodes both"\
                                                           "storing the value 1")

    def duplicateNodes(self):
        print("Test8: duplicateNodes:")
        root = Node(1)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(1, binaryLCA.findLCA(root, 1, 2),\
                         "Both the common ancestor and target are seperate nodes both"\
                         "storing the value 1")

        print(root)
        print("LCA of 6 & 7 is:", binaryLCA.findLCA(root, 6, 7))

    def testSingle(self):
        print("Test9: testSingle")
        root = Node(1)

        assert binaryLCA.findLCA(root, 1, 1) == 1, \
            "Should be 1 but got: " + str(binaryLCA.findLCA(root, 1, 1))


if __name__ == '__main__':
    unittest.main()
