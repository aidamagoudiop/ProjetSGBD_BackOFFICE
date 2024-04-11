import tkinter as tk

class Ui_Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure_ui()

    def configure_ui(self):
        self.master.title("Form")
        self.master.geometry("428x571")

        self.widget = tk.Frame(self.master, bg="rgba(45, 100, 135, 0.533)")
        self.widget.place(x=-10, y=-50, width=480, height=571)

        self.plainTextEdit = tk.Text(self.widget, bg="transparent", fg="whitesmoke", font=("Arial", 20), wrap="word")
        self.plainTextEdit.insert("1.0", "Bienvenu(e)! Que souhaitez-vous faire ?")
        self.plainTextEdit.configure(state="disabled")
        self.plainTextEdit.place(x=100, y=110, width=251, height=31)

        self.label = tk.Label(self.widget, text="GESTION DE L’EFFECTIVITE DES ENSEIGNEMENTS", bg="transparent", fg="whitesmoke", font=("Arial", 15, "bold"))
        self.label.place(x=80, y=180, width=291, height=31)

        self.label_2 = tk.Label(self.widget, text="Suivi périodique des enseignements effectués", bg="transparent", fg="whitesmoke", font=("Arial", 15, "bold"))
        self.label_2.place(x=80, y=330, width=291, height=31)

if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_Form(master=root)
    ui.mainloop()

class AccueilPage:
    def __init__(self, master):
        self.master = master
        self.configure_ui()

    def configure_ui(self):
        self.widget = tk.Frame(self.master, bg="#2D6487")  # Utilisation d'une couleur hexadécimale
        self.widget.pack(fill="both", expand=True)
