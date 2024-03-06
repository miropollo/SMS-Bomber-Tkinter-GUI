import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
from colorama import Fore
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor

# SMS servisleri listesi oluşturma
servisler_sms = [attribute for attribute in dir(SendSms) if not attribute.startswith('__') and callable(getattr(SendSms, attribute))]

# Assets dosya yolu belirleme
ASSETS_PATH_LOCATION = "assets"
OUTPUT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = OUTPUT_PATH / ASSETS_PATH_LOCATION

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def custom_message_box(title, message, button_text, after_callback):
    # Yeni bir Tkinter penceresi oluştur
    window = Tk()
    window.title(title)
    
    # Mesajı gösteren bir etiket ekle
    label = Label(window, text=message)
    label.pack(padx=20, pady=10)
    
    # Buton ekle ve işlevi tanımla
    def close_window():
        window.destroy()
        after_callback()
    
    button = Button(window, text=button_text, command=close_window)
    button.pack(pady=10)
    
    # Pencereyi ekranda göster
    window.mainloop()

def bilgi_button_command():
    global bilgi_window
    
    # Yeni bir Tkinter penceresi oluştur
    bilgi_window = Tk()
    bilgi_window.title("Bilgi")
    
    # Bilgi etiketi ekle
    bilgi_label = Label(bilgi_window, text=f"Telefon Numarası: {tel_no_entry.get()}\nGönderilecek SMS Sayısı: 0", font=("Arial", 12))
    bilgi_label.pack(padx=20, pady=10)
    
    # Durdur butonunu tanımla ve işlevi belirle
    def stop_sms():
        bilgi_window.destroy()
        # İlgili işlemleri buraya ekleyin (örneğin, SMS göndermeyi durdurun)
    
    stop_button = Button(bilgi_window, text="Kapat", command=stop_sms)
    stop_button.pack(pady=10)
    
    # Pencereyi göster
    bilgi_window.mainloop()

def gonder_button_command():
    messagebox.showinfo("YASAL UYARI", "Eğitim amaçlıdır.bu programı kullanarak tamamen kendi\n riskiniz üzerine kullanıldığınızı kabul etmiş olursunuz.\nHerhangi bir sorumluluk kabul etmemekteyim.\nprogramın kötüye kullanılması beni ilgilendirmez.\n\nDevam Etmek İstiyor Musunuz?")
    tel_no = tel_no_entry.get()
    kere = kere_entry.get()
    mail = ""
    aralik = 0
    tel_liste = []

    if not tel_no:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Telefon numarası boş bırakılamaz!")
        messagebox.showerror("Hata", "Telefon numarası boş bırakılamaz!")
        return

    if kere and int(kere) == 1:
        messagebox.showerror("Hata", "Teknik bir hatadan dolayı SMS sayısı 1'den büyük olmalıdır.")
        return

    else:
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
            tel_liste.append(tel_no)

        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası.")
            messagebox.showerror("Hata", "Hatalı telefon numarası.")
            return

    if kere:
        kere = int(kere) // 2
        print("Telefon Numarası:", tel_no, "\nSMS Adeti:", kere * 2, "\nSaniye Aralığı:", aralik, "\ne-mail:", mail)
    else:
        kere = None
        print("Telefon Numarası:", tel_no, "\nSMS Adeti: SONSUZ", "\nSaniye Aralığı:", aralik, "\ne-mail:", mail)

    tel_liste.append(tel_no)

    def send_sms():
        nonlocal tel_no, kere, mail, aralik
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                while sms.adet < kere:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value) and not attribute.startswith('__'):
                            if sms.adet == kere:
                                break
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        system("cls||clear")
        print("Bitti,Gönderilen SMS Sayısı:", kere * 2)
        print("Yeniden gönderebilirsin.by @miropollo")
        messagebox.showinfo("Bilgilendirme", f"{kere * 2} tane SMS başarıyla gönderildi.\nTekrardan gönderebilirsiniz.")

    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(send_sms)

def hakkımda_button_command():
    print("bilgi_button_command")
    global info_window  # Define info_window as global to access it outside the function
    info_window = Tk()
    info_window.title("Information")
    info_window.geometry("415x140")
    info_window.resizable(False, False)

    info_label = Label(info_window, text="Eğitim amaçlıdır.bu programı kullanarak tamamen kendi\n riskiniz üzerine kullanıldığınızı kabul etmiş olursunuz.\nHerhangi bir sorumluluk kabul etmemekteyim.\nprogramın kötüye kullanılması beni ilgilendirmez.",font=("Arial", 13), bg="grey", fg="white")
    info_label.place(x=2, y=0)

    close_button = Button(info_window, text="Okudum,Anladım ve kabul ediyorum", command=info_window.destroy, padx=40, pady=0, font=("Arial", 13), bg="green", fg="white", relief="flat")
    close_button.place(x=35, y=90)
    info_window.mainloop()
    print("hakkımda_button")
    custom_message_box("Özel Mesaj Kutusu", "Bu bir özel mesaj kutusu!", "Kapat", continue_after_message_box)
    print("test123")

def continue_after_message_box():
    print("Devam eden kod işlendi.")

# Ana Tkinter penceresi oluşturma
window = Tk()
window.title("SMS Bomber by @miropollo")
window.geometry("400x160")
window.configure(bg="#FFFFFF")

# Rakam girilmesini sağlayan ve maksimum 10 karakter sınırını kontrol eden doğrulama fonksiyonu
def on_validate(d, i, P, s, S, v, V, W):
    if S.isdigit() and len(P) <= 10:
        return True
    else:
        return False

# Doğrulama fonksiyonunu Tkinter'a kaydetme
validation = window.register(on_validate)

# Canvas oluşturma
canvas = Canvas(window, bg="#FFFFFF", height=160, width=400, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Resimler
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(200.0, 15.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(202.0, 15.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(91.0, 54.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(91.0, 95.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(91.0, 54.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(91.0, 95.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(277.0, 15.0, image=image_image_7)

# Giriş kutuları
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(284.0, 55.0, image=entry_image_1)
tel_no_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 14), validate="key", validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
tel_no_entry.place(x=215, y=40.0, width=182.0, height=28.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(284.0, 96.0, image=entry_image_2)
kere_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 14))
kere_entry.place(x=215, y=81.0, width=182.0, height=28.0)

# Butonlar
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
gonder_button = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: [gonder_button_command()], relief="flat")
gonder_button.place(x=256.0, y=121.0, width=130.0, height=30.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
hakkımda_button = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=hakkımda_button_command, relief="flat")
hakkımda_button.place(x=11.0, y=121.0, width=130.0, height=30.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
bilgi_button = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=bilgi_button_command, relief="flat")
bilgi_button.place(x=149.0, y=121.0, width=100.0, height=30.0)

# Ana pencereyi çalıştır
window.resizable(False, False)
window.mainloop()
