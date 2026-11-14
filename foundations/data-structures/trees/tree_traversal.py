class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return

    print(node.value)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)

    root.left.left = Node(3)
    root.left.right = Node(7)

    root.right.left = Node(15)
    root.right.right = Node(25)

    print("Preorder:")
    preorder(root)

    print("\nInorder:")
    inorder(root)

    print("\nPostorder:")
    postorder(root)