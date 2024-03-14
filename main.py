import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do Application")
        self.geometry(f"{400}x{600}")

        self.main()

    def main(self):
        self.container = customtkinter.CTkFrame(self)
        self.container.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
