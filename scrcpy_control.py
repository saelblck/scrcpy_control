# feito por: samuel A. @saelblck
# data: 12/001/2024

import tkinter as tk
import subprocess

def executar_comando(comando):
    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, resultado)
        texto_resultado.config(state=tk.DISABLED)
    except subprocess.CalledProcessError as e:
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, f"Erro ao executar o comando: {e}")
        texto_resultado.config(state=tk.DISABLED)

# Funções para executar comandos específicos
def comando_1():
    executar_comando("scrcpy -d -w --power-off-on-close")

def comando_2():
    executar_comando("scrcpy -e -w --power-off-on-close")

def comando_3():
    executar_comando("scrcpy -S -d -w --power-off-on-close")

def comando_4():
    executar_comando("scrcpy -S -e -w --power-off-on-close")
    
def comando_5():
    executar_comando("sudo snap install scrcpy")

def comando_6():
    executar_comando("sudo apt install scrcpy")

def comando_7():
    executar_comando("scrcpy --tcpip")

# Configuração da interface gráfica
app = tk.Tk()
app.title("SCRCPY control @saelblck")

# Botões
btn1 = tk.Button(app, text="iniciar (cabo)", command=comando_1)
btn1.pack(pady=5)

btn2 = tk.Button(app, text="iniciar (wi-fi)", command=comando_2)
btn2.pack(pady=5)

btn7 = tk.Button(app, text="reiniciar (wi-fi)", command=comando_7)
btn7.pack(pady=5)

btn3 = tk.Button(app, text="iniciar (cabo/tela apagada)", command=comando_3)
btn3.pack(pady=5)

btn4 = tk.Button(app, text="iniciar (wi-fi/tela apagada)", command=comando_4)
btn4.pack(pady=5)

btn5 = tk.Button(app, text="instalar scrcpy (snap)", command=comando_5)
btn5.pack(pady=5)

btn6 = tk.Button(app, text="instalar scrcpy (apt)", command=comando_6)
btn6.pack(pady=5)
# Resultado
texto_resultado = tk.Text(app, height=10, width=50, state=tk.DISABLED)
texto_resultado.pack(pady=10)

# Iniciar a interface gráfica
app.mainloop()