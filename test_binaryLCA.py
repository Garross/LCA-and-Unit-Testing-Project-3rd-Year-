import unittest
import binaryLCA

#inherited Node from binaryLCA to avoid typing binaryLCA again and again. Additionally it was an excuse to practice inheritance.
class Node(binaryLCA.Node):
    def __init__(self, value):
        super().__init__(value)
class TestLCA(unittest.TestCase):

    def testBasicTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        #visualising the data
        print(root)
        print("LCA of 6 & 7 is:" , binaryLCA.findLCA(root, 6, 7))

        self.assertEqual(3, binaryLCA.findLCA(root, 6,7), "3 should be the lowest common ancestor of 6 and 7")

    def testEmptyTree(self):
        root = None
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should be -1 since the tree is empty")

    def testNodesNotPresent(self):
        root = Node(1)
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output is -1 since the tree is empty")

    def commonAncestorIsTarget(self):
        root = Node(1)
        root.left = Node(3)
        root.right(5)
        root.left.left(6)
        root.left.right(8)

        self.assertEqual(1,binaryLCA.findLCA(root,1,3),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 1, 5),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 3, 6),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 3, 8),
                         "The output should be 1 since it is both the ancestor node and the target node")

    def testMissingNode(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(-1, binaryLCA.findLCA(root, 4, 9), "Missing node returns -1")
if __name__ == '__main__':
    unittest.main()
