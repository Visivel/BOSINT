import customtkinter as ctk
import threading
import concurrent.futures
import requests


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

        mainFrame = ctk.CTkFrame(root)
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
        print("test")

    def SocialFunction(self):
        ctk.set_default_color_theme("green")
        print_lock = threading.Lock()

        WEBSITES = [
            "instagram", "facebook", "twitter", "youtube", "blogger", "google_plus", "reddit",
            "wordpress", "pinterest", "github", "tumblr", "flickr", "steam", "vimeo", "soundcloud", "disqus",
            "medium", "deviantart", "vk", "aboutme", "imgur", "flipboard", "slideshare", "fotolog", "spotify",
            "mixcloud", "scribd", "badoo", "patreon", "bitbucket", "dailymotion", "etsy", "cashme", "behance",
            "goodreads", "instructables", "keybase", "kongregate", "livejournal", "angellist", "last_fm",
            "dribbble", "codecademy", "gravatar", "pastebin", "foursquare", "roblox", "gumroad", "newsground",
            "wattpad", "canva", "creative_market", "trakt", "five_hundred_px", "buzzfeed", "tripadvisor", "hubpages",
            "contently", "houzz", "blipfm", "wikipedia", "hackernews", "reverb_nation", "designspiration",
            "bandcamp", "colourlovers", "ifttt", "ebay", "slack", "okcupid", "trip", "ello", "tracky", "basecamp"
        ]
        
        def socialFirstMsg():
            socialMsg.insert("end", "[SISTEMA]: Bem vindo! Digite o nome de um usuário para procurá-lo em nossa lista de redes sociais.\n")


        def trolling():
            source = requests.get(url).text
            if vitima in source:
                with print_lock:
                    url = socialMsg.insert("end", "[SISTEMA]: Rede Social encontrada: https://www.{}.com/{}\n".format(website,vitima))
            else:
                pass
        def sendfunc():
            vitima = socialText.get("1.0", "end-1c")
            
            
            
            if vitima and not vitima.isspace():
                socialMsg.insert("end", "[Usuário]: {}\n".format(vitima))
                
                with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
                    for url in WEBSITES:
                        executor.submit(sendfunc, url)
                
                source = requests.get(url).text
                if vitima in source:
                    with print_lock:
                        socialMsg.insert("end", "[SISTEMA]: Rede Social encontrada: {}\n".format(url))
                else:
                    pass
                
            else:
                socialMsg.insert("end", "[SISTEMA]: Desculpe, você deve digitar algo no texto!\n")

           

        socialWindow = ctk.CTk()
        socialWindow.title("Social Media Lookup")
        socialWindow.configure(width=740, height=480)
        socialWindow.resizable(width=False, height=False)

        socialText = ctk.CTkTextbox(socialWindow, height=5, width=500)
        socialText.place(x=10, y=335)

        socialSend = ctk.CTkButton(socialWindow, text="Enviar", height=30, width=10, command=sendfunc)
        socialSend.place(x=525, y=335)

        socialMsg = ctk.CTkTextbox(socialWindow, height=300, width=565)
        socialMsg.place(x=10, y=20)

        socialFirstMsg()
        socialWindow.mainloop()
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
