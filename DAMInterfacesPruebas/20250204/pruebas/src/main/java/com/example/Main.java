package com.example;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }

    public static int suma(int a, int b){
        return a+b;
    }

    public static  int sumarValoresPares (List<Integer> lista){
        int suma = 0;
        for (int num : lista){
            if (num %2 == 0){
                suma += num;
            }
        }
        return suma;
    }

    public static String nombresMayusculas(List<String> listaNom){
        String nombre = null;
        for(String name : listaNom){
        nombre = name.toUpperCase();
        }
        return nombre;
    }

}