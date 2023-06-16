class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right

indent = 0
def node_name(node: Node):
    if node is None:
        return 'none'
    else:
        return node.id
def common_ancestor(root: Node, a: Node, b:Node):
    global indent
    if root is None:
        p = None
    elif root == a or root == b:
        p = root
    else:
        indent += 1
        left_parent = common_ancestor(root.left, a, b)
        right_parent = common_ancestor(root.right, a, b)
        indent -= 1

        if left_parent is None:
            p =  right_parent
        elif right_parent is None:
            p =  left_parent
        else:
            p = root

    print("%sParent of (%s, %s), (root = %s) == %s" % ('  ' * indent, node_name(a), node_name(b), node_name(root), node_name(p)))
    return p


def verify(root, a, b, p):
    assert(common_ancestor(root, a, b) == p)
    assert(common_ancestor(root, b, a) == p)

def test():
    k = Node('k', None, None)
    j = Node('j', k, None)
    g = Node('g', None, j)
    i = Node('i', None, None)
    f = Node('f', i, None)
    c = Node('c', f, g)
    h = Node('h', None, None)
    e = Node('e', None, h)
    d = Node('d', None, None)
    b = Node('b', d, e)
    a = Node('a', b, c)

    verify(a, b, c, a)
    verify(a, b, d, b)
    verify(a, b, e, b)
    verify(a, b, f, a)
    verify(a, b, g, a)
    verify(a, b, h, b)
    verify(a, b, i, a)
    verify(a, b, j, a)
    verify(a, b, k, a)
    verify(a, c, d, a)
    verify(a, c, e, a)
    verify(a, c, f, c)
    verify(a, c, g, c)
    verify(a, c, h, a)
    verify(a, c, i, c)
    verify(a, c, j, c)
    verify(a, c, k, c)
    verify(a, d, e, b)
    verify(a, d, f, a)
    verify(a, d, g, a)
    verify(a, d, h, b)
    verify(a, d, i, a)
    verify(a, d, j, a)
    verify(a, d, k, a)
    verify(a, e, f, a)
    verify(a, e, g, a)
    verify(a, e, h, e)
    verify(a, e, i, a)
    verify(a, e, j, a)
    verify(a, e, k, a)
    verify(a, f, g, c)
    verify(a, f, h, a)
    verify(a, f, i, f)
    verify(a, f, j, c)
    verify(a, f, k, c)

    verify(a, g, h, a)
    verify(a, g, i, c)
    verify(a, g, j, g)
    verify(a, g, k, g)

    verify(a, h, i, a)
    verify(a, h, j, a)
    verify(a, h, k, a)

    verify(a, i, j, c)
    verify(a, i, k, c)

    verify(a, j, k, j)

    verify(b, f, g, None)

if __name__ == '__main__':
    test()
