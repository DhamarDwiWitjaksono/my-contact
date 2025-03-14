import tkinter as tk
from tkinter import messagebox
from contact import Contacts

# list untuk menympan objek kontak
contacts_list = []

# fungsi untuk menmabahkan kontak
def add_contact():
    if str(var_number.get()).isdigit() and "@gmail.com" in var_email.get():
        person = Contacts(var_name.get(), int(var_number.get()), var_email.get())
        contacts_list.append(person)
        Contacts_box.insert(tk.END, str(person))
        messagebox.showinfo("Berhasil", f"{var_name.get()} berhasil ditambahkan.")
        
    else:
        messagebox.showerror("gagal", "mohon masukan data yang benar!")

# fungsi untuk menghapus kontak
def delete_contact():
    try:
        selected_index = Contacts_box.curselection()[0]
        selected_contact = contacts_list[selected_index]

        del contacts_list[selected_index]
        Contacts_box.delete(selected_index)
        messagebox.showinfo("Berhasil", f"Kontak {selected_contact} berhasil dihapus.")

    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih kontak yang ingin dihapus.")

# fungsi untuk menghapus data di form/entry
def clear_entry():
    var_name.set("")
    var_number.set("")
    var_email.set("")

# fungsi untuk menutup aplikasi
def close_app():
    window.destroy()

# tampilan utama
window = tk.Tk()
window.title("Kontak Saya")

# untuk menmabahkan nama kontak
var_name = tk.StringVar()
frame_name = tk.Frame(window)
frame_name.pack()
label_name = tk.Label(frame_name, text="Name")
label_name.pack()
name_entry = tk.Entry(frame_name, textvariable=var_name)
name_entry.pack()

# untuk menmabahkan nomer kontak
var_number = tk.StringVar()
frame_number = tk.Frame(window)
frame_number.pack()
label_phone_no = tk.Label(frame_number, text="Number")
label_phone_no.pack()
number_entry = tk.Entry(frame_number, textvariable=var_number)
number_entry.pack()

# untuk menmabahkan email kontak
var_email = tk.StringVar()
frame_email = tk.Frame(window)
frame_email.pack()
label_email = tk.Label(frame_email, text="Email")
label_email.pack()
email_entry = tk.Entry(frame_email, textvariable=var_email)
email_entry.pack()

# bingkai untuk 3 tombol
frame_button = tk.Frame(window)
frame_button.pack(pady=20)

# tombol tambah kontak
add_button =  tk.Button(frame_button, text="add", command=add_contact).pack(side="left", padx=10)
# tombol hapus kontak
delete_button =  tk.Button(frame_button, text="delete", command=delete_contact).pack(side="left", padx=10)
# tombol hapus form
clear_button =  tk.Button(frame_button, text="clear", command=clear_entry).pack(side="left", padx=10)

# frame untuk kolom daftar kontak
frame_clumb= tk.Frame(window)
frame_clumb.pack(pady=(40, 0))

# kolom nama
name_clumb =  tk.Label(frame_clumb, text="Name").pack(side="left", padx=30)
# kolom nomer hp
number_clumb =  tk.Label(frame_clumb, text="Number").pack(side="left", padx=30)
# kolom email
email_clumb =  tk.Label(frame_clumb, text="Email").pack(side="left", padx=30)

# listbox
Contacts_box = tk.Listbox(window, width=50, height=10)
Contacts_box.pack(padx=20, pady=20)

# tombol keluar aplikasi
quit_button = tk.Button(window, text="Quit", command=close_app).pack(pady=(20, 0))

window.mainloop()