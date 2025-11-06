/*Crea tres hilos que cuenten hasta diez y muestren el número en la consola. Cada hilo debe contar a una velocidad distinta, por ejemplo, uno cada medio segundo, otro cada segundo, y otro cada dos segundos.*/

public class hilos2{

    public hilos2(){
    }
 
    public static void main(String[] args) {
        Thread hilo = new Thread(new Contador(500));
        Thread hilo2  = new Thread(new Contador(1000));
        Thread hilo3  = new Thread(new Contador(2000));
        hilo.setName("Dani");
        hilo2.setName("Sergio");
        hilo3.setName("Galeano");
        hilo.start();
        hilo2.start();
        hilo3.start();
    }
}

class Contador implements Runnable{
    private int velocidad;

    public Contador(int velocidad){
        this.velocidad = velocidad;
    }

    @Override 
    public void run(){
        for(int i=0;i<10;i++){
            System.out.println( Thread.currentThread().getName() + " a velocidad de " + velocidad +" milisegundos :" + (i + 1));
            try {
                Thread.sleep(velocidad);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Hilo interrumpido");
            }
        }
    }
}
 