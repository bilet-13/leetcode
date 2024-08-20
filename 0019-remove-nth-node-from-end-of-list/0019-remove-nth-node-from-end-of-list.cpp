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
        
        ListNode* prev_node = nullptr;
        ListNode* cur = head;
        auto index = 1;
        while (cur != nullptr){
            if (index == n+1){
                prev_node = head;
            }
            else if (index > n+1){
                prev_node = prev_node->next;
            }
            cur = cur->next;
            index += 1;
        }
        // if removed node is head
        if (prev_node == nullptr){
            auto new_head = head->next;
            delete head;
            return new_head;
        }

        //remove node if node is not head
        auto deleted_node = prev_node->next;
        prev_node->next = deleted_node->next;
        delete deleted_node;
        return head;

    }
};