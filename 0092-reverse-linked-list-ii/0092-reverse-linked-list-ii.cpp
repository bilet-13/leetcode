/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* pre = dummy;
        ListNode* next_node = nullptr;
        ListNode*  cur = nullptr;

        for(auto i = 0; i <left-1; i++){
            pre = pre->next;
        }
        cur = pre->next;
        
        for(auto i=left; i < right; i++){
            next_node = cur->next;
            cur->next = next_node->next;
            next_node->next = pre->next;
            pre->next = next_node;
        }
        return dummy->next;
    }
};