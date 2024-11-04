import tkinter as tk

def clasificacionSignoZodiaco(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    else:
        return "Fecha no válida"

def calcularSigno():
    try:
        dia = int(entryDia.get())
        mes = int(entryMes.get())
        
        signo = clasificacionSignoZodiaco(dia, mes)
        rptaLabel.config(text=f"Su signo del zodiaco es: {signo}")
        errorLabel.config(text="", fg="red")  
    except ValueError:
        errorLabel.config(text="Por favor, ingrese números válidos.", fg="red")
        rptaLabel.config(text="")  

# Crea ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")
ventana.geometry("400x400")

# Título
tituloLabel = tk.Label(ventana, text="Cálculo de Signo Zodiacal", font=("Arial", 16))
tituloLabel.pack(pady=10)

# Entradas día y mes
tk.Label(ventana, text="Día de nacimiento (1-31):").pack(pady=5)
entryDia = tk.Entry(ventana)
entryDia.pack(pady=5)

tk.Label(ventana, text="Mes de nacimiento (1-12):").pack(pady=5)
entryMes = tk.Entry(ventana)
entryMes.pack(pady=5)

# Botón calcular signo zodiacal
btnCalcular = tk.Button(ventana, text="Calcular Signo", command=calcularSigno)
btnCalcular.pack(pady=10)

# Label mostrar resultado
rptaLabel = tk.Label(ventana, text="", justify="center")
rptaLabel.pack(pady=10)

# Label mostrar mensajes de error
errorLabel = tk.Label(ventana, text="", justify="center")
errorLabel.pack(pady=10)

# Label mostrar el autor 
autorLabel = tk.Label(ventana, text="Autor: Leonel Coyla Idme", font=("Arial", 10), fg="#D3D3D3")  # Gris claro
autorLabel.pack(side=tk.BOTTOM, pady=5)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
