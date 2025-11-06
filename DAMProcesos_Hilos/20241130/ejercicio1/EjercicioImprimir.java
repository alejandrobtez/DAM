/*Ejercicio básico para practicar
Crea un programa donde dos hilos trabajen simultáneamente. Uno imprimirá números del 1 al 10, y el otro imprimirá letras de la 'A' a la 'J'. Usa la interfaz Runnable para implementarlo.

Pistas:

Implementa la interfaz Runnable en dos clases diferentes.
Usa Thread.sleep() para simular pausas y observar la concurrencia.
Crea e inicia ambos hilos en el main. */
class ImprimeNumeros implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i <= 10; i++) {
            System.out.println(Thread.currentThread().getName() + " número: " + i);
            try {
                Thread.sleep(500); // Pausa de 500 ms
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

class ImprimeLetras implements Runnable {
    @Override
    public void run() {
        for (char letra = 'A'; letra <= 'J'; letra++) {
            System.out.println(Thread.currentThread().getName() + " letra: " + letra);
            try {
                Thread.sleep(500); // Pausa de 500 ms
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

public class EjercicioImprimir {
    public static void main(String[] args) {
        // Crear hilos
        Thread numerador = new Thread(new ImprimeNumeros());
        Thread letrador = new Thread(new ImprimeLetras());

        // Dar nombres a los hilos (opcional, para mayor claridad en la salida)
        numerador.setName("Numerador");
        letrador.setName("Letrador");

        // Iniciar los hilos
        numerador.start();
        letrador.start();
    }
}
