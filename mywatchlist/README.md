# Tugas-3 (PBP)

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama : Rahmat Bryan Naufal**
**NPM : 2106635650**
**Kelas : PBP-C**

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Deskripsi Tugas

Pengimplementasian Data Delivery Menggunakan Django

## Jawaban Pertanyaan

#### Jelaskan perbedaan antara JSON, XML, dan HTML!

*JSON (JavaScript Object Notation)*
JSON digunakan untuk menyimpan, membaca, serta menukar informasi dari web server agar dapat dilihat oleh pengguna. JSON sendiri dapat digunakan oleh berbagai bahasa pemrograman. JSON menyimpan elemennya secara efisien tapi tidak begitu rapi ketika dilihat. JSON juga punya array yang membuat transfer data lebih mudah

*XML (Extensible Markup Language)*
Sama seperti JSON, XML digunakan untuk menyimpan, membaca, serta menukar informasi dari web server agar dapat dilihat oleh pengguna. XML menyimpan elemennya lebih terstruktur tapi lebih tidak efisien dibandingkan JSON.

*HTML (Hypertext Markup Language)*
HTML digunakan sebagai kerangka dari suatu website. HTML biasanya digunakan bersama dengan CSS untuk mempercantik tampilan website

#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Sebuah website atau aplikasi yang dinamis tentu bisa menampilkan dan menerima banyak dan berbagai macam jenis data. Untuk mengirim dan menerima data tersebut agar dapat dipahami oleh kita sebagai manusia dan program komputer maka terdapat ketentuan-ketentuan atau format tertentu dalam mengerim dan menerima data tersebut. JSON, XML, dan HTML merupakan beberapa dari ketentuan dan format yang digunakan untuk data_delivery.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
**Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu**
Saya membuka folder yang sama dengan tugas 2 kemarin melalui cmd, lalu nyalakan virtual environment. Setelah itu, saya menjalankan perintah `python manage.py startapp mywatchlist` sehingga django app `mywatchlist` terbuat.

**Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist**
Pertama-tama saya menambahkan `mywatchlist` pada `INSTALLED_APPS` yang terletak pada file `settings.py` di folder `project_django` untuk mendaftarkan app mywatchlist. Selanjutnya, saya melakukan routings.
Routings dilakukan pada file urls.py
pada urls.py di folder mywatchlist saya tambahkan kode berikut
```shell
app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]
```
show_mywatchlist akan dibuat di `views.py` pada nantinya.

**Membuat sebuah model MyWatchList yang memiliki atribut sebagai berikut:**
Pebmuatan model dilakukan di `models.py` pada foder `mywatchlist`. Pertama-tama, saya membuat class `MyWatchList` yang memiliki atribut-atribut yang sudah ditentukan dengan data types yang menyesuaikan setiap atribut. Setelah itu, saya menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi.

**Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas**
data dibuat pada file `initial_mywatchlist_data.json` pada folder `fixtures`. Data yang dibuat berupa JSON.

**Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:**
Untuk menyajikan data dalam HTML, saya membuat fungsi `show_mywatchlist` pada file `views.py`. Fungsi tersebut akan mengembalikan HttpResponse dengan parameter mywatchlist.html dan juga context.
Untuk menyajikan data dalam JSON, saya membuat fungsi `show_json` dan `show_json_by_id` pada file `views.py` yang akan mereturn HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json".
Untuk menyajikan data dalam XML, saya membuat fungsi `show_xml` dan `show_xml_by_id` pada file `views.py` yang akan mereturn HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml".

**Membuat routing sehingga data di atas dapat diakses melalui URL:**
*http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML*
`path('html/', show_mywatchlist, name='show_mywatchlist')` Menambahkan kode tersebut pada `urlpatterns`

*http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML*
`path('xml/', show_xml, name='show_xml')` Menambahkan kode tersebut pada `urlpatterns`

*http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON*
`path('json/', show_json, name='show_json')` Menambahkan kode tersebut pada `urlpatterns`

**Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
Variabel `HEROKU_API_KEY` dan `HEROKU_APP_NAME` sudah berhasil ditambahkan pada tugas sebelumnya. Lalu, pada `Procfile` tamabahkan `python manage.py loaddata initial_mywatchlist_data.json` agar data dapat ke load di heroku.

## Link Aplikasi Katalog Tugas-2
Berikut link yang dapat diakses untuk membuka aplikasi yang sudah berhasil di-deploy
[PBP-Tugas-2](https://katalog-tugas-2.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.

#### Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
![](https://github.com/bryannaufal/Tugas-2/blob/main/mywatchlist/assets/mywatchlist_html.png)
![](https://github.com/bryannaufal/Tugas-2/blob/main/mywatchlist/assets/mywatchlist_json.png)
![](https://github.com/bryannaufal/Tugas-2/blob/main/mywatchlist/assets/mywatchlist_xml.png)