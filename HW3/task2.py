# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# сложность O(n)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr = head
        s = '' # переменная куда будем записывать данные
        while ptr != None: # итерация по узлам списка с помощью цикла
            s += str(ptr.val) # к строке добавляется значение узла, преобразованное в строку
            ptr = ptr.next
        return int(s, 2) # строка преобразуется в число
