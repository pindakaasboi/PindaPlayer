import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import pygame
import time

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("PindaPlayer")
        self.master.geometry("330x400")
        self.master.resizable(False, False)
        self.master.configure(bg="#3b3b3b")  # Set background color
        
        self.play_button = tk.Button(self.master, text="LUISTEREN", command=self.play_music, width=10, bg="#b8b8b8", fg="#3b3b3b", font=("Segoe UI", 10, "bold"))
        self.play_button.grid(row=0, column=0, padx=10, pady=(10, 5))
        
        self.pause_button = tk.Button(self.master, text="Lunchtijd", command=self.pause_music, width=10, bg="#b8b8b8", fg="#3b3b3b", font=("Segoe UI", 10, "bold"))
        self.pause_button.grid(row=0, column=1, padx=10, pady=(10, 5))
        
        self.stop_button = tk.Button(self.master, text="KAPPEN!!", command=self.stop_music, width=10, bg="#b8b8b8", fg="#3b3b3b", font=("Segoe UI", 10, "bold"))
        self.stop_button.grid(row=0, column=2, padx=10, pady=(10, 5))
        
        self.load_button = tk.Button(self.master, text="Laad muziek die ik kan afspelen", command=self.load_music, bg="#b8b8b8", fg="#3b3b3b", font=("Segoe UI", 10, "bold"))
        self.load_button.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 5), sticky="ew")
        
        self.volume_label = tk.Label(self.master, text="AAA TE HARD / veel te zacht", bg="#3b3b3b", fg="white", font=("Segoe UI", 10))
        self.volume_label.grid(row=2, column=0, columnspan=3, pady=(0, 5))
        
        self.volume_slider = tk.Scale(self.master, from_=0, to=100, orient="horizontal", command=self.set_volume)
        self.volume_slider.set(50)  # Set initial volume to 50
        self.volume_slider.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="ew")
        
        self.progress_label = tk.Label(self.master, text="OMG HIER KAN JE ZIEN HOE VER JE BENT O:", bg="#3b3b3b", fg="white", font=("Segoe UI", 10))
        self.progress_label.grid(row=4, column=0, columnspan=3, pady=(0, 5))
        
        self.progress_bar = Progressbar(self.master, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.grid(row=5, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="ew")
        
        self.music_file = None
        self.music_loaded = False
        
        pygame.mixer.init()
        
    def play_music(self):
        if self.music_loaded:
            pygame.mixer.music.unpause()
            self.update_progress_bar()
        elif self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.music_loaded = True
            self.update_progress_bar()
        
    def pause_music(self):
        pygame.mixer.music.pause()
        
    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_loaded = False
        self.progress_bar.stop()
        
    def load_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.music_file:
            self.music_loaded = False
    
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(int(volume) / 100)
        
    def update_progress_bar(self):
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            if not pygame.mixer.music.get_busy():
                break
            current_time = pygame.mixer.music.get_pos() / 1000
            song_length = pygame.mixer.Sound(self.music_file).get_length()
            progress = (current_time / song_length) * 100
            self.progress_bar['value'] = progress
            self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
