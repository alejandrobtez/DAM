package com.example;

public class Calculadora {  
    private ServicioMatematico servicio;  
   
    public Calculadora(ServicioMatematico servicio) {
         this.servicio = servicio;   
        }  
         
    public int calcularSuma(int a, int b) { 
        return servicio.suma(a, b); 
    }
}