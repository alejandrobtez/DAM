/*Crea un programa en el que un hilo imprima "Hola desde un Hilo" en la consola cinco veces. Usa Thread.sleep(1000) para que el hilo espere un segundo entre cada mensaje.*/
public class hilos1 extends Thread{
    public void run(){
                for(int i=0;i<5;i++){
                    System.out.println("Hola por " + (i + 1) + " vez");
                }
    }
 
    public static void main(String[] args) {
        hilos1 hilo = new hilos1();
        hilos1 hilo1 = new hilos1();
        hilo.start();
        hilo1.start();
    }
}
 