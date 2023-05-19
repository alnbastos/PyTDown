import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import ttk
from actions import Actions

class Application(ttk.Frame):
    actions = Actions()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.first_container()
        self.second_container()
        self.third_container()
        self.status_container()
        self.buttons_container()

    def first_container(self):
        container1 = ttk.Frame(padding=10)
        container1.grid()

        ttk.Label(container1, text="URL YouTube:").grid(column=0, row=0)
        self.url_youtube = ttk.Entry(container1)
        self.url_youtube.grid(column=1, row=0, ipadx=30, padx=2)

        ttk.Label(container1, text="iTag:").grid(column=2, row=0)
        self.itag = ttk.Entry(container1)
        self.itag.grid(column=3, row=0, ipadx=5, padx=2)


    def second_container(self):
        container = ttk.Frame(padding=10)
        container.grid()

        ttk.Label(container, text="Path to video:").grid(column=0, row=0)
        self.path_pc = ttk.Entry(container)
        self.path_pc.grid(column=1, row=0, ipadx=30, padx=2)

        # arquivo em 64pixels - https://www.flaticon.com/br/icones-gratis/pasta
        self.pasta = PhotoImage(file="resources\\armazenamento-de-arquivo.png")
        self.pasta = self.pasta.subsample(34)

        self.path_pc_button=ttk.Button(container, text="DEM", command=self.search_destination)
        self.path_pc_button.grid(column=2, row=0)
        self.path_pc_button.config(image=self.pasta)


    def third_container(self):
        container = ttk.Frame(padding=10)
        container.grid()

        ttk.Button(container, text="Enter", command=self.run_download).grid(column=3, row=0)
        ttk.Label(container, text='     ').grid(column=4, row=0)
        ttk.Button(container, text="Search iTag", command=self.show_itags).grid(column=5, row=0)


    def status_container(self):
        container = ttk.Frame(padding=10)
        container.grid()

        # TODO ajustar aqui
        if self.actions.status_download:
            ttk.Label(container, text='Download complete!').grid(column=0, row=1)


    def buttons_container(self):
        container = ttk.Frame(padding=10)
        container.grid()

        ttk.Button(container, text="Quit", command=root.destroy).grid(column=1, row=0)


    def search_destination(self):
        """ Folder path to save the video. """
        file_name = filedialog.askdirectory()
        app.path_pc.insert(tk.END, file_name)


    def run_download(self):
        return self.actions.download_video(self.url_youtube.get(), self.path_pc.get(), self.itag.get())
    
    def show_itags(self):
        return self.actions.get_and_show_itags(self.url_youtube.get())



root = tk.Tk()
app = Application(master=root)
app.app = app
app.mainloop()
