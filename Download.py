# Bibliotecas usadas

from tkinter import*
from tkinter import filedialog
import pytube
from pytube import YouTube

# Cores

CorEspecial = "#750709"
CorDeFundo = "#0D1016"
CorDeContraste = "#232931"
CorDaFonte = "#ffffff"

 # Fontes

FONTE = "Bahnschrift 20"

# Configuracoes da janela

Janela = Tk()
Janela.title('Youtube downlodader')
Janela.geometry('810x350')
Janela.resizable(width = FALSE, height= FALSE)
Janela.configure(bg = CorDeFundo)

# Importacao de icones para os botoes

busca = PhotoImage(file = 'F:\Importante\projetos\Python\VideoDownloader\Img\Pasta.png')

# Variaveis globais

stringDiretorio = StringVar()
caminho = str()

stringUrl = StringVar()
link = str()

# Acoes dos Botoes

def ondeSalvar():

    global caminho
    caminho = filedialog.askdirectory()
    stringDiretorio.set(caminho)

def baixarVideo():

    global link
    link = stringUrl.get()

    youtube = YouTube (link)
    dw = youtube.streams.filter ( progressive = True , file_extension = 'mp4' ) \
        .order_by ( 'resolution' ) \
        .desc () \
        .first () \
        .download (caminho, youtube.title)


# Criacao da interface


# Labels

lbl1 = Label(Janela, font = FONTE, text = "Prencha todos os  campos para criar o arquivo .MP4",
fg = CorDaFonte, bg = CorDeFundo).place(x = 15, y = 15)

lb2 = Label(Janela, font = FONTE, text = "Onde salvar:",
fg = CorDaFonte, bg = CorDeFundo).place(x = 15, y = 120)

lb3 = Label(Janela, font = FONTE, text = "URL do video:",
fg = CorDaFonte, bg = CorDeFundo).place(x = 15, y = 200)

# Campos de texto

et1 = Entry(Janela, font = FONTE, fg = CorDaFonte, bg = "#232931",
width = 30, textvariable = stringDiretorio, bd = 0).place(x = 230, y = 130)

et2 = Entry( Janela , font = FONTE , fg = CorDaFonte , bg = "#232931" ,
             textvariable = stringUrl , width = 38 , bd = 0 ).place( x = 230 , y = 200 )

# Botoes

Open = Button(Janela, image = busca, borderwidth = 0,  bg = CorEspecial,
bd = 0, command = ondeSalvar).place(x = 700, y = 128)

baixar = Button(Janela, text = "Baixar", fg = CorDaFonte, bg = CorEspecial,
font = FONTE, width = 52, bd = 0, command = baixarVideo).place(x = 15, y = 260)

Janela.mainloop()