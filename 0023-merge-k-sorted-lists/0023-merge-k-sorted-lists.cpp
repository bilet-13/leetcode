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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> min_heap(cmp);

        for (auto list : lists) {
            if (list != nullptr) {
                min_heap.push(list);
            }
        }
        auto dummy = new ListNode();
        auto curr = dummy;

        while (!min_heap.empty()) {
            auto min_node = min_heap.top();
            min_heap.pop();

            curr->next = min_node;
            curr = curr->next;

            if (min_node->next != nullptr) {
                min_heap.push(min_node->next);
            }
        }
        return dummy->next;
    }
};
