
import tkinter as tk
from tkinter import ttk, messagebox

# Membuat jendela utama
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("750x850")
root.resizable(False, False)

# Warna aplikasi
warna_bg = "#DCEAF7"
warna_putih = "#FFFFFF"
warna_biru = "#2874A6"
warna_biru_tua = "#174A70"
warna_teks = "#243746"

root.configure(bg=warna_bg)


# Fungsi Simpan
def simpan():
    nama = entry_nama.get()
    nim = entry_nim.get()
    jk = gender.get()
    prodi = combo_prodi.get()
    semester = combo_semester.get()
    alamat = text_alamat.get("1.0", tk.END).strip()

    if nama == "" or nim == "" or jk == "" or prodi == "" or semester == "" or alamat == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    hasil.config(state="normal")
    hasil.delete("1.0", tk.END)

    hasil.insert(tk.END, f"Nama             : {nama}\n")
    hasil.insert(tk.END, f"NIM              : {nim}\n")
    hasil.insert(tk.END, f"Jenis Kelamin    : {jk}\n")
    hasil.insert(tk.END, f"Program Studi    : {prodi}\n")
    hasil.insert(tk.END, f"Semester         : {semester}\n")
    hasil.insert(tk.END, f"Alamat           : {alamat}\n")

    hasil.config(state="disabled")

    messagebox.showinfo("Berhasil", "Data berhasil disimpan!")


# Fungsi Reset
def reset():
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    gender.set("")
    combo_prodi.set("")
    combo_semester.set("")
    text_alamat.delete("1.0", tk.END)

    hasil.config(state="normal")
    hasil.delete("1.0", tk.END)
    hasil.insert(tk.END, "Hasil identitas akan muncul di sini.")
    hasil.config(state="disabled")


# Fungsi Keluar
def keluar():
    jawab = messagebox.askyesno(
        "Konfirmasi",
        "Apakah Anda yakin ingin keluar?"
    )

    if jawab:
        root.destroy()


# Frame utama
frame_utama = tk.Frame(root, bg=warna_bg)
frame_utama.pack(pady=15)

# Judul aplikasi
tk.Label(
    frame_utama,
    text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 17, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
).pack(pady=5)

tk.Label(
    frame_utama,
    text="FAKULTAS TEKNOLOGI INFORMASI\nUNIVERSITAS HASYIM ASY'ARI",
    font=("Arial", 10),
    bg=warna_bg,
    fg=warna_teks,
    justify="center"
).pack(pady=5)

# Garis pemisah
tk.Frame(
    frame_utama,
    bg=warna_biru,
    height=2,
    width=550
).pack(pady=10)


# Frame formulir
frame_form = tk.Frame(
    frame_utama,
    bg=warna_putih,
    padx=25,
    pady=20
)
frame_form.pack(pady=5)

# Nama
tk.Label(
    frame_form,
    text="Nama Lengkap",
    bg=warna_putih,
    fg=warna_teks,
    font=("Arial", 10, "bold")
).grid(row=0, column=0, sticky="w", padx=10, pady=10)

entry_nama = tk.Entry(frame_form, width=35, font=("Arial", 10))
entry_nama.grid(row=0, column=1, pady=10)

# NIM
tk.Label(
    frame_form,
    text="NIM",
    bg=warna_putih,
    fg=warna_teks,
    font=("Arial", 10, "bold")
).grid(row=1, column=0, sticky="w", padx=10, pady=10)

entry_nim = tk.Entry(frame_form, width=35, font=("Arial", 10))
entry_nim.grid(row=1, column=1, pady=10)

# Jenis Kelamin
tk.Label(
    frame_form,
    text="Jenis Kelamin",
    bg=warna_putih,
    fg=warna_teks,
    font=("Arial", 10, "bold")
).grid(row=2, column=0, sticky="w", padx=10, pady=10)

gender = tk.StringVar()

frame_gender = tk.Frame(frame_form, bg=warna_putih)
frame_gender.grid(row=2, column=1, sticky="w")

tk.Radiobutton(
    frame_gender,
    text="Laki-laki",
    variable=gender,
    value="Laki-laki",
    bg=warna_putih
).pack(side="left", padx=5)

tk.Radiobutton(
    frame_gender,
    text="Perempuan",
    variable=gender,
    value="Perempuan",
    bg=warna_putih
).pack(side="left", padx=5)

# Program Studi
tk.Label(
    frame_form,
    text="Program Studi",
    bg=warna_putih,
    fg=warna_teks,
    font=("Arial", 10, "bold")
).grid(row=3, column=0, sticky="w", padx=10, pady=10)

combo_prodi = ttk.Combobox(
    frame_form,
    values=[
        "Teknik Informatika",
        "Sistem Informasi",
        "Teknologi Informasi"
    ],
    state="readonly",
    width=32
)
combo_prodi.grid(row=3, column=1, pady=10)

# Semester
tk.Label(
    frame_form,
    text="Semester",
    bg=warna_putih,
    fg=warna_teks,
    font=("Arial", 10, "bold")
).grid(row=4, column=0, sticky="w", padx=10, pady=10)

combo_semester = ttk.Combobox(
    frame_form,
    values=[
        "Semester 1", "Semester 2",
        "Semester 3", "Semester 4",
        "Semester 5", "Semester 6",
        "Semester 7", "Semester 8"
    ],
    state="readonly",
    width=32
)
combo_semester.grid(row=4, column=1, pady=10)

# Alamat
tk.Label(
    frame_form,
    text="Alamat",
    bg=warna_putih,
    fg=warna_teks,
    font=("Arial", 10, "bold")
).grid(row=5, column=0, sticky="nw", padx=10, pady=10)

text_alamat = tk.Text(
    frame_form,
    width=33,
    height=5,
    font=("Arial", 10)
)
text_alamat.grid(row=5, column=1, pady=10)


# Tombol
frame_tombol = tk.Frame(frame_utama, bg=warna_bg)
frame_tombol.pack(pady=15)

tk.Button(
    frame_tombol,
    text="Simpan",
    width=13,
    command=simpan,
    bg=warna_biru,
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat"
).grid(row=0, column=0, padx=7)

tk.Button(
    frame_tombol,
    text="Reset",
    width=13,
    command=reset,
    bg="#7F8C8D",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat"
).grid(row=0, column=1, padx=7)

tk.Button(
    frame_tombol,
    text="Keluar",
    width=13,
    command=keluar,
    bg="#C0392B",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat"
).grid(row=0, column=2, padx=7)


# Bagian hasil
tk.Label(
    frame_utama,
    text="HASIL IDENTITAS MAHASISWA",
    font=("Arial", 12, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
).pack(pady=5)

frame_hasil = tk.Frame(
    frame_utama,
    bg=warna_putih,
    padx=10,
    pady=10
)
frame_hasil.pack(pady=5)

scrollbar = tk.Scrollbar(frame_hasil)
scrollbar.pack(side="right", fill="y")

hasil = tk.Text(
    frame_hasil,
    width=65,
    height=8,
    font=("Consolas", 10),
    bg=warna_putih,
    fg=warna_teks,
    state="disabled",
    yscrollcommand=scrollbar.set
)
hasil.pack()

scrollbar.config(command=hasil.yview)

hasil.config(state="normal")
hasil.insert(tk.END, "Hasil identitas akan muncul di sini.")
hasil.config(state="disabled")


# Menjalankan aplikasi
root.mainloop()

