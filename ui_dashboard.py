import tkinter as tk

class Ui_MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("MainWindow")
        master.geometry("556x374")
        master.configure(bg="black")

        self.header = tk.Frame(master, bg="#071e26")
        self.header.pack(fill="x")

        self.menuBtn = tk.Button(self.header, text="\ue700  MENU", font=("Arial", 12), bg="#265e72", fg="whitesmoke")
        self.menuBtn.pack(side="left", padx=(10, 0), pady=10)

        self.frame_4 = tk.Frame(self.header, bg="#071e26")
        self.frame_4.pack(side="right", padx=(0, 10), pady=10)

        self.label_2 = tk.Label(self.frame_4, text="ADMINISTRATION", font=("Arial", 15, "bold"), bg="#071e26", fg="whitesmoke")
        self.label_2.pack(side="left")

        self.label_3 = tk.Label(self.frame_4, text="\ue77b", font=("Arial", 20), bg="#265e72", fg="whitesmoke")
        self.label_3.pack(side="left", padx=10)

        self.frame_2 = tk.Frame(master, bg="#1b1b27")
        self.frame_2.pack(fill="both", expand=True)

        self.leftMenu = tk.Frame(self.frame_2, bg="#265e72", width=150)
        self.leftMenu.pack(side="left", fill="y")

        self.homeBtn = tk.Button(self.leftMenu, text="\ue80f   Home", font=("Arial", 11, "bold"), bg="black", fg="whitesmoke", bd=1, relief="solid", padx=10)
        self.homeBtn.pack(fill="x", pady=(10, 0))

        self.pvBtn = tk.Button(self.leftMenu, text="\uee93  PV Sceance", font=("Arial", 10), bg="black", fg="whitesmoke", bd=1, relief="solid", padx=10)
        self.pvBtn.pack(fill="x", pady=(0, 10))

        self.main_body = tk.Frame(self.frame_2, bg="#1b1b27")
        self.main_body.pack(side="right", fill="both", expand=True)

        self.label = tk.Label(self.main_body, text="Corps", font=("Arial", 15, "bold"), bg="#1b1b27", fg="whitesmoke")
        self.label.pack(pady=30)
