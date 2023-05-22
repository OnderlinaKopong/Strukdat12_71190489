class Node:
    def _init_(self, data):
        self.data = data
        self.children = []

class Tree:
    def _init_(self, root):
        self.root = root

    def sums(self, node):
        total = node.data
        for child in node.children:
            total += self.sums(child)
        return total

    def sibling(self, node):
        total = node.data
        if node.parent:
            for child in node.parent.children:
                total += child.data
        return total
    
val200 = Node(200)
val23 = Node(23)
val11 = Node(11)
val13 = Node(13)
val57 = Node(57)
val32 = Node(32)
val42 = Node(42)
val51 = Node(51)
val71 = Node(71)
val12 = Node(12)
val15 = Node(15)
val33 = Node(33)
val8 = Node(8)

val200.children = [val23, val11]
val23.children = [val13, val57]
val11.children = [val32]
val13.children = [val42, val51, val71]
val57.children = [val12, val15]
val32.children = [val33, val8]

tree = Tree(val200)
#test-1
print(f'Total value of node {val200.data} and all of its
decendands = {tree.sums(val200)}')

#test-2
print(f'Total value of all sibling on node {val33.data} =
{t.sibling(val33)}')
