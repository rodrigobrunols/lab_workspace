package com.my.lab.myhashtable;

import java.util.LinkedList;

public class MyLinkedList {

    Node head;

    void dump() {
        if(head == null ){
            return;
        }

        Node current = head;

        while (current != null){
            System.out.print(current.data + " ->");
            current = current.next;
        }

    }

    Node insert (Node node){
        if (head == null){
            head = node;
            return node;
        }
        Node tail = head;

        while (tail.next != null){
            tail = tail.next;
        }
        tail.next = node;

        return node;
    }

    boolean remove (int data){
        if(head == null ) return false ;

        if(head.data == data) {
            head = head.next;
            return true;
        }

        Node current = head;

        while (current.next != null && current.next.data != data){
            current = current.next;
        }

        current.next = current.next.next; //remove

        return true;

    }

    int count(){
        int count = 0;

        if(head == null ){
            return count;
        }

        Node current = head;

        while (current != null){
            ++count;
            current = current.next;
        }
        return count;
    }

    public static void main(String[] args) {

//        LinkedList<String>
        MyLinkedList list = new MyLinkedList();

        list.insert(new Node(6));
        list.insert(new Node(10));
        list.insert(new Node(17));
        list.insert(new Node(19));


        System.out.println(list.count());


       list.dump();

       list.remove(17);

       System.out.println();

       list.dump();

        list.remove(6);

        System.out.println();

        list.dump();

//        list.remove(19);





    }


}
