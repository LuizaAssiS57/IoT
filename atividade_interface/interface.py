import customtkinter as ctk
ctk.set_appearance_mode("dark")


# Funções --------------------
def calcular():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(preco.get())
    
    formula = (d / c) * p
    
    resultado.configure(text=f"O valor para a viagem é de R$ {formula:.2f}")
# ----------------------------

#Janela ----------------------

janela = ctk.CTk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("Cauculadora de Viagem")
janela.iconbitmap("atividade_interface/journey_road_street_asph_highway_icon_226304.ico")

# -----------------------------

# Corpo da janela -------------
titulo = ctk.CTkLabel(janela,
                    text= "APP DE VIAGEM",
                    text_color="#ffffff",
                    font=("verdana", 35, "bold"))
titulo.pack(pady=10)


distancia = ctk.CTkEntry(janela,
                        width= 300,
                        height= 40,
                        border_color= "#ffffff",
                        placeholder_text= "Digite a distância da viagem em KM")
distancia.pack(pady= 30)


consumo = ctk.CTkEntry(janela,
                        width= 300,
                        height= 40,
                        border_color= "#ffffff",
                        placeholder_text= "Digite o consumo do seu veiculo")
consumo.pack()


preco = ctk.CTkEntry(janela,
                        width= 300,
                        height= 40,
                        border_color= "#ffffff",
                        placeholder_text= "Digite o preço atual do combustivel")
preco.pack(pady= 30)


botao = ctk.CTkButton(janela,
                    width=200,
                    height= 40,
                    text= "Calcular Gasto",
                    fg_color="#FFDDDD",
                    text_color="#000000",
                    cursor= "hand2",
                    font=("arial", 15),
                    border_color= "#F51D1D",
                    border_width=2,
                    command= calcular)
botao.pack(pady= 5)


resultado = ctk.CTkLabel(janela,
                        text="",
                        text_color= "#ffffff",
                        font= ("arial", 20))
resultado.pack(pady=10)


janela.mainloop()