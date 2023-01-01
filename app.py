import customtkinter as tk
from YoutubeVideo import YoutubeVideo
import time

# not used; customtkinter doesnt like these colors for some reason
class PASTEL_ENUM:
    PINK = '#df8598',
    PURPLE = '#aa93dd',
    BLUE = '#afcbff'

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        tk.set_appearance_mode('system')
        tk.set_default_color_theme('green')

        self.title('Youtube Yoink')
        self.geometry('600x450')
        self.resizable(False, False)

        self.buttonText = tk.StringVar(value='Convert')

        # frame
        self.frame = tk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        # title heading
        self.label = tk.CTkLabel(master=self.frame, text='Youtube Yoink')
        self.label.pack(pady=12, padx=10)

        # URL text heading
        self.label = tk.CTkLabel(master=self.frame, text='URL')
        self.label.place(relx=0.155, rely=0.155)

        # link entry field
        self.entry = tk.CTkTextbox(master=self.frame, width=250, height=3, activate_scrollbars=False)
        self.entry.pack(pady=12, padx=10)

        self.combobox = tk.CTkOptionMenu(master=self.frame, values=['Select an option:', 'MP3', 'MP4'])
        self.combobox.pack(padx=20, pady=10)
        self.combobox.set('Select an option:')

        # convert button
        self.button = tk.CTkButton(master=self.frame, text='Convert', command=self.execute, textvariable=self.buttonText)
        self.button.pack(pady=12, padx=10)
    
    def execute(self):
        self.buttonText.set('Convert')
        #self.button.configure(fg_color='green')
        try:
            url = self.entry.get('0.0', 'end')
            choice = self.combobox.get()
            self.buttonText.set('Downloading...')
            self.button.state = 'disabled'

            self.entry.delete('0.0', 'end')
            self.combobox.set('Select an option')

            YoutubeVideo(url, choice).convert()
            self.button.state = 'normal'
            self.buttonText.set('Convert')
        except:
            self.buttonText.set('Try Again')
            self.button.configure(fg_color='#D22B2B')

if __name__ == '__main__':
    app = App()
    app.mainloop()