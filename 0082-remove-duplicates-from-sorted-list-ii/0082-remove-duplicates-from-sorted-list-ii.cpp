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
        auto slow = dummy;
        auto fast = head;
        int count = 1;
        int duplicate = head->val;

        while(fast != nullptr){
            count = 1;
            duplicate = fast->val;
            while(fast->next != nullptr && fast->next->val == duplicate){
                fast = fast->next;
                count += 1;
            }

            if(count ==1){
                slow->next = fast;
                fast = fast->next;
                slow = slow->next;
            }
            else{
                slow->next = fast->next;
                fast = fast->next;
            }
        }
        return dummy->next;
    }
};