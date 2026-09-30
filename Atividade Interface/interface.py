import customtkinter as ctk
ctk.set_appearance_mode("dark")

# FUNÇÕES -------------------
def media():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())
    
    try:
        mediaFinal = (n1 + n2 + n3) / 3
        
        if (mediaFinal >= 5):
            media.configure(text=f"Aprovado! Sua média é {mediaFinal:.2f}", text_color="green")
        else:
            media.configure(text=f"Recuperação! Sua média é {mediaFinal:.2f}", text_color="red")
    
    except:
        media.configure(text="Dado inválido!")

# ---------------------------
# JANELA --------------------

janela = ctk.CTk()
janela.geometry("600x500")
janela.resizable(False, False)
janela.title("Sistema Escolar 2026")
# ---------------------------

# CORPO DA JANELA -----------

titulo = ctk.CTkLabel(janela,
                    text= "Sistema Escola",
                    text_color="#f8da32",
                    font=("arial", 50, "bold"))
titulo.pack(pady=10)

nota1 = ctk.CTkEntry(janela,
                    width= 300,
                    height= 40,
                    border_color= "#f8da32",
                    placeholder_text= "Digite a sua nota da 1ª Unidade")
nota1.pack(pady=30)

nota2 = ctk.CTkEntry(janela,
                    width= 300,
                    height= 40,
                    border_color= "#f8da32",
                    placeholder_text= "Digite a sua nota da 2ª Unidade")
nota2.pack()

nota3 = ctk.CTkEntry(janela,
                    width= 300,
                    height= 40,
                    border_color= "#f8da32",
                    placeholder_text= "Digite a sua nota da 3ª Unidade")
nota3.pack(pady=30)

botao = ctk.CTkButton(janela,
                    width=200,
                    height= 40,
                    text= "Resultado",
                    fg_color="#f8da32",
                    text_color="#000000",
                    cursor= "hand2",
                    font=("arial", 15),
                    command= media)
botao.pack(pady= 5)

media = ctk.CTkLabel(janela,
                    text="",
                    text_color= "#ffffff",
                    font= ("arial", 20))
media.pack(pady=10)

janela.mainloop()
# ---------------------------