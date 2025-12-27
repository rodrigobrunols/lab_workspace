package com.my.lab.myhashtable;

import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.Objects;

@Component
public class MyHashTable {


    private static class Node {
        private String key;
        private String value;

        public Node(String key, String value) {
            this.key = key;
            this.value = value;
        }
    }

    private Node[] table;

    public static final int MAX_SIZE = 256;

    private int count = 0;


    public MyHashTable(Integer size) {

        if(size <= 0) {
            throw new IllegalArgumentException("size");
        }
        table = new Node[size];
    }

    public MyHashTable(){
        this(MAX_SIZE);
    }


    public int generateHash(Node node) {
        return Math.abs(node.hashCode() % 7);
    }

    public Node insert(Node node){

       int index = generateHash(node);


       while(table[index] != null ){
           System.out.println("Colisao: " + node.value);
           ++index;
           if(index >= 256){
               throw new ArrayStoreException("Table Full");
           }
       }

       System.out.println(index);//find the index

       table[index] = node;

       count++;

        return node;

    }


    void dump() {
        for (int i=0; i< table.length; i++){
            if(table[i] != null){
                System.out.println(i + ":" + table[i].value);
            }
        }
    } // end dump()

    public static void main(String[] args) {
        MyHashTable table = new MyHashTable();

        table.insert(new Node("1", "Buiu"));

        table.insert(new Node("2", "Clarinha"));

        table.insert(new Node("3", "Fiona"));

        table.insert(new Node("4", "Thor"));


        table.dump();
    }


}
