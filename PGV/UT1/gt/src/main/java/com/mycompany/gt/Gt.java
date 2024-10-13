/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.gt;

import controladores.Controlador;
import modelos.Modelo;
import vistas.Vista;

/**
 *
 * @author navarro
 */
public class Gt {

    public static void main(String[] args) {
        Vista vista = new Vista();
        Modelo modelo = new Modelo();
        Controlador controlador = new Controlador(vista, modelo);
        
        vista.setVisible(true);
    }
}
