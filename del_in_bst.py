class Solution(object):
    def deleteNode(self, root, key):
        parent = None
        node = root
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
        if node is None:
            return root
        def findMax(n):
            while n.right:
                n = n.right
            return n
        def deleteTarget(node):
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            pred = findMax(node.left)
            val = pred.val
            node.left = self.deleteNode(node.left, val)
            node.val = val
            return node
        if parent is None:
            return deleteTarget(node)
        if parent.left == node:
            parent.left = deleteTarget(node)
        else:
            parent.right = deleteTarget(node)
        return root
