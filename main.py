from tkinter import messagebox
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do Application")
        self.geometry(f"{400}x{600}")
        # self.eval('tk::PlaceWindow . center')
        self.resizable(0, False)
        self.main()

    def main(self):
        container = customtkinter.CTkFrame(self)
        container.pack(padx=5, pady=5, fill="x")

        lbl_title = customtkinter.CTkLabel(container, text="To-Do List App", font=(customtkinter.CTkFont(weight="bold",
                                                                                                         size=25)))
        lbl_title.pack(pady=(20, 0))

        self.txt_todo = customtkinter.CTkEntry(container, height=40, width=300)
        self.txt_todo.pack(pady=(50, 5))

        btn_submit = customtkinter.CTkButton(container, text="Submit", command=self.submit,
                                             font=(customtkinter.CTkFont(weight="bold", size=20)))
        btn_submit.pack(pady=(0, 10))

        self.wrap = customtkinter.CTkScrollableFrame(self)
        self.wrap.pack(pady=(0, 5), expand=True, fill="both")

    def submit(self):
        todo = self.txt_todo.get()

        if not all([todo]):
            messagebox.showerror("Error", "Please fill.")

            return

        self.chck_box = customtkinter.CTkCheckBox(self.wrap, text=todo, font=(customtkinter.CTkFont(size=18)), command=self.done_list)
        self.chck_box.pack(pady=(3, 3), anchor="nw")

    def done_list(self):
        # self.chck_box.destroy()
        # todo = self.chck_box.getint()



if __name__ == "__main__":
    app = App()
    app.mainloop()
