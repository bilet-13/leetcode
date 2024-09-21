class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        return mergeList(head);
    }

    ListNode* mergeList(ListNode* head) {
        if(!head || !head->next){
            return head;
        }
        auto right = divide(head);
        auto tmp = right->next;
        right->next = nullptr;
        right = tmp;

        auto l_head = mergeList(head);
        auto r_head = mergeList(right);

        return mergeTwoList(l_head, r_head);
    }

    ListNode* mergeTwoList(ListNode* l_head, ListNode* r_head) {
        auto dummy = new ListNode();
        auto cur = dummy;
        auto l_node = l_head;
        auto r_node = r_head;

        // Merge two sorted sublists
        while (l_node && r_node) {
            if (l_node->val < r_node->val) {
                cur->next = l_node;
                l_node = l_node->next;
            } else {
                cur->next = r_node;
                r_node = r_node->next;
            }
            cur = cur->next;
        }

        cur->next = l_node ? l_node : r_node;
        
        // Get the head of the merged list
        auto new_head = dummy->next;
        delete dummy;  // Free the dummy node
        return new_head;
    }

    
    ListNode* divide(ListNode* head) {
        auto slow = head;
        auto fast = head;
        auto prev = head;

        while(fast && fast->next){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        return prev;
    }
};
