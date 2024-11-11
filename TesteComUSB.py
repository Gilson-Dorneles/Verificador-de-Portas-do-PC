import tkinter as tk
from tkinter import Listbox
import usb.core
import usb.util
import serial.tools.list_ports


def verificar_comunicacao():
    # Limpar a lista existente
    listbox.delete(0, tk.END)

    # Obter todos os dispositivos USB conectados
    try:
        dispositivos_usb = usb.core.find(find_all=True)
        if dispositivos_usb:
            for dispositivo in dispositivos_usb:
                try:
                    fabricante = usb.util.get_string(
                        dispositivo, dispositivo.iManufacturer
                    )
                    produto = usb.util.get_string(dispositivo, dispositivo.iProduct)
                    listbox.insert(
                        tk.END,
                        f"USB: {fabricante} - {produto} (ID: {hex(dispositivo.idVendor)}:{hex(dispositivo.idProduct)})",
                    )
                except Exception as e:
                    listbox.insert(tk.END, f"USB: Erro ao obter informações - {e}")
        else:
            listbox.insert(tk.END, "Nenhum dispositivo USB encontrado")
    except usb.core.NoBackendError as e:
        listbox.insert(tk.END, f"Erro de backend USB: {e}")

    # Obter todas as portas COM (seriais) disponíveis
    portas_com = serial.tools.list_ports.comports()
    if portas_com:
        for porta in portas_com:
            listbox.insert(tk.END, f"COM: {porta.device} - {porta.description}")
    else:
        listbox.insert(tk.END, "Nenhuma porta COM encontrada")


# Criação da janela principal
root = tk.Tk()
root.title("Verificador de Comunicação")
root.geometry("300x300")
root.resizable(True, True)  # Permitir redimensionar a janela

# Criação do botão
verificar_button = tk.Button(
    root, text="Verificar Comunicação", command=verificar_comunicacao
)
verificar_button.pack(pady=10)

# Criação da lista, que será redimensionável
listbox = Listbox(root)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Inicia o loop da interface gráfica
root.mainloop()
