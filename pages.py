# import tkinter as tk

# class Page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 1", font=('Helvetica', 18))
#         label.pack(pady=10, padx=10)
#         button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
#         button.pack()

# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 2", font=('Helvetica', 18))
#         label.pack(pady=10, padx=10)
#         button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
#         button.pack()


# pages.py
from accueil import Ui_Form as AccueilPage
from connexion import Ui_Form as ConnexionPage

class PagesManager:
    def __init__(self, master):
        self.master = master
        self.accueil_page = AccueilPage()
        self.connexion_page = ConnexionPage()

    def show_accueil(self):
        self.accueil_page.setupUi(self.master)

    def show_connexion(self):
        self.connexion_page.setupUi(self.master)
