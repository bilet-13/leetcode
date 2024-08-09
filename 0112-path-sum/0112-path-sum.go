/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, targetSum int) bool {
    
    if root == nil{
        return false
    }

    if root.Left == nil && root.Right == nil{
        return root.Val == targetSum
    }

    left_sum := hasPathSum(root.Left, targetSum - root.Val)
    right_sum := hasPathSum(root.Right, targetSum - root.Val)

    return left_sum || right_sum
}