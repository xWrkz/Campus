import tkinter as tk
import threading
import Entorno 

def on_enter():
    threading.Thread(target=Entorno.main).start()

root = tk.Tk()
root.title("Formulario de Entrada")

label = tk.Label(root, text="Escenario 3D", font=("Arial", 14))
label.pack(pady=20)

btn_enter = tk.Button(root, text="Ingresar al Escenario", command=on_enter, width=50, height=2)
btn_enter.pack(pady=30)

root.mainloop()
