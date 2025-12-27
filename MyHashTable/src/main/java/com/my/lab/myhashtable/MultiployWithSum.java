package com.my.lab.myhashtable;

public class MultiployWithSum {

    private static int multiply(int a , int b){
        int sum = 0;
        for(int i = 0; i < b; i++){
            sum+=a;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(multiply(2,6));
    }
}
