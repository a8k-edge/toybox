import weakref

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child: 'Node') -> None:
        child.parent = weakref.ref(self)
        self.children.append(child)

root = Node('#1')
child = Node('#2')
root.add_child(child)
print(root, child, child.parent())
del root
print(child, child.parent())