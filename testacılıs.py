from tkinter import Tk, Button, Label, messagebox
from tkinter.font import Font
import subprocess
import os
import sys

class App:
    def __init__(self, root):
        # Pencere başlığını ayarla
        root.title("SMS Bomber Menu")
        # Pencere boyutunu ayarla
        width = 300
        height = 100
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        sms_yazı = Label(root)
        sms_yazı["bg"] = "#000000"
        sms_yazı["cursor"] = "heart"
        sms_yazı["disabledforeground"] = "#d21a1a"
        ft = Font(family='Times', size=20)
        sms_yazı["font"] = ft
        sms_yazı["fg"] = "#ffffff"
        sms_yazı["justify"] = "center"
        sms_yazı["text"] = "SMS Modunu Seç;"
        sms_yazı.place(x=0, y=0, width=300, height=30)

        normal_button = Button(root)
        normal_button["bg"] = "#ffffff"
        normal_button["cursor"] = "cross"
        ft = Font(family='Times', size=14)
        normal_button["font"] = ft
        normal_button["fg"] = "#000000"
        normal_button["justify"] = "center"
        normal_button["text"] = "Normal"
        normal_button.place(x=20, y=40, width=100, height=25)
        normal_button.bind("<Enter>", self.on_enter)  # Üzerine gelindiğinde
        normal_button.bind("<Leave>", self.on_leave)  # Üzerinden ayrıldığında
        normal_button["command"] = self.normal_button_command

        turbo_button = Button(root)
        turbo_button["bg"] = "#ffffff"
        turbo_button["cursor"] = "cross"
        ft = Font(family='Times', size=14)
        turbo_button["font"] = ft
        turbo_button["fg"] = "#000000"
        turbo_button["justify"] = "center"
        turbo_button["text"] = "Turbo"
        turbo_button.place(x=180, y=40, width=100, height=25)
        turbo_button.bind("<Enter>", self.on_enter)  # Üzerine gelindiğinde
        turbo_button.bind("<Leave>", self.on_leave)  # Üzerinden ayrıldığında
        turbo_button["command"] = self.turbo_button_command

        # Label oluştur ve konumlandır
        label_normal = Label(root, text="(stabil)", font=("Times", 10, "italic"), fg="white", bg="black")
        label_normal.place(x=45, y=65)

        label_turbo = Label(root, text="(beta)", font=("Times", 10, "italic"), fg="white", bg="black")
        label_turbo.place(x=212, y=65)

    def normal_button_command(self):
        print("normal")
        print("normal")
        subprocess.Popen(["python", "smsbombertkinter.py"])
        sys.exit()  # Ana programı sonlandır

    def turbo_button_command(self):
        print("turbo")
        messagebox.showwarning("Turbo mod","Turbo mod hala geliştirme sürecindedir.Bazı hatalar olabilir, Size normal modu öneriyoruz.")

    def on_enter(self, event):
        event.widget.config(bg="red", fg="white")  # Düğme üzerine gelindiğinde arka plan rengini kırmızı yap

    def on_leave(self, event):
        event.widget.config(bg="#ffffff", fg="black")  # Düğmeden ayrıldığında arka plan rengini beyaz yap



cevap = messagebox.askquestion("YASAL UYARI", "Eğitim amaçlıdır.bu programı kullanarak tamamen kendi\n riskiniz üzerine kullanıldığınızı kabul etmiş olursunuz.\nHerhangi bir sorumluluk kabul etmemekteyim.\nprogramın kötüye kullanılması beni ilgilendirmez.\n\nDevam Etmek İstiyor Musunuz?")
if cevap == "yes":
    print("Evet")
else:
    print("Hayır")
    exit()



if __name__ == "__main__":
    root = Tk()
    root.configure(bg="black")
    app = App(root)
    root.mainloop()
