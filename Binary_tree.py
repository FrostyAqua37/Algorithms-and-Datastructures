#Methods: __init__(), height() and isBalanced()
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))

def isBalanced(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    print("Balanced Tree:", "True" if isBalanced(root) else "False")
