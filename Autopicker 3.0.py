#VALORANT AUTOPICKER BY p1n00

#IMPORTAT LIBRERIAS
import pyautogui
import keyboard
import tkinter
from tkinter import Label, Tk

ventana = Tk()

ventana.title("AUTOPICKER BY p1n00")
def kayo():
    keyboard.record(until="alt gr")

#MOVER A ESQUINA PARA CALIBRAR
    pyautogui.moveTo(1,1)

#PICKEO DE KAYO
    pyautogui.moveTo(826,933)
    pyautogui.click(826,933)
    pyautogui.click(826,933)
    pyautogui.click(826,933)

#CONFIRMAR
    pyautogui.moveTo(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)

def jett():
    keyboard.record(until="alt gr")

#MOVER A ESQUINA PARA CALIBRAR
    pyautogui.moveTo(1,1)

#PICKEO DE JETT
    pyautogui.moveTo(760,926)
    pyautogui.click(760,926)
    pyautogui.click(760,926)
    pyautogui.click(760,926)

#CONFIRMAR
    pyautogui.moveTo(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)

def sage():
    keyboard.record(until="alt gr")

#MOVER A ESQUINA PARA CALIBRAR
    pyautogui.moveTo(1,1)

#PICKEO DE SAGE
    pyautogui.moveTo(1108,926)
    pyautogui.click(1108,926)
    pyautogui.click(1108,926)
    pyautogui.click(1108,926)
    

#CONFIRMAR
    pyautogui.moveTo(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)
    
def skye():
    keyboard.record(until="alt gr")

#MOVER A ESQUINA PARA CALIBRAR
    pyautogui.moveTo(1,1)

#PICKEO DE SKYE
    pyautogui.moveTo(845,998)
    pyautogui.click(845,998)
    pyautogui.click(845,998)
    pyautogui.click(845,998)
    

#CONFIRMAR
    pyautogui.moveTo(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)
    pyautogui.click(979,807)

titulo = tkinter.Label(text=("Selecciona agente y presiona ALT GR cuando quieras que se pickee"))
titulo.pack(side="top")

boton_kayo = tkinter.Button(ventana, text="KAYO", command=kayo)
boton_kayo.pack(side="left")
boton_jett = tkinter.Button(ventana, text="JETT", command=jett)
boton_jett.pack(side="left")
boton_sage = tkinter.Button(ventana, text="SAGE", command=sage)
boton_sage.pack(side="left")
boton_skye = tkinter.Button(ventana, text=("SKYE"), command=skye)
boton_skye.pack(side="left")

ventana.mainloop()