import java.util.jar.Attributes.Name;

class Conta{
    int contador = 0;    

    public synchronized void incrementar(){
        contador++;
    }

    public int getContador(){ 
        return contador;
    }

}

public class Contador extends Thread{

    private Conta conta = null;
    
    public Contador(String hiloNombre, Conta conta){
        super(hiloNombre);
        this.conta = conta;

    }

    @Override
    public void run (){
        for(int i = 0;i<100; i++){
            conta.incrementar() ;
            System.out.println(getName() + "contador = " + conta.getContador());
        }

    }

    public static void main(String[] args) throws InterruptedException{

    Conta conta = new Conta();

    Contador c1 = new Contador("Beni", conta);
    Contador c2 = new Contador("Galea", conta);
    Contador c3 = new Contador("Sergi", conta);

    c1.start();
    c2.start();
    c3.start();

    c1.join();
    c2.join();
    c3.join();

    System.out.println("Contador: " + conta.getContador());
}

    
}
