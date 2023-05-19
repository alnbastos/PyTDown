from pytube import YouTube
import tkinter as tk
# from pyTDown import Application

class Actions:
    def __init__(self):
        self.status_download = False

    def get_and_show_itags(self, url_youtube:str):
        list_itags = self.check_itag(url_youtube)

        new_window = tk.Toplevel(padx=40, pady=40)
        new_window.title('Show iTags from URL')
        new_window.grid()

        label_show_itags = tk.Label(new_window, text="Show iTags")
        label_show_itags.grid(row=1, column=0 )

        show_itags = tk.Listbox(new_window)
        show_itags.grid(row=2, column=0, ipadx=300)

        # insert itag data into listbox
        for index, value in enumerate(list_itags):
            show_itags.insert(index, value)

        back_button = tk.Button(new_window, text = 'Voltar', command=new_window.destroy)
        back_button.grid(row=3, column=0)

    
    def check_itag(self, url_youtube:str) -> list:
        """ Check available tags. """
        return YouTube(url_youtube).streams.filter(file_extension='mp4')


    def download_video(self, url_youtube:str, pc_path:str, itag:int):
        """ Select video by a specific itag. """
        yt = YouTube(url_youtube).streams.get_by_itag(itag)
        yt.download(pc_path)
        self.status_download = True


# https://www.youtube.com/watch?v=uW0ZSvBphi0
