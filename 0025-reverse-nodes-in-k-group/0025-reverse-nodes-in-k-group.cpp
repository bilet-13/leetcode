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
    ListNode* reverseKGroup(ListNode* head, int k) {
        // find the head of the head of k node and the head of next head of next k nodes
        // reverse the k nodes and let the tail of reversed k node point to next head 
        // repeat
        // if cna not find next head break

        ListNode *dummy = new ListNode(0, head);
        ListNode *start = dummy->next;
        ListNode *prev = dummy;
        ListNode *next_head = nullptr;
        stack<ListNode*> reversed_nodes;

        while (start != nullptr) {
            next_head = start;
            int node_num = 0;

            for (int i = 0; i < k; i++) {
                if (next_head == nullptr) {
                    break;
                } 
                reversed_nodes.push(next_head);
                node_num += 1;
                next_head = next_head->next;
            }

            if (reversed_nodes.size() < k) {
                break;
            }

            while (!reversed_nodes.empty()) {
                auto node = reversed_nodes.top();
                reversed_nodes.pop();

                prev->next = node;
                prev = node;
            }
            prev->next = next_head;
            start = next_head;
        }
        return dummy->next;
    }
};
