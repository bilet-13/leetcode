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

        struct cmp{
            bool operator () (ListNode* a, ListNode* b){
                return a->val > b->val;
            }
        };
        auto dummy = new ListNode();
        auto cur = dummy;
        priority_queue<ListNode*, vector<ListNode*>, cmp> min_nodes;

        for(const auto& list: lists){
            auto node = list;
            while(node){
                min_nodes.push(node);
                auto tmp = node->next;
                node->next = nullptr;
                node = tmp;
            }
        }

        while(!min_nodes.empty()){
            auto node = min_nodes.top();
            min_nodes.pop();

            cur->next = node;
            cur = cur->next;
        }

        auto head = dummy->next;
        delete dummy;
        return head;
    }
};