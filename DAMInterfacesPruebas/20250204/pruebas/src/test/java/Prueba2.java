import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

import com.example.Main;

public class Prueba2 {
    
    @Test
    public void pares(){
        List<Integer> listapares = Arrays.asList(1,2,3,4);
        assertEquals(6,(Main.sumarValoresPares(listapares)));
    }
}
