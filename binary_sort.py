def tree_by_levels(root):
    if not root:
        return []

    listik = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        listik.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return listik
    
