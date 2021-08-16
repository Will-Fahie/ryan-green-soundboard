import tkinter as tk
import pygame


def play(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


window = tk.Tk()
window.geometry("300x500")
window.title("Ryan Green Soundboard")


filename = tk.PhotoImage(file="images/ryan_image.png")
background_image = tk.Label(window, image=filename)
background_image.place(x=-40, y=170)

title_label = tk.Label(window, text="Ryan Green Soundboard", font=("bahnschrift", 18))
title_label.pack(pady=10)

quiet_no_button = tk.Button(window, text="No.", command=lambda: play("sound_files/no_quiet.mp3"), width=20, font=("bahnschrift", 12), bg="#3399ff")
quiet_no_button.pack()

loud_no_button = tk.Button(window, text="NO!", command=lambda: play("sound_files/no_loud.mp3"), width=20, font=("bahnschrift", 12), bg="#ff5050")
loud_no_button.pack()

monkey_button = tk.Button(window, text="monkeh", command=lambda: play("sound_files/monkey.mp3"), width=20, font=("bahnschrift", 12), bg="#ffcc00")
monkey_button.pack()

german_button = tk.Button(window, text="Das war ein befehl!", command=lambda: play("sound_files/german.mp3"), width=20, font=("bahnschrift", 12), bg="#669900")
german_button.pack()

swine_button = tk.Button(window, text="swine", command=lambda: play("sound_files/swine.mp3"), width=20, font=("bahnschrift", 12), bg="#009999")
swine_button.pack()


window.mainloop()

