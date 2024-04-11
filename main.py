
import tkinter as tk
from ui_dashboard import Ui_MainWindow

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Créer une instance de l'interface graphique
        self.ui = Ui_MainWindow(self)

# Fonction principale
def main():
    # Créer une instance de la fenêtre principale
    app = MainWindow()

    # Lancer la boucle principale de l'application Tkinter
    app.mainloop()

# Vérifier si c'est le fichier principal exécuté
if __name__ == "__main__":
    main()
