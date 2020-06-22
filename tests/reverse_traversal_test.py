import unittest

from easy.reverse_traversal import rebuild_tree


def inorder_traversal(tree_root, traversal_output: list):
    if tree_root.left is not None:
        inorder_traversal(tree_root.left, traversal_output)
    traversal_output.append(tree_root.value)
    if tree_root.right is not None:
        inorder_traversal(tree_root.right, traversal_output)


def preorder_traversal(tree_root, traversal_output: list):
    traversal_output.append(tree_root.value)
    if tree_root.left is not None:
        preorder_traversal(tree_root.left, traversal_output)
    if tree_root.right is not None:
        preorder_traversal(tree_root.right, traversal_output)


def postorder_traversal(tree_root, traversal_output: list):
    if tree_root.left is not None:
        postorder_traversal(tree_root.left, traversal_output)
    if tree_root.right is not None:
        postorder_traversal(tree_root.right, traversal_output)
    traversal_output.append(tree_root.value)


class TestTreeRebuild(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(
            rebuild_tree([], "inorder"),
            None,
            "Empty tree must be returned when there is no traversal result",
        )

        self.assertEqual(
            rebuild_tree(None, "inorder"),
            None,
            "Empty tree must be returned when there is no traversal result",
        )

    def test_traversal_types(self):
        with self.assertRaises(AssertionError):
            rebuild_tree([], "abc")

        with self.assertRaises(AssertionError):
            rebuild_tree(["a", "b", "c"], "abc")

    def test_traversal_result_length_1(self):
        _traversal_result = ["a"]
        _regenerated_result = []

        _result = rebuild_tree(_traversal_result, "inorder")
        inorder_traversal(_result, _regenerated_result)
        self.assertEqual(
            _traversal_result, _regenerated_result, "Tree wasn't rebuilt correctly!"
        )

        _regenerated_result = []
        _result = rebuild_tree(_traversal_result, "preorder")
        preorder_traversal(_result, _regenerated_result)
        self.assertEqual(
            _traversal_result, _regenerated_result, "Tree wasn't rebuilt correctly!"
        )

        _regenerated_result = []
        _result = rebuild_tree(_traversal_result, "postorder")
        postorder_traversal(_result, _regenerated_result)
        self.assertEqual(
            _traversal_result, _regenerated_result, "Tree wasn't rebuilt correctly!"
        )

    def test_traversal_result(self):
        _traversal_result = ["a", "b", "d", "e", "c", "f", "g"]
        _regenerated_result = []

        _result = rebuild_tree(_traversal_result, "inorder")
        self.assertIsNotNone(_result, "Tree wasn't rebuild correctly!")

        inorder_traversal(_result, _regenerated_result)
        self.assertEqual(
            _traversal_result, _regenerated_result, "Tree wasn't rebuilt correctly!"
        )

        _regenerated_result = []
        _result = rebuild_tree(_traversal_result, "preorder")
        self.assertIsNotNone(_result, "Tree wasn't rebuild correctly!")

        preorder_traversal(_result, _regenerated_result)
        self.assertEqual(
            _traversal_result, _regenerated_result, "Tree wasn't rebuilt correctly!"
        )

        _regenerated_result = []
        _result = rebuild_tree(_traversal_result, "postorder")
        self.assertIsNotNone(_result, "Tree wasn't rebuild correctly!")

        postorder_traversal(_result, _regenerated_result)
        self.assertEqual(
            _traversal_result, _regenerated_result, "Tree wasn't rebuilt correctly!"
        )
