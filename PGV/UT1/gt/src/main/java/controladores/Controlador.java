package controladores;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
import modelos.Modelo;
import vistas.Vista;

public class Controlador implements ActionListener {
    private Vista vista;
    private Modelo modelo;

    public Controlador(Vista vista, Modelo modelo) {
        this.vista = vista;
        this.modelo = modelo;
        
        this.vista.btnUpdate.addActionListener(this);
        this.vista.btnNew.addActionListener(this);
        this.vista.btnKill.addActionListener(this);
        
        actualizarTabla();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == vista.btnUpdate) {
            actualizarTabla();
        }
        if (e.getSource() == vista.btnNew) {
            iniciarNuevoProceso();
        }
        if (e.getSource() == vista.btnKill) {
            pararProceso();
        }
    }
    
    private void actualizarTabla() {
        DefaultTableModel tableModel = (DefaultTableModel) vista.table_p.getModel();
        tableModel.setRowCount(0);
        
        modelo.obtenerProcesos().forEach(proceso -> {
            tableModel.addRow(proceso);
        });
        
        vista.processNum.setText(modelo.obtenerProcesos().size() + " Procesos");
    }
    
    private void iniciarNuevoProceso() {
        String programa = JOptionPane.showInputDialog(vista, "Introduce el nombre del programa a iniciar:");
        
        if (programa != null && !programa.trim().isEmpty()) {
            try {
                // Iniciar el proceso con el nombre introducido
                ProcessBuilder processBuilder = new ProcessBuilder(programa);
                processBuilder.start();
                
                actualizarTabla();
                JOptionPane.showMessageDialog(vista, "El proceso \"" + programa + "\" se ha iniciado correctamente.");
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(vista, "Error al iniciar el proceso: " + ex.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        } else {
            JOptionPane.showMessageDialog(vista, "No se ha introducido un nombre de programa válido.", "Advertencia", JOptionPane.WARNING_MESSAGE);
        }
    }

    private void pararProceso() {
        String pidStr = JOptionPane.showInputDialog(vista, "Introduce el PID del proceso a detener:");
        
        if (pidStr != null && !pidStr.trim().isEmpty()) {
            try {
                int pid = Integer.parseInt(pidStr.trim());
                
                ProcessBuilder processBuilder = new ProcessBuilder("kill", String.valueOf(pid));
                Process process = processBuilder.start();
                
                int exitCode = process.waitFor();
                if (exitCode == 0) {
                    JOptionPane.showMessageDialog(vista, "El proceso con PID " + pid + " ha sido detenido correctamente.");
                } else {
                    JOptionPane.showMessageDialog(vista, "No se pudo detener el proceso con PID " + pid + ". Código de salida: " + exitCode, "Error", JOptionPane.ERROR_MESSAGE);
                }
                
                actualizarTabla();
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(vista, "PID no válido. Introduce un número entero.", "Advertencia", JOptionPane.WARNING_MESSAGE);
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(vista, "Error al detener el proceso: " + ex.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        } else {
            JOptionPane.showMessageDialog(vista, "No se ha introducido un PID válido.", "Advertencia", JOptionPane.WARNING_MESSAGE);
        }
    }
}
