import tkinter as tk
from tkinter import font

class TimerApp: # Erstellt eine Klasse mit dem Namen TimerApp
    def __init__(self, root): # Erstellt eine Funktion mit dem Namen __init__ und den Parametern self und root

        # Setzt das Layout des Fensters   
        root.geometry("1440x900")           # Setzt die Größe des Fensters auf 1440x900 Pixel 
        root.configure(background='black')  # Setzt den Hintergrund des Fensters (root) auf schwarz 
        root.attributes('-fullscreen', True)
        self.font = font.Font(family="Helvetica", size=500) # Setzt die Schriftart auf Helvetica und die Schriftgröße auf 500 Pixel
        self.timer_label = tk.Label(root, text="00:00", fg="red", bg="black", font=self.font) # Erstellt ein Label mit dem Text "00:00" und der Schriftfarbe rot und dem Hintergrund schwarz und der Schriftart Helvetica und der Schriftgröße 500 Pixel 
        self.timer_label.pack(fill='both', expand=True) # Packt das Label in das Fenster (root) ein und zentriert es automatisch in der Mitte des Fensters (root) 


        # Definiert die Timer-Funktionen
        self.root = root                    # Setzt die Variable root auf das Fenster (root) 
        self.root.title("Timer App")        # Setzt den Titel des Fensters auf "Timer App" 
        self.remaining_time = 0             # Setzt die Variable remaining_time auf 0
        self.is_paused = True               # Setzt die Variable is_paused auf True


        #shot_clock_24_button = tk.Button(root, text="24 Sekunden Shot Clock", command=lambda: self.start_timer(24))
        #shot_clock_24_button.pack()

        #shot_clock_14_button = tk.Button(root, text="14 Sekunden Shot Clock", command=lambda: self.start_timer(14))
        #shot_clock_14_button.pack()

        # Bindet die Tasten an Funktionen
        self.root.bind("<space>", self.toggle_timer)
        self.update_clock()

        root.bind("1", lambda event: self.set_timer(24))
        root.bind("2", lambda event: self.set_timer(14))
        root.bind("3", self.decrese_timer)
        root.bind("4", self.increase_timer)

    # Definiert die Funktion zum Setzen des Timers
    def set_timer(self, seconds):
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
        self.root.after(100, self.update_clock)

    # Abschnitt: Timer-Label aktualisieren
    def update_timer_label(self):
        secs, tenths = divmod(self.remaining_time, 1)
        time_format = '{:02d}:{:01d}'.format(int(secs), int(tenths * 10))
        self.timer_label.config(text=time_format)




if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.bind("1", lambda event: app.set_timer(24))
    root.mainloop()

