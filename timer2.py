import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess



class TimerApp: # Erstellt eine Klasse mit dem Namen TimerApp
    def __init__(self, root):
        self.root = root
        image = Image.open("logo-vektor.png")  # Use image file name if it's in the same directory
        self.alarm_process = None

        # Ändern Sie die Größe des Bildes
        new_size = (700, 700)  # Setzen Sie die gewünschte Größe hier
        image = image.resize(new_size, Image.BICUBIC)

        self.logo = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(root, image=self.logo, bg="black")
        self.logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # Positioniert das Logo in der Mitte

        # Setzt das Layout des Fensters
        root.geometry("1440x900")           # Setzt die Größe des Fensters auf 1440x900 Pixel 
        root.configure(background='black')  # Setzt den Hintergrund des Fensters (root) auf schwarz 
        root.attributes('-fullscreen', True)


        self.font = font.Font(family="Helvetica", size=700) # Setzt die Schriftart auf Helvetica und die Schriftgröße auf 500 Pixel
        self.timer_label = tk.Label(root, text="00:00", fg="red", bg="black", font=self.font) # Erstellt ein Label mit dem Text "00:00" und der Schriftfarbe rot und dem Hintergrund schwarz und der Schriftart Helvetica und der Schriftgröße 500 Pixel 
        self.timer_label.pack(fill='both', expand=True) # Packt das Label in das Fenster (root) ein und zentriert es automatisch in der Mitte des Fensters (root) 
        self.timer_label.pack_forget()  # Versteckt den Timer zu Beginn

        #Timer Funktionen 
        self.root = root                    # Setzt die Variable root auf das Fenster (root) 
        self.root.title("Timer App")        # Setzt den Titel des Fensters auf "Timer App" 

        self.remaining_time = 0             # Setzt die Variable remaining_time auf 0
        self.is_paused = True               # Setzt die Variable is_paused auf True

        #Key Bindings
        self.root.bind("<space>", self.toggle_timer)
        self.update_clock()

        root.bind("1", lambda event: self.set_timer(24))
        root.bind("2", lambda event: self.set_timer(14))
        root.bind("6", lambda event: self.set_timer(60))
        root.bind("3", self.decrese_timer)
        root.bind("4", self.increase_timer)
        root.bind("7", lambda event: self.set_timer(999))
        
        
    def play_alarm(self):
        if self.alarm_process is not None:
            self.alarm_process.terminate()  # Beendet einen bereits laufenden Alarm
        self.alarm_process = subprocess.Popen(['afplay', 'Basketball_Buzzer_lang.wav'])

    def stop_alarm(self):
        if self.alarm_process is not None:
            self.alarm_process.terminate()
            self.alarm_process = None

    def adjust_colors(self):
        if self.remaining_time >= 800:
            # Setzt sowohl Schriftfarbe als auch Hintergrundfarbe auf Schwarz
            self.timer_label.config(fg="black", bg="black")
            self.logo_label.pack_forget()
        elif self.remaining_time < 5:
            self.timer_label.config(fg="black", bg="red")
        else:
            self.timer_label.config(fg="red", bg="black")


    def set_timer(self, seconds):
        self.stop_alarm()  # Stoppt den Alarm, wenn "1" oder "2" gedrückt wird
        self.logo_label.pack_forget()
        self.timer_label.pack(fill='both', expand=True)
        self.remaining_time = seconds
        self.adjust_colors()
        self.update_timer_label()
        if not self.is_paused:
            # Wenn der Timer läuft, wird er direkt neu gestartet
            self.is_paused = False
        else:
            # Wenn der Timer pausiert ist, wird er nur eingestellt, aber nicht gestartet
            self.is_paused = True

    
    def toggle_timer(self, event):
        self.is_paused = not self.is_paused

    def decrese_timer(self, event):
        if self.is_paused and self.remaining_time > 0:
            self.remaining_time -= 1
            if self.remaining_time < 0:
                self.remaining_time = 0
            self.update_timer_label()

    def increase_timer(self, event):
        if self.is_paused:
            self.remaining_time += 1
            self.update_timer_label()
            

    def update_timer_label(self):
        secs, tenths = divmod(self.remaining_time, 1)
        time_format = '{:02d}.{:01d}'.format(int(secs), int(tenths * 10))
        self.timer_label.config(text=time_format)
        self.adjust_colors()

    def start_alarm(self):
#        if self.remaining_time <= 0:
        self.play_alarm()  # Spielt den Alarm ab, wenn der Timer abgelaufen ist

    def update_clock(self):
        if self.remaining_time > 0 and not self.is_paused:
            self.remaining_time -= 0.1
            if self.remaining_time <= 0:
                self.remaining_time = 0
                self.is_paused = True
                self.start_alarm()

        self.update_timer_label()
        self.root.after(100, self.update_clock)
                    


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
