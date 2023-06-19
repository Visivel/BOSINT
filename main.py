import customtkinter
import customtkinter as ctk

class App:
    def __init__(self, root):
        ctk.set_default_color_theme("dark-blue")
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
        buttonIPLocation.configure(font=("Algma coisa", 25), text="IP Location", command=self.IPFunction)
        buttonIPLocation.place(x=80, y=150)
        buttonIPLocation.configure(width=244, height=88)

        labelTitle = ctk.CTkLabel(mainFrame)
        labelTitle.configure(font=("Times", 50, "bold"), text="BOSINTS", justify="center")
        labelTitle.place(x=140, y=40)
        labelTitle.configure(width=328, height=30)

        labelDescription = ctk.CTkLabel(root)
        labelDescription.configure(font=("Times", 30), text="Basic OSINT Search")
        labelDescription.place(x=230, y=320)

        labelCredits = ctk.CTkLabel(root)
        labelCredits.configure(font=("Times", 15), text="Made by Mikael", text_color="green")
        labelCredits.place(x=300, y=350)

        buttonSocial = ctk.CTkButton(root)
        buttonSocial.configure(font=("Alguma outra coisa", 25), text="Social Media Lookup", command=self.SocialFunction)
        buttonSocial.place(x=390, y=150)
        buttonSocial.configure(width=237, height=89)

    def IPFunction(self):
        print("IP command")

    def SocialFunction(self):
        ctk.set_default_color_theme("green")
        def socialFirstMsg():
            socialMsg.insert("end", "[SISTEMA]: Bem vindo! Digite o nome de um usuario para procura-lo em nossa lista de redes\nsociais.\n")
        def sendfunc():
            mensagem = socialText.get("1.0", "end-1c") # definitivamente eu que fiz isso kkkk
            #socialMsg.delete("1.0", "end")
            if mensagem and not mensagem.isspace():
                socialMsg.insert("end", "[Usuario]: {} \n".format(mensagem))
            else:
                socialMsg.insert("end", "[SISTEMA]: Desculpe, voce deve colocar algo no texto!\n")
        socialWindow = ctk.CTk()
        socialWindow.title("Social Media Lookup")
        socialWindow.configure(width=600, height=400)
        socialWindow.resizable(width=False, height=False)

        socialText = ctk.CTkTextbox(socialWindow, height=50, width=500)
        socialText.place(x=10, y=335)

        socialSend = ctk.CTkButton(socialWindow, text="Enviar", height=50, width=50, command=sendfunc)
        socialSend.place(x=525, y=335)

        socialMsg = ctk.CTkTextbox(socialWindow, height=300, width=565)
        socialMsg.place(x=10, y=20)

        socialFirstMsg()
        socialWindow.mainloop()
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
