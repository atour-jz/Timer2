import tkinter as tk
from tkinter import font
from PIL import *
from PIL import ImageTk, Image

class TimerApp: # Erstellt eine Klasse mit dem Namen TimerApp
    def __init__(self, root):
        self.root = root
        image = Image.open("/Users/arthur/Documents/Basketball/Augustdorf/Kampfgericht/Shotclock/Timer2/logo-vektor.png")

        # Ändern Sie die Größe des Bildes
        new_size = (700, 700)  # Setzen Sie die gewünschte Größe hier
        image = image.resize(new_size, Image.BICUBIC)

        self.logo = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(root, image=self.logo, bg="black")
        self.logo_label.pack(fill='both', expand=True)

        # Setzt das Layout des Fensters  
        self.font = font.Font(family="Helvetica", size=500) # Setzt die Schriftart auf Helvetica und die Schriftgröße auf 500 Pixel
        self.timer_label = tk.Label(root, text="00:00", fg="red", bg="black", font=self.font) # Initialisieren Sie self.timer_label hier

        # Setzt das Layout des Fensters  
        self.root.configure(background='black')  # Setzt den Hintergrund des Fensters (root) auf schwarz 
        self.timer_label.config(fg="red", bg="black")  # Ändert die Farben des Labels

        root.attributes('-fullscreen', True)

        # Definiert die Timer-Funktionen
        self.root = root                    # Setzt die Variable root auf das Fenster (root) 
        self.root.title("Timer App")        # Setzt den Titel des Fensters auf "Timer App" 
        self.remaining_time = 0             # Setzt die Variable remaining_time auf 0
        self.is_paused = True               # Setzt die Variable is_paused auf True

        # Bindet die Tasten an Funktionen
        self.root.bind("<space>", self.toggle_timer)
        self.update_clock()

        root.bind("1", lambda event: self.set_timer(24))
        root.bind("2", lambda event: self.set_timer(14))
        root.bind("3", self.decrese_timer)
        root.bind("4", self.increase_timer)

    # Definiert die Funktion zum Setzen des Timers
    def set_timer(self, seconds):
        self.logo_label.pack_forget()  # Fügen Sie diese Zeile hinzu, um das Logo zu entfernen
        self.timer_label.pack(fill='both', expand=True)
        self.remaining_time = seconds  # Setzt den Timer auf die gegebene Zeit
        self.update_timer_label()
        if not self.is_paused:
            self.start_timer(self.remaining_time)  # Startet den Timer wieder
    
    # Definiert die Funktion zum Umschalten des Timers
    def toggle_timer(self, event):
        self.is_paused = not self.is_paused 

    # Definiert die Funktion zum Verringern des Timers
    def decrese_timer(self, event):
        if self.is_paused and self.remaining_time > 0:
            self.remaining_time -= 1
            if self.remaining_time < 0:
                self.remaining_time = 0
            self.update_timer_label()
        
    # Definiert die Funktion zum Erhöhen des Timers
    def increase_timer(self, event): #
        if self.is_paused:
            self.remaining_time += 1
            self.update_timer_label()

    # Definiert die Methode zur Aktualisierung der Uhr
    def update_clock(self):
        if self.remaining_time > 0 and not self.is_paused:# and not self.minlabel:  # Überprüft, ob der Timer nicht pausiert ist
            self.remaining_time -= 0.1
            if self.remaining_time < 0:     # Überprüft, ob die Zeit abgelaufen ist
                self.remaining_time = 0     # Stellt sicher, dass die Zeit nicht negativ wird
            secs, tenths = divmod(self.remaining_time, 1) 
            time_format = '{:02d}:{:01d}'.format(int(secs), int(tenths * 10))
            self.timer_label.config(text=time_format)
            if self.remaining_time < 5:  # Verwenden Sie self.remaining_time statt remaining_time
                self.root.configure(background='red')  # Setzt den Hintergrund des Fensters (root) auf rot 
                self.timer_label.config(fg="black", bg="red")  # Ändert die Farben des Labels
            else:
                self.timer_label.config(fg="red", bg="black")
        
        self.root.after(100, self.update_clock)

        #if self.remaining_time <= 5:
         #   self.root.configure(background='red')  # Setzt den Hintergrund des Fensters (root) auf rot 
          #  self.timer_label.config(fg="black", bg="red")  # Ändert die Farben des Labels

    # Abschnitt: Timer-Label aktualisieren
    def update_timer_label(self):
        secs, tenths = divmod(self.remaining_time, 1)
        time_format = '{:02d}:{:01d}'.format(int(secs), int(tenths * 10))
        self.timer_label.config(text=time_format)
    
    def start_timer(self):
        self.is_paused = False

class SideScreen:
    def __init__(self, root, timer_app):
        self.root = root
        self.timer_app = timer_app
        self.font = font.Font(family="Helvetica", size=200)
        self.timer_label = tk.Label(root, text="00:00", fg="red", bg="black", font=self.font)
        self.timer_label.pack(fill='both', expand=True)
        self.root.configure(background='black')
        self.root.attributes('-fullscreen', True)
        self.update_clock()

    def update_clock(self):
        secs, tenths = divmod(self.timer_app.remaining_time, 1)
        time_format = '{:01d}:{:02d}'.format(int(secs) // 60, int(secs) % 60)
        self.timer_label.config(text=time_format)
        self.root.after(100, self.update_clock)

class StartScreen:
    def __init__(self, root, timer_app):
        self.root = root
        self.timer_app = timer_app
        self.start_3min_button = tk.Button(root, text="Start 3-Minuten-Timer", command=self.start_3min_timer)
        self.start_3min_button.pack()
        self.start_24sec_button = tk.Button(root, text="Start 24-Sekunden-Timer", command=self.start_24sec_timer)
        self.start_24sec_button.pack()

    def start_3min_timer(self):
        self.timer_app.set_timer(180)
        self.root.destroy()
        self.timer_app.start_timer()  # Startet den Timer
        self.timer_app.root.deiconify()  # Zeigt das Hauptfenster wieder an
        side_root = tk.Toplevel(self.timer_app.root)
        side_screen = SideScreen(side_root, self.timer_app)  # Erstellt den Nebenbildschirm

    def start_24sec_timer(self):
        self.timer_app.set_timer(24)
        self.root.destroy()
        self.timer_app.root.deiconify()  # Zeigt das Hauptfenster wieder an

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    start_root = tk.Toplevel(root)
    start_screen = StartScreen(start_root, timer_app)
    side_root = tk.Toplevel(root)
    side_screen = SideScreen(side_root, timer_app)
    root.withdraw()
    root.mainloop()