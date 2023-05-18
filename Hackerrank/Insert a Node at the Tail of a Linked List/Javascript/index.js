
// Complete the insertNodeAtTail function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtTail(head, data) {
    if(!head){
        return {data: data, next: null}
    }
    let currentNode = head;
    let prevNode = null;
    while(currentNode){
        prevNode = currentNode
        currentNode = currentNode.next
    }
    prevNode.next = {data: data, next: null}
    return head


}
