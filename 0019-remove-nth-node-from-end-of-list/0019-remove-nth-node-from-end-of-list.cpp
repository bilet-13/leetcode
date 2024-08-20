/**
 * Definition for singly-linked list->
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* dummy = new ListNode(0, head);
        auto slow = dummy;
        auto fast = dummy;
        
        for (auto i = 0; i < n; i++){
            fast = fast->next;
        }
        
        while(fast->next != nullptr){
            slow = slow->next;
            fast = fast->next;
        }

        auto removed_node = slow->next;
        slow->next = removed_node->next;
        delete removed_node;

        return dummy->next;
        
    }
};