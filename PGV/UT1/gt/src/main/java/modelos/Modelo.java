package modelos;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Modelo {
    public List<String[]> obtenerProcesos() {
        List<String[]> procesos = new ArrayList<>();
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("ps", "-eo", "pid,euser,comm");
            Process process = processBuilder.start();
            
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            reader.readLine();
            
            while ((line = reader.readLine()) != null) {
                String[] procesoData = line.trim().split("\\s+", 3);
                procesos.add(procesoData);
            }
            
            process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return procesos;
    }
}
