class Node:
    def __init__(self, value: str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rebuild_tree(traversal_result: list, traversal_type: str) -> Node:
    assert traversal_type in (
        "inorder",
        "preorder",
        "postorder",
    ), "Traversal type must be on of 'inorder', 'preorder' or 'postorder'"

    if not traversal_result:
        return None

    if len(traversal_result) == 1:
        return Node(traversal_result[0])

    if traversal_type == "inorder":
        pass
    elif traversal_type == "preorder":
        pass
    elif traversal_type == "postorder":
        pass
