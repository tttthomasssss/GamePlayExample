'''
Created on Jan 2, 2014

@author: thomas
'''
class GameTree(object):
    
    def __init__(self, root):
        self._root = root
        self._size = 1
        
    @property
    def root(self):
        return self._root

    @property
    def size(self):
        return self._size
    
    def is_root(self, node):
        return node.parent == None
    
    def is_leaf(self, node):
        return node.is_leaf()
    
class GameNode(object):
    
    def __init__(self, parent, name, value=None):
        
        self._parent    = parent
        self._children  = list()
        self._value     = value
        self._name      = name
        self._pruned    = True
        
    @property
    def parent(self):
        return self._parent
    
    @property
    def children(self):
        return self._children
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
        
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val
       
    @property
    def pruned(self):
        return self._pruned
    
    @pruned.setter
    def pruned(self, val):
        self._pruned = val
        
    def add_child(self, node):
        self._children.append(node)
        
    def is_leaf(self):
        return len(self._children) == 0
    
    def __str__(self):
        return self._name + ': ' + str(self._value)
    
    def __repr__(self):
        return "%s(name:[%s] value:[%s])" % (self.__class__.__name__, self._name, self._value)