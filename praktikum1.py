import tkinter as tk

root = tk.Tk()
root.title("Sistem Informasi Apotek")

# Mengatur ukuran jendela menjadi 500x500 piksel
root.geometry("500x500")

# Judul utama
label = tk.Label(
    root,
    text="Sistem Informasi Apotek!",
    font=("Arial", 14, "bold")
)
label.grid(row=0, column=0, columnspan=2, pady=20)

# Input Username
tk.Label(root, text="Username").grid(
    row=1, column=0, padx=10, pady=5, sticky="e"
)

entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=5)

# Input Password
tk.Label(root, text="Password").grid(
    row=2, column=0, padx=10, pady=5, sticky="e"
)

entry2 = tk.Entry(root, show="*")
entry2.grid(row=2, column=1, padx=10, pady=5)

# Tombol Login
button = tk.Button(root, text="Login")
button.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()


#Tombol login (merentang dari kolom 0 sampai 1)
