# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# сложность O(n)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root) # используем очередь, в которую будут добавляться узлы на каждом уровне
        res = []
        while q: # цикл, который будет работать пока очередь не станет пустой
            qlen = len(q) # вычисляем количество узлов
            list1 = [] # в него будут добавляться значения узлов на текущем уровне
            for i in range(qlen): # проходит по каждому узлу на текущем уровне
                node = q.popleft() # извлекаем первый элемент из очереди
                if node: # если узел не равен none, то его значение добавляется в список list1
                    list1.append(node.val)
                    q.append(node.left) # если есть правый и левый потомок, то они добавляются в конец очереди q
                    q.append(node.right)
            if list1: # если список не пустой, добавляется СА узлов на каждом уровне
                res.append(sum(list1) / len(list1))
        return res
