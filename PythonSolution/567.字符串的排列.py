#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (42.46%)
# Likes:    372
# Dislikes: 0
# Total Accepted:    91.4K
# Total Submissions: 215K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
# 
# 
# 
# 
# 提示：
# 
# 
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# @lc code=end

