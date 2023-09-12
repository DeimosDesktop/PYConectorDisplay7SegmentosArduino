#PARA RECIBIR##
'''import serial, time
arduino = serial.Serial('COM3', 9600)
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.close()'''
#PARA ENVIAR###
import tkinter as tk
from tkinter import ttk, Label, messagebox
import serial, time
root = tk.Tk()
root.title("Controlador de 7 segmentos")
root.geometry("410x200")
root.resizable(False,False)
#ICONO:
# <a href="https://www.flaticon.es/iconos-gratis/bloques-de-numeros" # title="bloques de números iconos">
# Bloques de números iconos creados por surang - 
# Flaticon</a>
icono = tk.PhotoImage(file="icono.png")
root.iconphoto(True, icono)
global mensaje
global conexion
conexion = serial.Serial('COM3', 9600)
time.sleep(2)
conexion.write(b'A')
conexion.close()

####CONTROLES####
mensaje = tk.Label(root, text="")
mensaje.pack(side="bottom")

#Frame de botones
frameBotones = tk.Frame(root)
frameBotones.pack(side="top")

frameLabelBotones = tk.LabelFrame(frameBotones, text="Control manual de Números", 
                                  width="130", height="150")

frameLabelBotones.pack(ipadx="60", pady="10")
frameLabelCombobox = tk.LabelFrame(frameBotones, text="Selecciona un elemento.", width="130", height="150")
frameLabelCombobox.pack(side="top")
###FUNCIONALIDAD####
def cero():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'0')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 0")
def uno():
    print("UNO")
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'1')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 1")
def dos():
    print("DOS")
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'2')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 2")
def tres():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'3')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 3")
def cuatro():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'4')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 4")
def cinco():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'5')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 5")
def seis():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'6')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 6")
def siete():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'7')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 7")
def ocho():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'8')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 8")
def nueve():
    conexion = serial.Serial('COM3', 9600)
    time.sleep(2)
    conexion.write(b'9')
    conexion.close()
    mensaje.configure(text="Se está mostrando el número 9")
def seleccionElementoCombo(event):
    elemento=seleccionFuncion.current()
    messagebox.showinfo(title="Nuevo elemento seleccionado",
          message=elemento)
    if elemento==0:
        conexion = serial.Serial('COM3', 9600)
        time.sleep(2)
        conexion.write(b's')
        conexion.close()
        mensaje.configure(text="Secuencia de todos los números del display")
    if elemento==1:
        conexion = serial.Serial('COM3', 9600)
        time.sleep(2)
        conexion.write(b'p')
        conexion.close()
        mensaje.configure(text="Mostrando solo números pares")
    if elemento==2:
        conexion = serial.Serial('COM3', 9600)
        time.sleep(2)
        conexion.write(b'i')
        conexion.close()
        mensaje.configure(text="Mostrando solo números impares")

#botones para mostrar los números.
boton0 = tk.Button(frameLabelBotones, text="0", bg="#CCEAFF", pady="8", padx="8", command=cero)
boton0.pack(side="left",ipadx="2", ipady="2")
boton1 = tk.Button(frameLabelBotones, text="1", bg="#CCEAFF", pady="8", padx="8", command=uno)
boton1.pack(side="left",padx="5", ipadx="2", ipady="2")
boton2 = tk.Button(frameLabelBotones, text="2", bg="#CCEAFF", pady="8", padx="8", command=dos)
boton2.pack(side="left", ipadx="2", ipady="2")
boton3 = tk.Button(frameLabelBotones, text="3", bg="#CCEAFF", pady="8", padx="8", command=tres)
boton3.pack(side="left", padx="5",ipadx="2", ipady="2")
boton4 = tk.Button(frameLabelBotones, text="4", bg="#CCEAFF", pady="8", padx="8", command=cuatro)
boton4.pack(side="left", ipadx="2", ipady="2")
boton5 = tk.Button(frameLabelBotones, text="5", bg="#CCEAFF", pady="8", padx="8", command=cinco)
boton5.pack(side="left",padx="5",ipadx="2", ipady="2")
boton6 = tk.Button(frameLabelBotones, text="6", bg="#CCEAFF", pady="8", padx="8", command=seis)
boton6.pack(side="left",ipadx="5", ipady="2")
boton7 = tk.Button(frameLabelBotones, text="7", bg="#CCEAFF", pady="8", padx="8", command=siete)
boton7.pack(side="left", padx="5", ipadx="2", ipady="2")
boton8 = tk.Button(frameLabelBotones, text="8", bg="#CCEAFF", pady="8", padx="8", command=ocho)
boton8.pack(side="left",ipadx="2", ipady="2")
boton9 = tk.Button(frameLabelBotones, text="9", bg="#CCEAFF", pady="8", padx="8", command=nueve)
boton9.pack(side="left", padx="5", ipadx="2", ipady="2")
###combobox
seleccionFuncion=ttk.Combobox(frameLabelCombobox, state="readonly",
                              value=['Mostrar secuencia', 'Pares', 'impares'])
seleccionFuncion.bind("<<ComboboxSelected>>", seleccionElementoCombo)
seleccionFuncion.pack(side="top")
#Label

root.mainloop()