# main.py
import tkinter as tk
from pages import PagesManager

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.geometry("800x600")
        self.title("Sample App")

        # Create instance of PagesManager
        self.pages_manager = PagesManager(self)

        # Show the accueil page initially
        self.pages_manager.show_accueil()

# Main function
def main():
    # Create an instance of the main application
    app = SampleApp()

    # Run the main application loop
    app.mainloop()

# Check if the script is being run directly
if __name__ == "__main__":
    main()
