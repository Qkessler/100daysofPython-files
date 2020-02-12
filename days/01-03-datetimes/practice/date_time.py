from Tkinter import Tk, Label, Button, StringVar
from datetime import timedelta
from time import sleep

DEFAULT = timedelta(minutes=25)


class Ventana:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")
        master.geometry("800x700+350+100")
        self.botonSaludar = Button(master, text="Saludar",
                                   command=self.saludar)
        self.botonSaludar.pack()
        self.botonStart = Button(master, text="Start",
                                 command=self.pomodoro_timer)
        self.botonStart.pack()

        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
        self.miLabel = Label(master, text="Hola que tal", font=('times', 10),
                             fg='black', bg='white', width=50, height=5)
        self.miLabel.place(x=200, y=100)

    def pomodoro_timer(self):
        initial = timedelta(seconds=0)
        time = DEFAULT
        while time > initial:
            sleep(1)
            time -= timedelta(seconds=1)
            print(time)
            initial += timedelta(seconds=1)

    def saludar(self):
        print("Hola que tal")


root = Tk()
miVentana = Ventana(root)
root.mainloop()
