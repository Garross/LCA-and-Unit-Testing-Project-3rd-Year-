import unittest
import binaryLCA

class TestLCA(unittest.TestCase):

    def testBasicTree(self):
        root = binaryLCA.Node(1)
        root.left = binaryLCA.Node(2)
        root.right = binaryLCA.Node(3)
        root.left.left = binaryLCA.Node(4)
        root.left.right = binaryLCA.Node(5)
        root.right.left = binaryLCA.Node(6)
        root.right.right = binaryLCA.Node(7)

        #visualising the data
        print(root)
        self.assertEqual(3, binaryLCA.findLCA(root, 6,7), "3 is the lowest common ancestor of 6 and 7")

    def testEmptyTree(self):
        root = None
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output is -1 since the tree is empty")



if __name__ == '__main__':
    unittest.main()
