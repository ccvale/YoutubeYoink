import customtkinter as tk
from YoutubeYoink import YoutubeVideo

class App(tk.CTk):
    def __init__(self):
        super().__init__()
        tk.set_appearance_mode('system')
        tk.set_default_color_theme('green')

        self.geometry('600x450')
        self.title('Youtube Yoink')
        self.minsize(500, 350)

        self.boxText = tk.StringVar(value='Select an option')

        # frame
        self.frame = tk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        # title heading
        self.label = tk.CTkLabel(master=self.frame, text='Youtube Yoink')
        self.label.pack(pady=12, padx=10)

        # URL text heading
        self.label = tk.CTkLabel(master=self.frame, text='URL')
        self.label.place(relx=0.29, rely=0.15)

        # link entry field
        self.entry = tk.CTkEntry(master=self.frame)
        self.entry.pack(pady=12, padx=10)

        self.combobox = tk.CTkOptionMenu(master=self.frame, values=['Select an option', 'MP3', 'MP4'])
        self.combobox.pack(padx=20, pady=10)
        self.combobox.set('Select an option')

        # convert button
        self.button = tk.CTkButton(master=self.frame, text='Convert', command=self.execute)
        self.button.pack(pady=12, padx=10)
    
    def execute(self):
        url = self.entry.get()
        choice = self.combobox.get()
        self.button.state = 'disabled'

        self.entry.delete(0, len(url))
        self.combobox.set('Select an option')

        YoutubeVideo(url, choice).convert()
        self.button.state = 'normal'

if __name__ == '__main__':
    app = App()
    app.mainloop()