from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        container1 = ttk.Frame(padding=10)
        container1.grid()

        container2 = ttk.Frame(padding=10)
        container2.grid()
        
        container3 = ttk.Frame(padding=10)
        container3.grid()

        container_buttons = ttk.Frame(padding=10)
        container_buttons.grid()

        tk.Label(container1, text="URL YouTube:").grid(column=0, row=0)
        self.url_youtube = tk.Entry(container1)
        self.url_youtube.grid(column=1, row=0)

        tk.Label(container1, text="ITag:").grid(column=2, row=0)
        self.itag = tk.Entry(container1)
        self.itag.grid(column=3, row=0)

        tk.Label(container2, text="Destino Vídeo:").grid(column=0, row=0)
        self.path_pc = tk.Entry(container2)
        self.path_pc.grid(column=1, row=0)

        # arquivo em 64pixels - https://www.flaticon.com/br/icones-gratis/pasta
        self.pasta= PhotoImage(file="resources\\armazenamento-de-arquivo.png")
        self.pasta=self.pasta.subsample(34)

        self.path_pc_button=tk.Button(container2, text="DEM", command=search_destination)
        self.path_pc_button.grid(column=2, row=0)
        self.path_pc_button.config(image=self.pasta)

        self.run_download_button = tk.Button(container3, text="Enter", command=self.run_download).grid(column=1, row=0)

        # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    def run_download(self):
        print(self.url_youtube.get(), self.path_pc.get(), self.itag.get())

def search_destination():
    app.path_pc.delete("0", "end")
    file_name = filedialog.askdirectory()
    app.path_pc.insert(tk.END, file_name)

def download_video(url_youtube, pc_path, itag):
    # selecionando qual itag desejo
    yt = YouTube(url_youtube).streams.get_by_itag(itag)
    yt.download(pc_path)
    print('DOWNLOAD REALIZADO')

def check_itag(url_youtube):
    #verifica as itag disponiveis
    yt = YouTube(url_youtube).streams.filter(file_extension='mp4')

    for linha in yt:
        print(linha)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
