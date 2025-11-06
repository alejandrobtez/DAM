/*Requisitos:
Crear una clase Contador que mantenga el valor del contador.
Implementar un método sincronizado en Contador para incrementar el valor.
Crear una clase Incrementador que implemente Runnable y use el método sincronizado.
Crear y ejecutar varios hilos que utilicen el mismo objeto Contador.
 */
class Contador{
    private int contador = 0;

    public synchronized void incrementar(){
        contador++;
        System.out.println(Thread.currentThread().getName() + " incrementó el valor de contador a :" + getContador());
    }

    public int getContador(){
        return contador;
    }
    
}

class Incrementador implements Runnable {
    private final Contador contador; //Objeto que comparten los hilos

    public Incrementador(Contador contador){ //Constructor
        this.contador = contador;
    }

    @Override

    public void run() {
        for (int i = 0; i < 15; i++) {
            contador.incrementar();
            try {
                Thread.sleep(500);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

public class ContadorGlobal {
    public static void main(String[] args) throws InterruptedException {
        Contador contador = new Contador(); //Crea el objeto compartido por los hilos

        Thread hilo1 = new Thread(new Incrementador(contador),"Contador Principal");
        Thread hilo2 = new Thread(new Incrementador(contador),"Contador Secundario");

        hilo1.start();
        hilo2.start();
    }
}