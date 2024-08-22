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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == nullptr || head->next == nullptr){
            return head;
        }

        auto dummy = new ListNode(101, head);
        auto prev = dummy;
        auto current = head;
        int count = 1;
        int current_val = head->val;

        while(current != nullptr){
            count = 1;
            current_val = current->val;
            while(current->next != nullptr && current->next->val == current_val){
                current = current->next;
                count += 1;
            }

            if(count == 1){
                prev = prev->next;
            }
            else{
                prev->next = current->next;
            }

            current = current->next;
        }
        return dummy->next;
    }
};