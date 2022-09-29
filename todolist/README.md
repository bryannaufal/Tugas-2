# Tugas-4 (PBP)

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama : Rahmat Bryan Naufal**
**NPM : 2106635650**
**Kelas : PBP-C**

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Deskripsi Tugas

Pengimplementasian Form dan Autentikasi Menggunakan Django

## Jawaban Pertanyaan

#### Apa kegunaan `{% csrf_token %}` pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

csrf_tokem berfungsi untuk melindungi dari Cross-Site Request Forgery attack. Token berupa value acak yang panjang sehingga sulit untuk ditebak dan token harus berbeda di setiap user session. Token tersebut akan digunakan sebagai parameter tambahan ketika ingin menjalankan suatu syntax pada suatu website. Oleh karena itu, hanya web tersebut sajalah yang bisa menjalankan syntax karena terdapat tokennya, sedangkan web lain tidak dapat menjalankan syntax pada sesuatu web karena tidak punya tokennya.
Jadi jika tidak ada potongan kode `{% csrf_token %}` pada elemen `<form>` maka website lain dapat menjalankan syntax ke suatu web karena tidak diperlukan token

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Kita dapat membuat elemen `<form>` secara manual. Caranya adalah dengan membuat field input pada HTML dan juga button untuk mengeksekusi POST request ke dalam server. Dengan membuat `<form>` secara manual, kita dapat membuatnya dengan tampilan yang lebih fleksibel (bebas semua kita).

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user menakan tombol submit, maka HTTP request, beserta method dan agumennya di kirim ke server. Di server, akan ditentukan views.py mana yang diperlukan. Setelah itu, segala hal yang di request di lakukan, seperti penyimpanan data ke database. Setelah itu, server akan kembali meresponse dengan menampilkan template yang sesuai. Data yang telah diubah juga dapat ditampilan pada template tertentu ke user.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

**Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.**
Saya membuka folder yang sama dengan tugas 2 kemarin melalui cmd, lalu nyalakan virtual environment. Setelah itu, saya menjalankan perintah `python manage.py startapp todolist` sehingga django app `todolist` terbuat. Lalu tambahkan `todolist` pada `INSTALLED_APPS` yang terdapat pada settings.py yang berlokasi di folder project_django.

**Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.**

Routings dilakukan pada file urls.py
pada urls.py di folder todolist saya tambahkan kode berikut
```shell
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
]
```
Fungsi show_todolist akan dibuat di `views.py` pada nantinya.

pada `urlpatterns` di `urls.py` di folder project_django tambahkan `path('todolist/', include('todolist.urls'))`
```shell
urlpatterns = [
    path('todolist/', include('todolist.urls')),
]
```
**Membuat sebuah model Task yang memiliki atribut sebagai berikut:**

Pebmuatan model dilakukan di `models.py` pada foder `todolist`. Pertama-tama, saya membuat class `Task` yang memiliki atribut-atribut yang sudah ditentukan dengan data types yang menyesuaikan setiap atribut. Setelah itu, saya menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi.

**Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**

Di `views.py` membuat fungsi register, login_user, logout user. Lalu buat template berupa file HTML untuk menampilkan form regis, form login, dan juga tombol logout. `@login_required(login_url='/todolist/login/')` tambahkan kode diatas pada sebelum fungsi-fungsi di `views.py` yang memerlukan login untuk mengaksesnya.

**Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.**

Halaman utama todolist dibuat pada file `todolist.html`

**Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**

Halaman untuk pembuatan task dibuat pada file `form_task.html`

**Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:**

Pada `urls.py` pada folder todolist tambahakan
```shell
path('', show_todolist, name='show_todolist'),
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('create-task/', create_task, name='create-task'),
path('<id>/delete/', delete_task, name='delete-task'),
path('<id>/update/', update_task, name='update-task'),
```
pada urlpatterns.

**Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

Karena repositori sudah terhubung dengan hereko dari tugas-tugas sebelumnya, maka kita hanya perlu add commit dan push. Setelah itu, tunggu web di deploy dan web bisa diakses melalui internet.