class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []

            return dfs(node.left) + [node.val] + dfs(node.right)

        nums = dfs(root)

        return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))