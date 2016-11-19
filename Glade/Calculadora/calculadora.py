#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from gi.repository import Gtk

#metodo de suma, usamos try y except para poder imprimir el error
def on_bSum_clicked(button):
	try:	
		num1 = float(entry.get_text())
		num2 = float(entry2.get_text())	
		opc = num1 + num2
		resultado.set_text(str(opc))
		entry.set_text(str(opc))
		entry2.set_text(" ")

	except:
		resultado.set_text(str(error))
#metodo de resta, usamos try y except para poder imprimir el error
def on_bRes_clicked(button):
	try:
		num1 = float(entry.get_text())
		num2 = float(entry2.get_text())
		opc = num1 - num2
		resultado.set_text(str(opc))
		entry.set_text(str(opc))
		entry2.set_text(" ")
	except:
		resultado.set_text(str(error))
#metodo de multiplicacion, usamos try y except para poder imprimir el error
def on_bMul_clicked(button):
	try:
		num1 = float(entry.get_text())
		num2 = float(entry2.get_text())
		opc = num1 * num2
		resultado.set_text(str(opc))
		entry.set_text(str(opc))
		entry2.set_text(" ")
	except:
		resultado.set_text(str(error))
#metodo de division, usamos try y except para poder imprimir el error
def on_bDiv_clicked(button):
	try:
		num1 = float(entry.get_text())
		num2 = float(entry2.get_text())
		opc = num1 / num2
		resultado.set_text(str(opc))
		entry.set_text(str(opc))
		entry2.set_text(" ")
	except:
		resultado.set_text(str(error))
#metodo de borrar, volvemosa poner a cero los entry 
def borrar(button):
	entry.set_text(" ")
	entry2.set_text(" ")

#Mensaje de error para cuando no se introducen números		
error = "Por favor, introducir solo caracteres númericos"
#Creamos un builder para cargar el .glade y contruir metodos y objetos
builder = Gtk.Builder()
builder.add_from_file("calculadora.glade")
handlers={
	"on_bSum_clicked" : on_bSum_clicked,
	"on_bRes_clicked" : on_bRes_clicked,
	"on_bMul_clicked" : on_bMul_clicked,
	"on_bDiv_clicked" : on_bDiv_clicked,
	"borrar":borrar,
	"gtk_main_quit" : Gtk.main_quit
}

builder.connect_signals(handlers)
resultado=builder.get_object("resultado")
entry=builder.get_object("entry")
entry2=builder.get_object("entry2")
window = builder.get_object("window1")
window.show_all()

Gtk.main()
