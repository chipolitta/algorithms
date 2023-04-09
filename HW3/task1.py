# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Сложность  O(n)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num = [] # будет хранить значения
        while head != None: # используем цикл, чтобы проходить по списку, итерируясь через каждый узел
            num.append(head.val) # извлекаем значение и добавляме в список num
            head = head.next
        return num == num[::-1] # проверяем равен ли список num его обратному порядку