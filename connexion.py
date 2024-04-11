import tkinter as tk

class PagesManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure la fenêtre principale
        self.geometry("800x600")
        self.title("Sample App")

        # Crée les pages
        self.accueil_page = AccueilPage(self)
        self.connexion_page = ConnexionPage(self)

        # Affiche la page d'accueil initialement
        self.show_accueil()

    def show_accueil(self):
        self.accueil_page.pack()
        self.connexion_page.pack_forget()

    def show_connexion(self):
        self.accueil_page.pack_forget()
        self.connexion_page.pack()

class AccueilPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2D6487")  # Changer la couleur d'arrière-plan
        self.master = master
        self.configure_ui()

    def configure_ui(self):
        self.label = tk.Label(self, text="GESTION DE L’EFFECTIVITE DES ENSEIGNEMENTS", font=("Arial", 10, "bold"), fg="white", bg="#2D6487")  # Changer la couleur de texte et d'arrière-plan
        self.label.pack(side=tk.TOP, padx=10, pady=(20, 0))

        self.label_2 = tk.Label(self, text="Suivi périodique des enseignements effectués", font=("Arial", 10, "bold"), fg="white", bg="#2D6487")  # Changer la couleur de texte et d'arrière-plan
        self.label_2.pack(side=tk.TOP, padx=10, pady=(10, 0))

class ConnexionPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2D6487")  

class Ui_Form:
    def __init__(self, master):
        self.master = master
        self.configure_ui()

    def configure_ui(self):
        self.master.title("Connexion")

        self.widget = tk.Frame(self.master, bg="white")
        self.widget.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.widget, text="Connexion Page", font=("Arial", 18))
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.widget, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.widget)
        self.username_entry.pack()

        self.password_label = tk.Label(self.widget, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.widget, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.widget, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Vérification des identifiants
        # if username == "admin" and password == "admin":
        # #     messagebox.showinfo("Success", "Login successful!")
        #     # Ajoutez ici le code pour rediriger vers la page d'accueil ou effectuer d'autres actions après la connexion réussie
        # else:
        #     messagebox.showerror("Error", "Invalid username or password. Please try again.")

# Pour tester l'interface utilisateur
def main():
    root = tk.Tk()
    ui = Ui_Form(root)
    root.mainloop()

if __name__ == "__main__":
    main()