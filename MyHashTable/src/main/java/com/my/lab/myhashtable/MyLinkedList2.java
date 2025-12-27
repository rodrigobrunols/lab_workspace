package com.my.lab.myhashtable;

public class MyLinkedList2 {

    Node head = null;

    void dump() {
        Node current = head;

        if(current == null ){
            return;
        }

        while (current != null){
            System.out.print(current.data + " ->");
            current = current.next;
        }

    }

    void insert (int value){
        if (head == null){
            head = new Node(value);
            return;
        }
        Node current = head;

        while (current.next != null){
            current = current.next;
        }
        current.next = new Node(value);

    }

    void remove (int data){
        if(head == null ) return ;

        if(head.data == data){
            head = head.next;
            return;
        }

        Node current = head;

        while (current.next != null){
            if(current.next.data == data){
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }

    int count(){
        int count = 0;
        Node current = head;
        if(current == null){
            return  count;
        }
        count++;
        while (current.next != null){
            current = current.next;
            count++;
        }
        return count;
    }

    public static void main(String[] args) {

        MyLinkedList2 list = new MyLinkedList2();

        list.insert(6);
        list.insert(10);
        list.insert(17);
        list.insert(19);


        System.out.println(list.count());


       list.dump();

    }


}
