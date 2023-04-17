import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
from main import scrapProxies, checkerHandler, proxySave, openFile

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.textBox1 = None
        self.textBox2 = None
        self.title('Proxy Scrapper / Checker')
        self.eval('tk::PlaceWindow . center')
        self.geometry('620x400')
        self.resizable(False, False)

        self.allProxiesFrame()
        self.goodProxiesFrame()
        self.secondFrame()

    def allProxiesFrame(self):
        frame_1 = CTkFrame(self, width=225, height=380, fg_color='black', border_color='black', corner_radius=20, border_width=5)
        frame_1.grid(row=0, column=0, pady=10, padx=8)

        self.textBox1 = CTkTextbox(frame_1, width=225, height=380, border_color='#808080', corner_radius=20,
                                   border_width=5, bg_color='#808080', font=('Arial', 15, 'bold'))
        self.textBox1.pack(fill=X)
        
    def goodProxiesFrame(self):
        frame_2 = CTkFrame(self, width=225, height=380, fg_color='white', border_color='black', corner_radius=20,
                           border_width=5)
        frame_2.grid(row=0, column=1, pady=10, padx=(0, 8))
        self.textBox2 = CTkTextbox(frame_2, width=225, height=380, border_color='#808080', corner_radius=20,
                                   border_width=5, bg_color='#808080', font=('Arial', 15, 'bold'))
        self.textBox2.pack(fill=X)
        
        
    def secondFrame(self):

        image = Image.open('image.png').resize((120, 120))

        frame_3 = CTkFrame(self, width=120, height=380, border_color='#808080', corner_radius=10, border_width=2)
        frame_3.grid(row=0, column=2, pady=10, padx=(0, 8))

        CTkLabel(frame_3, image=ImageTk.PhotoImage(image), text='').grid(row=0, column=0, pady=10, padx=10)
        CTkButton(frame_3, text='Scrap', width=100, command=lambda: scrapProxies(self.textBox1)).grid(row=1, column=0, pady=10, padx=10)
        CTkButton(frame_3, text='Save', width=100, command=lambda: proxySave()).grid(row=2, column=0, padx=10)
        CTkButton(frame_3, text='Open', width=100, command=lambda: openFile(self.textBox1)).grid(row=3, column=0, pady=10, padx=10)
        CTkButton(frame_3, text='Check', width=100, command=lambda: checkerHandler(self.textBox2)).grid(row=4, column=0, padx=10)
        CTkButton(frame_3, text='Exit', width=100, command=lambda: self.destroy()).grid(row=5, column=0, pady=10, padx=10)
        CTkLabel(frame_3, text='I Hate This Life!', font=('Arial', 12, 'bold')).grid(row=6, column=0, pady=(0, 0), padx=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()