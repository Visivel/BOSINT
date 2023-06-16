import customtkinter
import customtkinter as ctk

class App:
    def __init__(self, root):
        root.title("BOSINTS")
        width = 731
        height = 432
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        mainFrame = customtkinter.CTkFrame(root)
        mainFrame.grid(row=0, column=0, padx=60, pady=20, sticky="nsw")
        mainFrame.configure(width=600, height=250)

        buttonIPLocation = ctk.CTkButton(root)
        buttonIPLocation.configure(font=("Times", 25), text="IP Location", command=self.IPFunction)
        buttonIPLocation.place(x=80, y=150)
        buttonIPLocation.configure(width=244, height=88)

        labelTitle = ctk.CTkLabel(root)
        labelTitle.configure(font=("Times", 50), text="BOSINTS", justify="center")
        labelTitle.place(x=195, y=40)
        labelTitle.configure(width=328, height=30)

        labelDescription = ctk.CTkLabel(root)
        labelDescription.configure(font=("Italic", 30), text="Basic OSINT Search")
        labelDescription.place(x=220, y=90)

        labelCredits = ctk.CTkLabel(root)
        labelCredits.configure(font=("Montserrat", 15), text="Made by Mikael")
        labelCredits.place(x=300, y=350)

        buttonSocial = ctk.CTkButton(root)
        buttonSocial.configure(font=("Times", 25), text="Social Media Lookup", command=self.SocialFunction)
        buttonSocial.place(x=390, y=150)
        buttonSocial.configure(width=237, height=89)

    def IPFunction(self):
        print("IP command")

    def SocialFunction(self):
        socialWindow = ctk.CTk()
        socialWindow.title("Social Media Lookup")
        socialWindow.resizable(width=False, height=False)
        socialWindow.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
