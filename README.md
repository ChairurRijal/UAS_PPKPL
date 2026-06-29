# ⚓ Sistem Informasi Inspeksi Kapal Berbasis NDT - Automated Regression Test

Repositori ini dibuat sebagai bukti pemenuhan **Ujian Akhir Semester (UAS)** mata kuliah **Pengujian dan Penjaminan Kualitas Perangkat Lunak (PKPL)**.

## 👥 Identitas Kelompok 1
* **Jovan Gilbert N.** - NIM: 2110817xxxxxx (Mewakili Kelompok 1)

**Program Studi:** Teknologi Informasi  
**Fakultas:** Teknik  
**Universitas:** Universitas Lambung Mangkurat  

---

## 📝 Cakupan Pengujian
Repositori ini berisi skrip otomatisasi pengujian regresi menggunakan **Python & Selenium WebDriver** untuk memvalidasi:
* **TC-R03:** Validasi pengisian beruntun 5 titik koordinat pengujian ketebalan pelat lambung kapal (Ultrasonic Testing) ke *Protected Zone* pasca-perubahan skema data.

## 🚀 Pipeline CI/CD (GitHub Actions)
Pengujian ini telah terintegrasi dengan GitHub Actions. Setiap kali ada perubahan atau upload file, robot GitHub akan otomatis mengeksekusi pengujian ini secara *headless* di server Ubuntu.
