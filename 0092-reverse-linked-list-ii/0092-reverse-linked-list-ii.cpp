class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *node_ptr;
        ListNode assist_head(7);
        ListNode assist_tail(8);
        ListNode *left_left_ptr;
        ListNode *right_right_ptr;
        ListNode *tail_ptr ;
        ListNode *tmp_ptr;
        stack<ListNode*> node_stack;

        int index = 0;
        bool tail_existed = true;

        assist_head.next = head;

        tail_ptr = &assist_head;
        while(tail_ptr->next != NULL)
            tail_ptr = tail_ptr->next;
        tail_ptr->next = &assist_tail;

        left_left_ptr = &assist_head;
        right_right_ptr = &assist_head;

        for (size_t i = 0; i < (left-1); i++)
            left_left_ptr = left_left_ptr->next;

        for (size_t i = 0; i < right+1 ; i++)
            right_right_ptr = right_right_ptr->next;
        
        
        node_ptr = &assist_head;
        for (size_t i = 0; i < left; i++)
            node_ptr = node_ptr->next;

        for (size_t i = 0; i < (right - left + 1); i++)
        {
            node_stack.push(node_ptr);
            node_ptr = node_ptr->next;
        }

        tmp_ptr = node_stack.top();
        node_stack.pop();
        left_left_ptr->next = tmp_ptr;

        while( !node_stack.empty()){
            node_ptr = node_stack.top();
            //cout<< node_ptr->val<<endl;
            node_stack.pop();
            tmp_ptr->next = node_ptr;
            tmp_ptr = tmp_ptr->next;
        }
        tmp_ptr->next = right_right_ptr;

        tail_ptr = &assist_head;

        while(  tail_ptr->next != &assist_tail)
            tail_ptr = tail_ptr->next;
        tail_ptr->next = NULL;
        //cout<<tail_ptr->val<<endl;

    //     node_ptr =assist_head.next;
    //       while (node_ptr != NULL)
    // {
    //     cout<< node_ptr->val<<endl;
    //     node_ptr = node_ptr->next;
    // }
        return assist_head.next;

    }
        
};