import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk

ctk.set_appearance_mode('dark')

#janela ----------------------
janela = ctk.CTk()
janela.geometry('400x500')
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
titulo = ctk.CTkLabel(janela, text= 'Sistema Gerador de QrCode', text_color= "#FFFFFF", font= ('Arial', 30))
titulo.pack(pady = 10)

entrada = ctk.CTkEntry(janela, width= 300, height= 40, placeholder_text='Digite a URL ou o PIX', border_color= "#FFFFFF")
entrada.pack(pady = 10)

botao = ctk.CTkButton(janela, width= 100, height= 20, fg_color= "#FFFFFF", text='GERAR QRCODE', text_color= 'black', hover_color= "#A7A1A1", cursor= 'hand2', command= gerar_qrcode)
botao.pack()

resultado = ctk.CTkLabel(janela, text= '')
resultado.pack(pady= 20)

janela.mainloop()