# Tugas-2 (PBP)

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama : Rahmat Bryan Naufal**
**NPM : 2106635650**
**Kelas : PBP-C**

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Deskripsi Tugas

mengimplementasikan konsep Model-View-Template

## Jawaban Pertanyaan

#### 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![](assets/Diagram_MVT.PNG)

Client melakukan request dengan url yang dimasukkan pada browser, lalu request tersebut akan masuk ke server django. Pada `urls.py`, request tersebut akan diarahkan ke `views.py` yang sesuai. Di `views.py` akan terjadi pemrosesan data yang nantinya akan dijadikan response ke client. `views.py` juga mengirimkan query ke `models.py`. `models.py` berguna untuk menghubungkan dengan database sehingga akan terjadi transaksi data antara `models.py` dengan database. `views.py` juga menghubungkan ke `templates` yang berikan file HTML yang merupakan kerangka tampilan dari suatu website. Data yang diperoleh dari `models.py` akan diterima oleh template melalui `views.py`. Hal terakhir yang terjadi adalah response. Setelah data diolah, `views.py` akan merender template lalu akan dikirim ke Client.

#### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual Environment berfungsi untuk mengisolasi environment yang menjadi tempat project kita berjalan. Dengan adanya virtual environment, kita dapat mengembangkan project yang membutuhkan package dengan berbeda-beda versi. Hal ini dapat dilakukan karena masing-masing package akan terisolasi pada environmentnya masing-masing. 

Jika kita ingin menjalankan project yang menggunakan python versi lama, sedangkan pada laptop kita terdapat python versi terbaru, maka kita perlu menghapus python versi terbaru dan meng-install python versi lama yang diperlukan. Agak merepotkan bukan? Dengan virtual environment kita tidak perlu menghapus python versi baru, tetapi python versi baru tersebut dapat berfungsi dengan baik selagi kita menggunakan python versi lama pada project kita. Hal itu, disebabkan karena masing-masing environment saling terisolasi sehingga tidak terjadi clash.

Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, kita akan lumayan kesulitan ketika kita ingin menjalankan project dengan berbeda package yang diperlukan. Jadi penggunaan virtual environment sangat disarankan

#### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
**Poin1**


## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.