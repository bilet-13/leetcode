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
    ListNode* partition(ListNode* head, int x) {
        if (head == nullptr or head->next == nullptr){
            return head;
        }

        ListNode* less_head = new ListNode(0);
        ListNode* more_head = new ListNode(0);
        auto less_tail = less_head;
        auto more_tail = more_head;
        auto node = head;

        while(node != nullptr){
            if(node->val < x){
                less_tail->next = node;
                less_tail = less_tail->next;
            }
            else{
                more_tail->next = node;
                more_tail = more_tail->next;
            }
            node = node->next;
        } 
        more_tail->next = nullptr;

        ListNode* new_head = nullptr;
        less_tail->next = more_head->next;
        new_head = less_head->next;

        return new_head;
    }
};