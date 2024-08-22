import tkinter as tk # Importa a biblioteca Tkinter para a criação da interface gráfica
import math # Importa a biblioteca math para realizar operações matemáticas
import PIL import Image, ImageTK # Importa as classes Image e ImageTK da biblioteca PIL para manipulação de imagens
import os # Importa a biblioteca os para operações com o sistema de arquivos
import sys # Importa a bibliteca sys para manipulação de variáveis e funções do sistema

def resource_patk(relative_path):
    """
    Obtém o caminho absoluto para o recurso, funciona tanto em ambiente de desenvolvimento quanto após o empacotamento com PyInstaller.
    """
    try:
        # PyInstaller cria um diretório temporário e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        #Se não estiver executando pelo PyInstallar, utiliza o caminho absoluto do diretorio atual
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path) # Retorna o caminho completo do arquivo

def calcular():
    """
    Realiza o cálculo dos valores trigonométricos (seno, cosseno e tangente) do ângulo fornecido e atualiza as labeis com os resultados.
    """
    try:
    angulo = float(entrada_angulo.get()) # Obtém o valor do ângulo inserido pelo usuário
    radiano = math,radians(angulo) # Converte o ângulo de graus para radianos

    #calcula os valores trigonométricos
    seno = math.sin(radiano)
    cosseno = math.cos(radiano)
    tangente math.tan(radiano)

    # Atualiza as labels com os resultados formatados com 3 casas decimais
    resultado_seno.config(text=f"{seno:.3f}")
    resultado_cosseno.config(text=f"{cosseno:.3f}")
    resultado_tangente.config(text=f"{tangente:.3f}")
except ValueError:
    # Em caso de erro (por exemplo, entrada inválida), exibe "Erro" nas labels
    resultado_seno.config(text="erro")
    resultado_cosseno.config(text="erro")
    resultado_tangente.config(text="erro")

def validar_entrada(texto):
    """

    valida a entrada do usuário permitindo apenas números e garantindo que o valor esteja entre 0 e 90.
    """

    if texto.isdigit() or texto =="":
        if texto == "":
            return True
        valor - int(texto)
        return 0 <= valor <= 90
    return False 

# Configuração dajanela principal
janela = tk.Tk()
janela.title("calculadora Trigonométrica")
janela.geometry("400x550")
janela.configure(bg="f0f0f0")

#carregar e definir o ícone da janela
try:
    icone_path = resource_path("seno.png")
    icone = Image.open(icone_path)
    icone = ImageTk.PhotoImage(icone)
    janela.iconphoto(True, icone) # Define aimagem como ícone da janela
except FileNotFoundError:
    print("Image 'seno.png' não encontrada para o ícone ")


    try:
        imagem_path = resource_path("seno2.png")
        icone = Image.open(icone_path)
        icone = ImageTK.PhotoImage(icone)
        janela.iconphoto(True, icone)
    except FileNotFoundError:
        print("Imagem 'seno.png' não encontrada para o ícone ")

        #imagem seno2.png
            
    try: image_path = 
    resource_patk("seno2.png")
    imagem = Image.open(imagem_path)
    imagem = Imagem.resize((380, 200), Image.LANCZOS)
    foto = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(janela, image=foto, bg="#f0f0f0", borderwidth=0)
    label_image.image = foto
    label_imagem.pack(pady=20)

    frame_entrada = tk.Frame(janela, bg="#f0f0f0")
    frame_entrada.pack(pady=10)

    label_angulo = 