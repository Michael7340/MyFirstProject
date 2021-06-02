from pytube import YouTube
from playsound import playsound
import tkinter as tk

WINDOWS_WIDTH = 500
WINDOWS_HEIGHT = 150
WINDOWS_TITLE = "Youtbe Downloader"
BOTTOM_CLICK_SOUND = "click.m4a"

class YoutubeVideoDownloader():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WINDOWS_WIDTH,WINDOWS_HEIGHT))
        self.window.configure(bg= "#6495ED")
        self.window.title(WINDOWS_TITLE)

                              
        self.link_label = tk.Label(self.window, text = "Download Link")
        self.link_label.grid(column = 0,row = 0)
        self.name_label = tk.Label(self.window, text = "Save file as")
        self.name_label.grid(column = 0,row = 1)
        self.path_label = tk.Label(self.window, text = "Save file Path")
        self.path_label.grid(column = 0,row = 2)
        self.ext_label = tk.Label(self.window, text = "Save file Extension")
        self.ext_label.grid(column = 0, row = 3)

        self.link_entry = tk.Entry(master= self.window, width = 40)
        self.link_entry.grid(column = 1, row = 0)
        self.name_entry = tk.Entry(master= self.window, width = 40)
        self.name_entry.grid(column = 1, row = 1)
        self.path_entry = tk.Entry(master= self.window, width = 40)
        self.path_entry.grid(column = 1, row = 2)
        self.ext_entry = tk.Entry(master= self.window, width = 40)
        self.ext_entry.grid(column = 1, row = 3)

        self.download_button = tk.Button(self.window, text = "Download", command = self.__get_link)
        self.download_button.grid(column = 1, row = 4)

        return

    def __downloader(self, link, save_path = "", save_name = "", extension = "mp4"):
        yt = YouTube(link)
        yt_stream = yt.streams.filter(progressive = True, file_extension = extension).order_by('resolution').desc().first()
        yt_stream.download(output_path = save_path, filename = save_name)

        return
                                                                                               

    def __get_link(self):
        link = self.link_entry.get()
        path = self.path_entry.get()
        name = self.name_entry.get()
        ext = self.ext_entry.get()

    def run_app(self):
        self.window.mainloop()
        return

if __name__ == "__main__":
    app = YoutubeVideoDownloader()
    app.run_app()

                              
                              
