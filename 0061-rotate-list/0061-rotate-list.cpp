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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr or head->next == nullptr){
            return head;
        }

        auto len = 1;
        auto node = head;
        auto dummy = new ListNode(0, head);
        auto tail = dummy;
        while(node->next != nullptr){
            len++;
            node = node->next;
        }
        tail = node;
        k = k % len;
        if (k == 0){
            delete dummy;
            return head;
        }
        auto cur = 1;
        node = head;

        while(cur != len-k and node != nullptr){
            cur += 1;
            node = node->next;
        }
        auto new_head = node->next;
        node->next = nullptr;
        tail->next = head;
        dummy->next = new_head;

        delete dummy;
        return new_head;

    }
};