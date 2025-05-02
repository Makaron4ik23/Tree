def pre_order(root):
    if root is None:
        return []
    listik = []
    def recurse(node):
        if node!=None:
            listik.append(node.data)
            recurse(node.left)
            recurse(node.right)
    recurse(root)
    return listik


# In-order traversal
def in_order(root):
    if root is None:
        return []
    listik = []
    def recurse(node):
        if node!=None:
            recurse(node.left)
            listik.append(node.data)
            recurse(node.right)
    recurse(root)
    return listik
# Post-order traversal
def post_order(root):
    if root is None:
        return []
    listik = []
    def recurse(node):
        if node!=None:
            recurse(node.left)
            
            recurse(node.right)
            listik.append(node.data)
    recurse(root)
    return listik