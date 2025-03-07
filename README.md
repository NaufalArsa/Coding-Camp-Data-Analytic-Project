# 🚴 Bike Rental Dashboard - Streamlit

Selamat datang di **Bike Rental Dashboard**, sebuah aplikasi interaktif berbasis **Streamlit** untuk menganalisis data penyewaan sepeda! 📊🚴‍♂️

---

## 📌 **Fitur Utama**
✅ Visualisasi data penyewaan sepeda berdasarkan musim & cuaca 🌤️❄️  
✅ Perbandingan penyewaan antara hari kerja dan hari libur 🏢🏖️  
✅ Analisis kategori penyewaan sepeda 📈  
✅ RFM (Recency, Frequency, Monetary) Analysis untuk memahami pola sewa pelanggan 📊  
✅ Grafik interaktif untuk eksplorasi lebih dalam 🔍  

---

## 🚀 **Cara Menjalankan Dashboard**

### **1️⃣ Clone Repository**
Jika belum memiliki kode, clone repository ini terlebih dahulu:
```sh
git clone https://github.com/your-username/streamlit-bike-rental.git
cd streamlit-bike-rental
```

### **2️⃣ Siapkan Virtual Environment (Opsional tapi Direkomendasikan)**
```sh
conda create --name main-ds python=3.12
conda activate main-ds
```

### **3️⃣ Install Dependencies**
Pastikan semua dependensi sudah terinstall dengan menjalankan perintah:
```sh
pip freeze > requirements.txt
```

### **4️⃣ Jalankan Aplikasi Streamlit**
```sh
streamlit run app.py
```
📍 Aplikasi akan berjalan di **http://localhost:8501**

---

## 📂 **Struktur Direktori**
```
streamlit-bike-rental/
│-- data/                # Folder berisi dataset CSV
│   ├── day.csv          # Data penyewaan harian
│   ├── hour.csv         # Data penyewaan per jam
│-- app.py               # File utama untuk menjalankan Streamlit
│-- requirements.txt     # Daftar dependensi yang diperlukan
│-- README.md            # Dokumentasi proyek ini
```

---

## 🛠 **Masalah & Solusi**
Jika mengalami error **FileNotFoundError: No such file or directory: 'data/day.csv'**, pastikan bahwa:
1. File CSV ada di dalam folder `data/`.
2. Jalankan kode ini untuk mengecek apakah file ada:
   ```python
   import os
   print(os.listdir("data"))
   ```

Jika masih mengalami masalah, silakan ajukan **Issue** di repository ini. 😊

---

## 🤝 **Kontribusi**
Ingin berkontribusi? Yuk ikut serta!
1. Fork repository ini 🍴
2. Buat branch baru (`git checkout -b feature-namaFitur`) 🌱
3. Commit perubahan (`git commit -m "Menambahkan fitur XYZ"`) ✨
4. Push ke GitHub (`git push origin feature-namaFitur`) 🚀
5. Buat Pull Request ✅

---

## 📞 **Kontak & Dukungan**
Jika Anda memiliki pertanyaan atau saran, jangan ragu untuk menghubungi saya di:
📧 Email: naufal.arsa.27@gmail.com  
🐙 GitHub: [NaufalArsa](https://github.com/NaufalArsa)  
Terima kasih telah menggunakan **Bike Rental Dashboard**! 🚴‍♂️📊

