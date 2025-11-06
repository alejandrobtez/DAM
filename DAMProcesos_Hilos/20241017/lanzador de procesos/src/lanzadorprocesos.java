
import java.io.*;

public class lanzadorprocesos {
    public static void main(String[] args){
        String archivo = "CodeInjectionExampleWindows.java";
        ProcessBuilder pb = new ProcessBuilder("cmd","/c","find" ,"/c" ,"/v","\"\"", archivo );
        try{
            Process process = pb.start();
            BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream()));

            String linea;
            while ((linea = br.readLine()) != null){
                System.out.println("Resultado:" + linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
