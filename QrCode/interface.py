import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk

ctk.set_appearance_mode('dark')

#janela ----------------------
janela = ctk.CTk()
janela.geometry('400x520')
janela.title('SISTEMA GERARDOR DE QRCODE')
janela.resizable(False, False)
#-----------------------------

imagem_qr = None

def gerar_qrcode():
    global imagem_qr
    texto = entrada.get()
    
    if(texto != ''):
        qr = qrcode.make(texto)
        qr = qr.resize((300, 300))
        imagem_qr = ImageTk.PhotoImage(qr)
        resultado.configure(image = imagem_qr, text= '')
    else:
        resultado.configure(text= 'Digite um texto ou um PIX')

#Elementos da janela ---------
titulo = ctk.CTkLabel(janela, text='Gerador de QR Code', font=('Roboto', 24, 'bold'))
titulo.pack(pady = 10)

entrada = ctk.CTkEntry(janela, width=320, height=45, placeholder_text='Digite a URL ou o PIX...', font=('Roboto', 14), corner_radius=8)
entrada.pack(pady = 10)

botao = ctk.CTkButton(janela, text='GERAR QR CODE', width=320, height=45, font=('Roboto', 14, 'bold'), cursor='hand2', corner_radius=8, command=gerar_qrcode, fg_color= "#f896f8", hover_color="#f346f3")
botao.pack()

resultado = ctk.CTkLabel(janela, text= '')
resultado.pack(pady= 20)

janela.mainloop()