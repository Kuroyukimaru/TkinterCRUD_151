#Mengimpor modul sqlite3 yang memungkinkan interaksi dengan database SQLite.
import sqlite3
# Mengimpor komponen-komponen dari modul tkinter, yang merupakan library bawaan Python untuk membuat GUI (Graphical User Interface).
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk

# Fungsi membuat database dan tabel
#Membuat atau memastikan database dan tabel yang diperlukan tersedia.
def create_database():
    # Membuka koneksi ke database SQLite bernama nilai_siswa.db. Jika file database belum ada, SQLite akan membuatnya secara otomatis.
    conn = sqlite3.connect('nilai_siswa.db')
    # Membuat cursor, yaitu objek yang digunakan untuk menjalankan perintah SQL pada database.
    cursor = conn.cursor()
    # Menjalankan perintah SQL untuk membuat tabel bernama nilai_siswa jika tabel tersebut belum ada.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')
    # Menyimpan perubahan ke database (misalnya, membuat tabel).
    conn.commit()
    # Menutup koneksi ke database untuk membebaskan sumber daya.
    conn.close()

# Mengakses database dan mengambil semua data dari tabel nilai_siswa.
def fetch_data():
    # Membuka koneksi ke database nilai_siswa.db.
    conn = sqlite3.connect('nilai_siswa.db')
    # Membuat cursor untuk menjalankan perintah SQL.
    cursor = conn.cursor()
    # Menjalankan perintah SQL SELECT *, yang mengambil semua kolom dan semua baris dari tabel nilai_siswa.
    cursor.execute('SELECT * FROM nilai_siswa')
    # Mengambil semua data hasil eksekusi perintah SQL dalam bentuk list of tuples. Setiap tuple mewakili satu baris data.
    rows = cursor.fetchall()
    # Menutup koneksi ke database untuk menghemat sumber daya.
    conn.close()
    # Mengembalikan semua data yang diambil dari tabel dalam bentuk list of tuples ke pemanggil fungsi.
    return rows

# Fungsi menyimpan data ke database
# Mendefinisikan fungsi bernama save_to_database yang menerima lima parameter
def save_to_database(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    # Membuka koneksi ke database nilai_siswa.db.
    conn = sqlite3.connect('nilai_siswa.db')
    #Membuat cursor untuk menjalankan perintah SQL.
    cursor = conn.cursor()
    # Menjalankan perintah SQL INSERT INTO untuk menambahkan data baru ke tabel nilai_siswa.
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    # Menyimpan perubahan ke database agar data benar-benar tersimpan.
    conn.commit()
    # Menutup koneksi ke database untuk membebaskan sumber daya.
    conn.close()
    
# Fungsi memperbarui database
# Mendefinisikan fungsi update_database yang menerima enam parameter:
def update_database(id, nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    # Membuka koneksi ke database nilai_siswa.db.
    conn = sqlite3.connect('nilai_siswa.db')
    # Membuat cursor untuk menjalankan perintah SQL.
    cursor = conn.cursor()
    # Menjalankan perintah SQL UPDATE untuk memperbarui kolom-kolom pada tabel nilai_siswa
    cursor.execute('''
        UPDATE nilai_siswa
        SET nama_siswa = ?, biologi = ?, fisika = ?, inggris = ?, prediksi_fakultas = ?
        WHERE id = ?
    ''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas, id))
    #Menyimpan perubahan ke database agar data yang diperbarui tersimpan.
    conn.commit()
    # Menutup koneksi ke database untuk membebaskan sumber daya.
    conn.close()
    
# Fungsi menghapus data di database
# Mendefinisikan fungsi delete_database yang menerima satu parameter
def delete_database(id):
    # Membuka koneksi ke database nilai_siswa.db.
    conn = sqlite3.connect('nilai_siswa.db')
    # Membuat cursor untuk menjalankan perintah SQL.
    cursor = conn.cursor()
    # Menjalankan perintah SQL DELETE FROM untuk menghapus baris dari tabel nilai_siswa
    cursor.execute('DELETE FROM nilai_siswa WHERE id = ?', (id,))
    # Menyimpan perubahan ke database agar penghapusan benar-benar dilakukan.
    conn.commit()
    # Menutup koneksi ke database untuk membebaskan sumber daya.
    conn.close()
    
# Fungsi menghitung prediksi fakultas
# Mendefinisikan fungsi calc_prediction yang menerima tiga parameter
def calc_prediction(biologi, fisika, inggris):
    # Mengecek apakah nilai Biologi lebih besar dari nilai Fisika dan Bahasa Inggris.
    if biologi > fisika and biologi > inggris:
        # Jika True, maka mengembalikan 'Kedokteran'.
        return 'Kedokteran'
    # Mengecek apakah nilai Fisika lebih besar dari nilai Biologi dan Bahasa Inggris.
    elif fisika > biologi and fisika > inggris:
        # Jika True, maka mengembalikan 'Teknik'.
        return 'Teknik'
    #Mengecek apakah nilai Bahasa Inggris lebih besar dari nilai Biologi dan Fisika.
    elif inggris > biologi and inggris > fisika:
        # Jika True, maka mengembalikan 'Bahasa'.
        return 'Bahasa'
    #Jika tidak ada nilai yang paling dominan (misalnya dua atau lebih nilai sama tinggi), fungsi mengembalikan 'Tidak Diketahui'.
    else:
        return 'Tidak Diketahui'


# Fungsi menangani tombol submit
# Menyimpan data
def submit():
    # Blok untuk menangkap kesalahan yang mungkin terjadi selama eksekusi kode, seperti kesalahan konversi data atau input kosong.
    try:
        #Mengambil nilai dari variabel nama_var, yang biasanya terhubung dengan input Entry tkinter untuk nama siswa.
        nama_siswa = nama_var.get()
        # Mengambil nilai dari variabel biologi_var, fisika_var, dan inggris_var, kemudian mengonversinya menjadi tipe int untuk memastikan input berupa angka.
        biologi = int(biologi_var.get())
        fisika = int(fisika_var.get())
        inggris = int(inggris_var.get())
        
        # Mengecek apakah nama siswa kosong. Jika kosong, akan memunculkan kesalahan dengan pesan "Nama siswa harus diisi".
        if not nama_siswa:
            raise Exception("Nama siswa harus diisi")
        
        # Memanggil fungsi calc_prediction untuk menentukan prediksi fakultas berdasarkan nilai input.
        prediksi = calc_prediction(biologi, fisika, inggris)
        
        # Menyimpan data siswa ke database menggunakan fungsi save_to_database.
        save_to_database(nama_siswa, biologi, fisika, inggris, prediksi)
        
        # Menampilkan pesan keberhasilan kepada pengguna, termasuk prediksi fakultas.
        messagebox.showinfo("Sukses", "Data berhasil disimpan! \nPrediksi Fakultas: " + prediksi)
        # Memanggil fungsi untuk mengosongkan semua input form (belum didefinisikan di kode ini, biasanya untuk membersihkan form GUI setelah data disimpan).
        clear_inputs()
        # Memanggil fungsi untuk memperbarui tabel data di GUI (misalnya, menampilkan data terbaru dari database dalam tabel).
        populate_table()
    # Menangkap kesalahan konversi tipe data (misalnya, input angka tidak valid) dan menampilkan pesan kesalahan kepada pengguna.
    except ValueError as e:
        messagebox.showerror("Error", f"Kesalahan: {e}")
        
# Fungsi menangani tombol update
def update():
    # Blok untuk menangkap kesalahan selama eksekusi.
    try:
        # Mengecek apakah pengguna telah memilih data untuk diperbarui.
        if not selected_id.get():
            raise Exception("Pilih data yang akan diupdate",)
        
        # Mengambil ID data yang dipilih dari variabel selected_id dan mengonversinya menjadi tipe int. ID ini adalah kunci unik data dalam tabel.
        id = int(selected_id.get())
        # Mengambil nama siswa dari form input.
        nama_siswa = nama_var.get()
        # Mengambil nilai dari input dan memastikan bahwa nilainya berupa angka.
        biologi = int(biologi_var.get())
        fisika = int(fisika_var.get())
        inggris = int(inggris_var.get())
        
        # Mengecek apakah nama_siswa kosong. Jika kosong, fungsi akan memunculkan kesalahan dengan pesan "Nama siswa harus diisi".
        if not nama_siswa:
            raise ValueError("Nama siswa harus diisi")
        
        # Menggunakan fungsi calc_prediction untuk menghitung prediksi fakultas berdasarkan nilai siswa.
        prediksi = calc_prediction(biologi, fisika, inggris)
        
        # Memanggil fungsi update_database untuk memperbarui data siswa di database, termasuk id, nama, nilai, dan prediksi fakultas.
        update_database(selected_id.get(), nama_siswa, biologi, fisika, inggris, prediksi)
        
        # Menampilkan pesan bahwa data berhasil diperbarui, termasuk prediksi fakultas yang baru.
        messagebox.showinfo("Sukses", "Data berhasil diperbarui!\nPrediksi Fakultas: " + prediksi)
        # Mengosongkan form input setelah data diperbarui.
        clear_inputs()
        # Memperbarui tampilan tabel di GUI agar menampilkan data terbaru.
        populate_table()
    # Menangkap semua kesalahan dan menampilkan pesan error melalui messagebox.showerror.
    except Exception as e:
        messagebox.showerror("Error", f"Kesalahan: {e}")
        
# Fungsi menangani tombol delete
def delete():
    # Blok untuk menangkap kesalahan selama eksekusi fungsi.
    try:
        # Mengecek apakah pengguna telah memilih data untuk dihapus melalui variabel selected_id.
        if not selected_id.get():
            raise Exception("Pilih data yang akan dihapus")
        
        #Mengambil ID dari data yang dipilih dan mengonversinya menjadi tipe int.
        id = int(selected_id.get())
        # Memanggil fungsi delete_database untuk menghapus data dari tabel nilai_siswa dalam database berdasarkan id.
        delete_database(id)
        # Menampilkan pesan bahwa data telah berhasil dihapus.
        messagebox.showinfo("Sukses", "Data berhasil dihapus!")
        # Membersihkan form input di GUI setelah penghapusan selesai.
        clear_inputs()
        # Memperbarui tabel di GUI agar mencerminkan perubahan data.
        populate_table()
    # Menangkap kesalahan konversi tipe data (jika input ID tidak valid) dan menampilkan pesan error.
    except ValueError as e:
        messagebox.showerror("Error", f"Kesalahan: {e}")
        
# Fungsi mengosongkan input
def clear_inputs():
    # Mengosongkan nilai input untuk nama siswa dengan mengatur nilai nama_var
    nama_var.set("")
    # Meng==osongkan nilai input untuk nilai Biologi dengan mengatur nilai biologi_var menjadi string kosong.
    biologi_var.set("")
    # Mengosongkan nilai input untuk nilai Fisika dengan mengatur nilai fisika_var menjadi string kosong.
    fisika_var.set("")
    # Mengosongkan nilai input untuk nilai Bahasa Inggris dengan mengatur nilai inggris_var menjadi string kosong.
    inggris_var.set("")
    # Mengosongkan nilai ID yang dipilih dengan mengatur selected_id menjadi string kosong, yang berarti tidak ada ID yang dipilih.
    selected_id.set("")
    
# Fungsi mengisi tabel dengan data dari database
def populate_table():
    # Mengambil semua item (baris) yang sudah ada di dalam tabel (widget Treeview).
    for row in tree.get_children():
        # Menghapus setiap baris yang ada di tabel sebelum mengisinya dengan data baru. 
        tree.delete(row)
    
    #  mengambil semua data dari database (misalnya, semua data siswa dalam tabel nilai_siswa).
    for row in fetch_data():
        # Menambahkan setiap baris yang diambil dari fetch_data() ke dalam Treeview.
        tree.insert("", "end", values=row)
        
# Fungsi mengisi input dengan data dari tabel
def fill_inputs_from_table(event):
    try:
        # tree.selection() mengembalikan daftar item yang saat ini dipilih di dalam tabel Treeview.
        selected_item = tree.selection()[0]
        # tree.item(selected_item) mengembalikan informasi tentang item yang dipilih, termasuk data yang terkait dengan item tersebut.
        selected_data = tree.item(selected_item)['values']

        # Mengisi ID dengan data yang terambil pada indeks pertama (ID siswa).
        selected_id.set(selected_data[0])
        # Mengisi nama siswa dengan data pada indeks kedua.
        nama_var.set(selected_data[1])
        # Mengisi nilai Biologi dengan data pada indeks ketiga.
        biologi_var.set(selected_data[2])
        # Mengisi nilai Fisika dengan data pada indeks keempat.
        fisika_var.set(selected_data[3])
        #  Mengisi nilai Bahasa Inggris dengan data pada indeks kelima.
        inggris_var.set(selected_data[4])
    # akan ditangkap jika pengguna mencoba memilih item yang tidak valid atau tidak ada yang dipilih.
    except IndexError:
        # Jika terjadi kesalahan ini, akan muncul pesan kesalahan melalui messagebox.showerror("Error", "Pilih data yg valid!"), meminta pengguna untuk memilih data yang benar.
        messagebox.showerror("Error", "Pilih data yg valid!")


# Inisialisasi database
create_database()

# Membuat GUI dengan tkinter
# Tk() adalah kelas utama dari tkinter yang digunakan untuk membuat aplikasi GUI.
root = Tk()
# menetapkan judul jendela aplikasi menjadi "Prediksi Fakultas Siswa". Ini akan ditampilkan di bagian atas jendela aplikasi.
root.title("Prediksi Fakultas Siswa")
# Membuat warna tampilan
root.configure(bg="#ff7477")

# Variabel tkinter
#StringVar() adalah kelas di tkinter yang digunakan untuk mengelola string yang terikat pada widget.
nama_var = StringVar()
# biologi_var adalah objek StringVar() yang digunakan untuk menyimpan dan mengelola nilai untuk input nilai Biologi.
biologi_var = StringVar()
# # fisika_var adalah objek StringVar() yang digunakan untuk menyimpan dan mengelola nilai untuk input nilai Fisika.
fisika_var = StringVar()
# inggris_var adalah objek StringVar() yang digunakan untuk menyimpan dan mengelola nilai untuk input nilai Bahasa Inggris.
inggris_var = StringVar()
# selected_id adalah objek StringVar() yang digunakan untuk menyimpan nilai ID yang dipilih oleh pengguna (misalnya, untuk memperbarui atau menghapus data).
selected_id = StringVar()

# Element GUI
#Label(root, text="Nama Siswa"): Membuat widget Label yang menampilkan teks "Nama Siswa" di jendela aplikasi root.
# .grid(row=0, column=0): Menempatkan label di posisi baris ke-0, kolom ke-0 dalam grid layout.
# padx=10, pady=5: Memberikan padding horizontal sebesar 10 piksel dan padding vertikal sebesar 5 piksel di sekitar widget.
Label(root, text="Nama Siswa").grid(row=0, column=0, padx=10, pady=5,)

# Entry(root, textvariable=nama_var): Membuat widget Entry (kotak input teks) yang terikat pada variabel nama_var. Ini memungkinkan kita untuk mengambil atau menyimpan nilai yang dimasukkan pengguna ke dalam nama_var.
Entry(root, textvariable=nama_var).grid(row=0, column=1, padx=10, pady=5)

# Label(root, text="Biologi"): Membuat widget Label yang menampilkan teks "Biologi".
Label(root, text="Biologi").grid(row=1, column=0, padx=10, pady=5)
# Entry(root, textvariable=biologi_var): Membuat widget Entry yang terikat pada variabel biologi_var untuk memasukkan nilai Biologi.
Entry(root, textvariable=biologi_var).grid(row=1, column=1, padx=10, pady=5)

# Label(root, text="Fisika"): Membuat widget Label yang menampilkan teks "Fisika".
Label(root, text="Fisika").grid(row=2, column=0, padx=10, pady=5)
#  Entry(root, textvariable=fisika_var): Membuat widget Entry yang terikat pada variabel fisika_var untuk memasukkan nilai Fisika.
Entry(root, textvariable=fisika_var).grid(row=2, column=1, padx=10, pady=5)

# Label(root, text="Bahasa Inggris"): Membuat widget Label yang menampilkan teks "Bahasa Inggris".
Label(root, text="Bahasa Inggris").grid(row=3, column=0, padx=10, pady=5)
# Entry(root, textvariable=inggris_var): Membuat widget Entry yang terikat pada variabel inggris_var untuk memasukkan nilai Bahasa Inggris.
Entry(root, textvariable=inggris_var).grid(row=3, column=1, padx=10, pady=5)

# Membuat tombol Add, Update, dan Delete
# Button(root, text="Add", command=submit): Membuat tombol dengan teks "Add". Ketika tombol ini ditekan, fungsi submit() akan dipanggil.
Button(root, text="Add", command=submit).grid(row=4, column=0, padx=10, pady=5,)
# Button(root, text="Update", command=update): Membuat tombol dengan teks "Update". Ketika tombol ini ditekan, fungsi update() akan dipanggil.
Button(root, text="Update", command=update).grid(row=4, column=1, padx=10, pady=5)
# Button(root, text="Delete", command=delete): Membuat tombol dengan teks "Delete". Ketika tombol ini ditekan, fungsi delete() akan dipanggil.
Button(root, text="Delete", command=delete).grid(row=4, column=2, padx=10, pady=5)

# Tabel untuk menampilkan data
# Mendefinisikan kolom yang akan ditampilkan dalam tabel. Kolom-kolom ini adalah: "ID", "Nama Siswa", "Biologi", "Fisika", "Bahasa Inggris", dan "Prediksi".
columns = ("ID", "Nama Siswa", "Biologi", "Fisika", "Bahasa Inggris", "Prediksi")
# ttk.Treeview() adalah widget dari tkinter untuk menampilkan data dalam bentuk tabel.
# root adalah jendela utama aplikasi tempat Treeview ini ditempatkan.
# columns=columns: Mengatur kolom-kolom yang akan ditampilkan sesuai dengan nilai yang ada dalam variabel columns.
# show="headings": Menampilkan hanya header (judul kolom) tanpa kolom tambahan (seperti kolom yang menunjukkan nomor indeks atau ID internal) di awal tabel.
tree = ttk.Treeview(root, columns=columns, show="headings")
# tree.heading() digunakan untuk mengatur judul kolom dalam tabel.
tree.heading("ID", text="ID")
# Mengatur header kolom "Nama Siswa" menjadi "Nama Siswa".
tree.heading("Nama Siswa", text="Nama Siswa")
# Mengatur header kolom "Biologi" menjadi "Biologi".
tree.heading("Biologi", text="Biologi")
# Mengatur header kolom "Fisika" menjadi "Fisika".
tree.heading("Fisika", text="Fisika")
# Mengatur header kolom "Bahasa Inggris" menjadi "Bahasa Inggris".
tree.heading("Bahasa Inggris", text="Bahasa Inggris")
# Mengatur header kolom "Prediksi" menjadi "Prediksi".  
tree.heading("Prediksi", text="Prediksi")
# Menempatkan Treeview di jendela aplikasi menggunakan grid().
# row=5, column=0: Menempatkan tabel di baris ke-5, kolom ke-0 dalam grid layout.
# columnspan=3: Menyebar tabel ke tiga kolom dalam grid, sehingga tabel akan mengambil ruang dari kolom ke-0, ke-1, dan ke-2.
# padx=10, pady=10: Memberikan padding (jarak) di sekitar tabel untuk memberikan ruang antara tabel dan elemen lainnya di antarmuka.
tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Menyatakan posisi teks di setiap kolom ke tengah
# Mengatur posisi isi tabel di tengah
# Loop ini iterasi melalui setiap elemen dalam list columns yang sebelumnya berisi nama-nama kolom yang akan ditampilkan di tabel (misalnya "ID", "Nama Siswa", "Biologi", dll).
for col in columns:
    # tree.heading(col, text=col.capitalize()) digunakan untuk mengatur teks header untuk setiap kolom.
    tree.heading(col, text=col.capitalize())
    # tree.column(col, anchor="center") digunakan untuk mengatur posisi teks dalam setiap kolom.
    tree.column(col, anchor="center")

# tree.bind("<ButtonRelease-1>", fill_inputs_from_table) menetapkan event handler untuk interaksi klik pada tabel.
tree.bind("<ButtonRelease-1>", fill_inputs_from_table)

#root.mainloop() adalah perintah utama untuk menjalankan aplikasi tkinter.
root.mainloop()