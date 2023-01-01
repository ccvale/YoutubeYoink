import customtkinter as tk
from PIL import Image, ImageTk
from YoutubeVideo import YoutubeVideo

class ENUM:
    PINK = '#df8598'
    DARK_PINK = '#b26a79'
    DARKER_PINK = '#9c5d6a'
    PURPLE = '#aa93dd'
    BLUE = '#afcbff'
    DEFAULT_GREEN = '#54a376'
    RED = '#d22b2b'
    FONT = '<MesloLGS NF>'
    COMP = '#8598df'

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        tk.set_appearance_mode('system')

        self.title('Youtube Yoink')
        self.geometry('600x450')
        self.resizable(False, False)

        self.buttonText = tk.StringVar(value='Convert')

        # frame
        self.frame = tk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        # title heading
        self.title = tk.CTkLabel(master=self.frame, text='Youtube Yoink', font=(ENUM.FONT, 30))
        self.title.pack(pady=12, padx=10)

        # URL text heading
        self.label = tk.CTkLabel(master=self.frame, text='URL', font=(ENUM.FONT, 20))
        self.label.place(relx=0.155, rely=0.175)

        # link entry field
        self.entry = tk.CTkTextbox(master=self.frame, width=250, height=3, activate_scrollbars=False)
        self.entry.pack(pady=12, padx=10)

        self.combobox = tk.CTkOptionMenu(master=self.frame, values=['MP3', 'MP4'], fg_color=ENUM.PINK, button_color=ENUM.DARK_PINK, button_hover_color=ENUM.DARKER_PINK, font=(ENUM.FONT, 15))
        self.combobox.pack(padx=20, pady=10)
        self.combobox.set('Select an option:')

        # convert button
        self.button = tk.CTkButton(master=self.frame, text='Convert', command=self.execute, textvariable=self.buttonText, fg_color=ENUM.PINK, hover_color=ENUM.DARK_PINK, font=(ENUM.FONT, 15))
        self.button.pack(pady=12, padx=10)
    
    def execute(self):
        self.buttonText.set('Convert')
        self.button.configure(fg_color=ENUM.PINK)

        url = self.entry.get('0.0', 'end')
        choice = self.combobox.get()
        self.update()
        
        try:
            # handling on submit
            self.buttonText.set('Downloading...')
            self.button.state = 'disabled'
            self.update()

            # these will reset no matter what
            self.entry.delete('0.0', 'end')
            self.combobox.set('Select an option:')

            YoutubeVideo(url, choice).convert()

            # handling the reset
            self.button.state = 'normal'
            self.buttonText.set('Convert')
            self.update()

        except:
            self.buttonText.set('Try Again')
            self.button.configure(fg_color=ENUM.COMP)
            self.update()


if __name__ == '__main__':
    app = App()
    app.mainloop()