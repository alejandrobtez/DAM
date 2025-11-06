package ejercicio3_PC;
/*Ejercicio: Productor-Consumidor
Objetivo: Simular un escenario donde un productor genera números y los almacena en un espacio compartido, y un consumidor toma esos números para procesarlos. Ambos hilos deben coordinarse para no interferir y evitar problemas como producir cuando el espacio está lleno o consumir cuando está vacío.

Requisitos:
Crear una clase Buffer que actúe como un espacio compartido entre productor y consumidor.
Usar los métodos wait() y notify() para coordinar los hilos.
Crear clases Productor y Consumidor que implementen Runnable.
Ejecutar ambos hilos en la clase principal.*/

class Buffer{
    private int valor;
    private boolean disponible = false; // Indica si el buffer está disponible para ser utilizado

    public synchronized void producir(int nuevoValor){
        while(disponible){ // Igual que disponible == true
            try {
                wait(); // Espera a que el buffer no tenga un valor
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        valor = nuevoValor; // Coloca el nuevo valor en el buffer
        disponible = true; // Buffer lleno
        System.out.println("Se ha producido: "+ valor);
        notify(); // Avisa a consumidor de que puede acceder al buffer, que hay un valor disponible
    }

    public synchronized int consumir(){
        while (!disponible ){ // Igual que disponible == false
            try {
                wait(); // Espera a que el buffer tenga un valor
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        disponible = false; // Buffer vaciado
        System.out.println("Se ha consumido: " + valor);
        notify(); // Avisa a productor de que puede producir
        return valor; // Devuelve el valor consumido
    }
}

class Productor implements Runnable{
    private final Buffer buffer; // Objeto compartido entre hilos

    public Productor(Buffer buffer){
        this.buffer = buffer;
    }

    @Override
    public void run(){
        for (int i = 0; i <= 5; i++) { //Genera valores
            buffer.producir(i); // Produce valores generados en i, i = nuevoValor
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

}

class Consumidor implements Runnable{
    private final Buffer buffer; // Objeto compartido entre hilos

    public Consumidor(Buffer buffer){
        this.buffer = buffer;
    }

    @Override
    public void run(){
        for (int i = 0; i < 10; i++) { //Genera valores
            buffer.consumir(); // Consume valores generados
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

public class ProductorConsumidor{
    public static void main(String[] args) {
    Buffer buffer = new Buffer();

    Thread hiloProductor = new Thread(new Productor(buffer), "Productor");
    Thread hiloConsumidor = new Thread(new Consumidor(buffer), "Consumidor");

    hiloProductor.start();
    hiloConsumidor.start();

    }
}