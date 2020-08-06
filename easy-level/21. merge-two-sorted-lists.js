/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var mergeTwoLists = function(l1, l2) {
    var result = new ListNode();
    var pointer = result; 
    
    while(l1 !== null && l2 !== null) {
        if(l1.val < l2.val) {
            pointer.next = l1;
            pointer = l1;
            l1 = l1.next;
        } else {
            pointer.next = l2;
            pointer = l2;
            l2 = l2.next;
        }
    }
    
    if(l1 !== null) {
      pointer.next = l1;
    }

    if(l2 !== null) {
      pointer.next = l2;
    }
    
    return result.next;
};