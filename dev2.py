import customtkinter as ctk
import threading
import concurrent.futures
import requests
import requests.exceptions
from time import sleep


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
        buttonSocial.configure(font=("roboto", 25), text="Social Media Lookup", command=self.SocialFunction)
        buttonSocial.place(x=390, y=150)
        buttonSocial.configure(width=237, height=89)

    def IPFunction(self):
        ctk.set_default_color_theme("green")
        def firstmsg():
            ipMsg.insert("end","[SISTEMA]: Bem vindo! Digite um IP para localiza-lo.\n")
        def ipsendfunc():
            ipvitima = ipText.get("1.0", "end-1c")
            if ipvitima and not ipvitima.isspace():
                ipMsg.insert("end",f"\n[USUARIO]: {ipvitima}\n")
                ip = requests.get(f'https://api.incolumitas.com/?q={ipvitima}').text
                ipMsg.insert("end", ip)
            else:
                ipMsg.insert("end","[SISTEMA]: Desculpe, você deve digitar algo no texto!\n")
                
        ipWindow = ctk.CTk()
        ipWindow.title("IP Location")
        ipWindow.configure(width=740, height=480)
        ipWindow.resizable(width=False, height=False)

        ipText = ctk.CTkTextbox(ipWindow, height=5, width=500)
        ipText.place(x=10, y=335)

        ipSend = ctk.CTkButton(ipWindow, text="Enviar", height=30, width=10, command=ipsendfunc)
        ipSend.place(x=525, y=335)

        ipMsg = ctk.CTkTextbox(ipWindow, height=300, width=565)
        ipMsg.place(x=10, y=20)
        ipMsg.bind("<KeyPress>", lambda e: "break")
        ipMsg.bind("<KeyRelease>", lambda e: "break")
        # ipMsg.bind("<Button-1>", lambda e: "break") caso queira pra nao poder copiar

        firstmsg()
        ipWindow.mainloop()

    def SocialFunction(self):
        result_queue = []
        ctk.set_default_color_theme("green")
        print_lock = threading.Lock()
        
        
        def socialFirstMsg():
            socialMsg.insert("end", "[SISTEMA]: Bem vindo! Digite o nome de um usuário para procurá-lo em nossa lista de redes sociais.\n(Detalhe: O programa pode demorar ate 10 segundos para dar sua resposta)\n")


        #def trolling():
            #source = requests.get(url).text
            #if vitima in source:
                #with print_lock:
                    #url = socialMsg.insert("end", "[SISTEMA]: Rede Social encontrada: https://www.{}.com/{}\n".format(website,vitima))
            #else:
                #pass
        def sendfunc():
            vitima = socialText.get("1.0", "end-1c")
            if vitima and not vitima.isspace():
                socialMsg.insert("end", "[Usuário]: {}\n".format(vitima))
                WEBSITES = [
                    f"https://www.instagram.com/{vitima}", f"https://www.facebook.com/{vitima}", f"https://twitter.com/{vitima}", f"https://www.youtube.com/user/{vitima}", f"https://{vitima}.blogspot.com", f"https://www.reddit.com/user/{vitima}",
                    f"https://{vitima}.wordpress.com", f"https://www.pinterest.com/{vitima}", f"https://www.github.com/{vitima}", f"https://{vitima}.tumblr.com", f"https://www.flickr.com/people/{vitima}", f"https://steamcommunity.com/id/{vitima}", f"https://vimeo.com/{vitima}", f"https://soundcloud.com/{vitima}",
                    f"https://medium.com/@{vitima}", f"https://{vitima}.deviantart.com", f"https://vk.com/{vitima}", f"https://about.me/{vitima}", f"https://imgur.com/user/{vitima}", f"https://slideshare.net/{vitima}", f"https://fotolog.com/{vitima}", f"https://open.spotify.com/user/{vitima}",
                    f"https://www.scribd.com/{vitima}", f"https://www.patreon.com/{vitima}", f"https://bitbucket.org/{vitima}", f"https://www.dailymotion.com/{vitima}", f"https://www.etsy.com/shop/{vitima}", f"https://cash.me/{vitima}", f"https://www.behance.net/{vitima}",
                    f"https://keybase.io/{vitima}", f"https://kongregate.com/accounts/{vitima}", f"https://angel.co/{vitima}", f"https://last.fm/user/{vitima}",
                    f"https://www.codecademy.com/{vitima}", f"https://en.gravatar.com/{vitima}", f"https://pastebin.com/u/{vitima}", f"https://foursquare.com/{vitima}", f"https://www.roblox.com/user.aspx?username={vitima}", f"https://{vitima}.newgrounds.com"
                ]
                # Sim, eu sei que esse codigo ta horrivel mas e o que deu pra fazer em 4 dias.
                # Filtrar alguns webites

                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    for url in WEBSITES:
                        executor.submit(redes, url, vitima, result_queue)

                socialMsg.after(10, update_messages)
            else:
                socialMsg.insert("end", "[SISTEMA]: Desculpe, você deve digitar algo no texto!\n")

        def redes(url, vitima, result_queue):
            try:
                source = requests.get(url, timeout=5, verify=False).text
                if vitima in source:
                    with print_lock:
                        result_queue.append(url)
                sleep(1)
            except requests.ReadTimeout:
                socialMsg.insert("end", f"[DEBUG]: Tempo limite de leitura excedido para o site: {url}")
            except requests.ConnectTimeout:
                socialMsg.insert("end", f"[DEBUG]: Tempo limite para conectar foi excedido no website: {url}")
            except requests.SSLError:
                socialMsg.insert("end", f"[DEBUG]: Tempo limite de SSH excedido no website: {url}")
                

        def update_messages():
            if result_queue:
                with print_lock:
                    for url in result_queue:
                        socialMsg.insert("end", "[SISTEMA]: Rede Social encontrada: {}\n".format(url))
                result_queue.clear()
            socialMsg.after(100, update_messages)
    
           

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
        socialMsg.bind("<KeyPress>", lambda e: "break")
        socialMsg.bind("<KeyRelease>", lambda e: "break")
        # socialMsg.bind("<Button-1>", lambda e: "break") caso queira para nao poder copiar

        socialFirstMsg()
        socialWindow.mainloop()
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
