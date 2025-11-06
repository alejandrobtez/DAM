package test.java;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;
 
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import com.example.*;
 
public class Prueba {
 
    @Test
    public void testCalcularSuma() {
        // 1. Crear un mock de ServicioMatematico
        ServicioMatematico servicioMock = mock(ServicioMatematico.class);
 
        // 2. Definir el comportamiento del mock
        when(servicioMock.suma(5, 3)).thenReturn(10);
 
        // 3. Usar el mock en la clase que queremos probar
        Calculadora calculadora = new Calculadora(servicioMock);
 
        // 4. Llamar al método y verificar el resultado
        int resultado = calculadora.calcularSuma(5, 3);
        assertEquals(10, resultado);
 
        // 5. Verificar que el método fue llamado correctamente
        verify(servicioMock).suma(5, 3);
    }
}