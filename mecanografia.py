'''
La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir palabras
un conjunto de palabras, las cuales son tienen como máximo 8 letras, aleatorias en un minuto,
presiona el botón enter para pasar a la siguiente palabra. Si la palabra es incorrecta, 
el programa te lo indicará y cambiará de palabra. Al finalizar el minuto, el programa te mostrará 
el total de palabras escritas correctamente.
'''

import tkinter as tk
from tkinter import messagebox
import random
import time

# Lista de palabras comunes
palabras = ['hola', 'adios', 'casa', 'perro', 'gato', 'raton', 'libro', 'lapiz', 'rojo', 'azul', 'verde', 'amar',
            'manzana', 'pera', 'platano', 'naranja', 'limon', 'uva', 'fresa', 'sandia', 'papaya', 'mango', 'piña',
            'pina', 'melon', 'aguacate', 'coco', 'kiwi', 'ciruela', 'durazno', 'guayaba', 'mamey', 'nuez','almendra', 
            'pistache', 'avellana', 'chocolate', 'vainilla', 'fresa', 'caramelo', 'canela', 'menta', 'limonada',
            'jamaica', 'cafe', 'te', 'leche', 'agua', 'refresco', 'jugo', 'cerveza', 'vino', 'whisky', 'ron', 'tequila', 
            'mezcal', 'pulque', 'sotol', 'bacanora', 'charanda', 'cachaza', 'pisco','absenta', 'anis', 'sambuca', 'ouzo', 
            'raki', 'pastis', 'arak', 'oum', 'mescal', 'rakia', 'cidra', 'sidra', 'chicha', 'pomada', 'sake', 'soju',
            'desde', 'hasta', 'para', 'por', 'sin', 'sobre', 'tras', 'durante', 'mediante', 'excepto', 'salvo', 'incluso',
            'mas', 'menos', 'mejor', 'peor', 'mayor', 'menor', 'tan', 'tanto', 'bastante', 'demasiado', 'muy', 'poco',
            'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'este', 'esta', 'estos', 'estas', 'ese', 'esa', 'esos',
            'esas', 'aquel', 'aquella', 'aquellos', 'aquellas', 'mi', 'mis', 'tu', 'tus', 'su', 'sus', 'nuestro', 'nuestra',
            'monitor', 'teclado', 'disco', 'duro', 'video', 'ram', 'red', 'usb']

# Función para iniciar el juego
def iniciarJuego(event=None):
    global palabras, palabra, tiempo_inicial, total_palabras, palabras_correctas
    ventana.unbind('<Return>')
    entrada_palabra.config(state='normal')
    entrada_palabra.bind('<Return>', verificarPalabra)
    palabra = random.choice(palabras)
    palabra_label.config(text=palabra)
    tiempo_inicial = time.time()
    total_palabras = 0
    palabras_correctas = 0
    total_palabras_label.config(text='Total de palabras: 0')
    palabras_correctas_label.config(text='Palabras correctas: 0')
    entrada_palabra.delete(0, tk.END)
    entrada_palabra.focus()
    
# Función para verificar la palabra
def verificarPalabra(event):
    global palabras, palabra, tiempo_inicial, total_palabras, palabras_correctas
    total_palabras += 1
    total_palabras_label.config(text='Total de palabras: ' + str(total_palabras))
    if entrada_palabra.get() == palabra:
        palabras_correctas += 1
        palabras_correctas_label.config(text='Palabras correctas: ' + str(palabras_correctas))
        palabra = random.choice(palabras)
        palabra_label.config(text=palabra)
        entrada_palabra.delete(0, tk.END)
    else:
        messagebox.showerror('Error', 'La palabra es incorrecta')
        palabra = random.choice(palabras)
        palabra_label.config(text=palabra)
        entrada_palabra.delete(0, tk.END)
        entrada_palabra.focus()
    
    if time.time() - tiempo_inicial >= 60:
        messagebox.showinfo('Fin del juego', 'El tiempo ha terminado')
        entrada_palabra.delete(0, tk.END)
        entrada_palabra.unbind('<Return>')
        entrada_palabra.config(state='disabled')
        ventana.bind('<Return>', iniciarJuego)
        palabra_label.config(text='')
        tiempo_inicial = 0
        total_palabras = 0
        palabras_correctas = 0
        
# Crear la ventana
ventana = tk.Tk()
ventana.title('Mecanografía')
ventana.geometry('800x600')
ventana.resizable(False, False)

# Etiqueta de instrucciones
instrucciones_label = tk.Label(ventana, text='Escribe la palabra y presiona enter', font=('Arial', 20))
instrucciones_label.pack(pady=20)

# Etiqueta de la palabra
palabra_label = tk.Label(ventana, text='', font=('Arial', 40))
palabra_label.pack(pady=20)

# Etiqueta del total de palabras
total_palabras_label = tk.Label(ventana, text='Total de palabras: 0', font=('Arial', 20))
total_palabras_label.pack(pady=20)

# Etiqueta de palabras correctas
palabras_correctas_label = tk.Label(ventana, text='Palabras correctas: 0', font=('Arial', 20))
palabras_correctas_label.pack(pady=20)

# Campo de entrada
entrada_palabra = tk.Entry(ventana, font=('Arial', 20))
entrada_palabra.pack(pady=20)
entrada_palabra.bind('<Return>', verificarPalabra)
entrada_palabra.config(state='disabled')

# Botón de inicio
iniciar_button = tk.Button(ventana, text='Iniciar', font=('Arial', 20), command=iniciarJuego)
iniciar_button.pack(pady=20)
ventana.bind('<Return>', iniciarJuego)

# Mantener la ventana abierta
ventana.mainloop()