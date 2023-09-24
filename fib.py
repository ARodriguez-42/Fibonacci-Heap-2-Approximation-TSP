from __future__ import annotations
import math

class FibNode:
    def __init__(self, val: int, vertices:tuple):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False
        self.vertices = vertices

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val
    
    def __str__(self):
        return f'Verticies: {self.vertices}, Distance: {self.val} '

class FibHeap:
    def __init__(self):
        self.roots = []
        self.min = None
        self.count = 0
        

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int, vertices:tuple) -> FibNode:
        node = FibNode(val, vertices)
        if self.min is None or self.min.val > node.val:
            self.min = node
        self.roots.append(node)
        self.count += 1    
        return node
        
    def delete_min(self) -> None:
        if self.min.children:
            for x in self.min.children:
                x.parent = None
                x.flag = False
                self.roots.append(x)
            self.roots.remove(self.min)
            self.min = None
        else:
            self.roots.remove(self.min)
            self.min = None
        self.count = self.count - 1
        m = math.log2(self.count)
        #need help
        m = math.ceil(m) + 1
        c = [None] * m
        while self.roots != []:
            x = self.roots[0]
            self.roots.remove(x)
            child_count = len(x.children)
            if c[child_count] is None:
                c[child_count] = x
            else:
                d = c[child_count]
                if x.val < d.val:
                    d.parent = x
                    x.children.append(d)
                    self.roots.insert(0, x)
                    c[child_count] = None
                else:
                    x.parent = d
                    d.children.append(x)
                    self.roots.insert(0, d)
                    c[child_count] = None        
        #move array into heap
        for t in c:
            if t is not None:
                self.roots.append(t)
        #find new min
        self.min = self.roots[0]
        for x in self.roots:
            if x.val < self.min.val:
                self.min = x
              

    def find_min(self) -> FibNode:
        #return min node 
        return self.min

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        self.promote(node)        
        if new_val < self.min.val or self.min is None:
            self.min = node
    
    def promote(self, node: FibNode) -> None:
        if node not in self.roots:
            p = node.parent
            p.children.remove(node)
            self.roots.append(node)
            node.flag = False
            if p.flag == False:
                self.promote(p)
            elif p not in self.roots:
                p.flag = True 
