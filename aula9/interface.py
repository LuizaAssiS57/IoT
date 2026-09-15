import customtkinter as ctk
ctk.set_appearance_mode("dark")

#janela ------------

janela = ctk.CTk()
janela.geometry("500x300")
janela.resizable(False, False)
janela.title("SISTEMA DE ACESSO - 2026")
janela.iconbitmap("aula9/security-protection-protect-key-password-login_108554.ico")

#----------------------------

# corpo da janela -----------
titulo = ctk.CTkLabel(janela,
                      text= "SISTEMA DE LOGIN",
                      text_color= "#97f577",
                      font=("arial", 35))
titulo.pack()


login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="#97f577",
                     placeholder_text="Digite seu login")
login.pack(pady=30)


senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color="#97f577",
                     placeholder_text="Digite sua senha",
                     show="•")
senha.pack()


botao = ctk.CTkButton(janela,
                      width= 200,
                      height=40,
                      text="ACESSAR",
                      fg_color= "#97f577",
                      text_color= "#ffffff",
                      cursor= "heart",
                      font=("arial", 30))
botao.pack(pady=30)


janela.mainloop()