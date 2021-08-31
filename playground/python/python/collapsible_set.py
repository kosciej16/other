from copy import deepcopy
from functools import reduce


class Node:
    def __init__(self, children=None, name=""):
        self.parent = None  # parent Node
        self.dotted_name = name  # full name with dots separated elements
        self.name = name
        self.children = {c.name: c for c in children or []}
        for c in self.children.values():
            c.parent = self
            c.dotted_name = f"{self.name}.{c.name}" if self.name else c.name
        self.taken = set()  # Set of already taken children for specific node
        self.locked = False  # Indicates that some of parent is already taken
        self.marked = (
            False  # Used in complement to mark all Nodes that have children already in Set
        )

    def add_to_non_locked(self, name):
        if not self.locked:
            self.taken.add(name)

    @property
    def is_complete(self):
        return len(self.taken) == len(self.children)  # We should collapse here

    def change_lock(self, val):
        """ Change locked attribute recursively """
        self.locked = val
        for c in self.children.values():
            c.change_lock(val)

    def clear(self):
        """ Clear Node and children, used in collapse """
        self.taken.clear()
        for c in self.children.values():
            c.clear()

    def mark(self, mark_parent=True, mark_children=True):
        """ Used in complement """
        if self.marked:
            return
        self.marked = True
        if self.parent and mark_parent:
            self.parent.mark(mark_children=False)
        if mark_children:
            for c in self.children.values():
                c.mark(mark_parent=False)

    def get_non_marked(self):
        """ Traverse every Node and take non marked which is what complement should returs """
        if not self.marked:
            res = [self]
        else:
            res = [x for c in self.children.values() for x in c.get_non_marked()]
        self.marked = False
        return res

    def __str__(self):
        ll = [str(c) for c in self.children.values()]
        return f"{self.name}{ll if ll else ''}"


# Creates example structure
f11 = Node(name="f11")
f12 = Node(name="f12")
f21 = Node(name="f21")
f22 = Node(name="f22")
dir1 = Node({f11, f12}, name="dir1")
dir2 = Node({f21, f22}, name="dir2")
file0 = Node(name="file0")
root = Node({dir1, dir2, file0})


class CollapsibleSubset(set):
    def __init__(self, *args, root: Node, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

    def add_el(self, el: list):
        """ Assuming element to add is in form list of elements """
        last = self.get_node(el).parent
        last.add_to_non_locked(el[-1])
        if last.is_complete:
            for t in last.taken:
                self.discard(
                    ".".join([*el[:-1], t])
                )  # Removing all elements from set as we need to collapse
            last.clear()
            last.change_lock(True)
            self.add_el(el[:-1])  # Running recursively for parent
            return
        self.add(".".join(el))

    def union(self, other):
        for el in other:
            self.add_el(el.split("."))

    def complement(self):
        for el in self:
            self.get_node(el).mark()
        x = self.root.get_non_marked()
        return CollapsibleSubset([a.dotted_name for a in x], root=deepcopy(root))

    def get_node(self, el):
        if isinstance(el, str):
            el = el.split(".")
        return reduce(lambda x, y: getattr(x, "children")[y], el, self.root)


s = CollapsibleSubset(root=deepcopy(root))
s2 = CollapsibleSubset(root=deepcopy(root))
s.add_el(["dir1", "f11"])
s2.add_el(["dir1", "f12"])
s2.add_el(["dir2", "f21"])
s.union(s2)
print(s)
sc = s.complement()
print(sc)
