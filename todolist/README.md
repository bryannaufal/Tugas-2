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


## Deskripsi Tugas

Web Design Using HTML, CSS, and CSS Framework

## Jawaban Pertanyaan

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline: Kode css untuk styling ditaruh Sejajar dengan kode HTMLnya
`<h1 class = "text-6xl font-extrabold  text-center mb-6">Sign Up</h1> ` (contoh)
kelebihan
- Tidak perlu buat file lain
- Bagus untuk memantau perubahan-perubahan
kekurangan
- Kode HTML jadi terlalu ramai
- agak nguli untuk masang di tiap element

Internal: Kode css ada di dalam file HTML, tapi tidak sejajar dengan kode HTMLnya melainkan ditaruh bagian paling atas pada kode HTML
kelebihan
- Bisa memanfaatkan id dan class selector
- Tidak perlu buat file lain
kekurangan
- kode HTML jadi terkesan panjang
- loading time membesar

External: Kode css ditaruh berbeda file dengan file HTML
kelebihan
- Kode HTML jadi lebih bersih
- Bisa pakai styling yang sama untuk halaman-halaman yang berbeda
kekurangan:
- Semakin banyak file yang terkoneksi, download time jadi semakin lama

### Jelaskan tag HTML5 yang kamu ketahui.
`<p>` Untuk membuat paragraf
`<h1>` sampai `<h6>` Untuk membuat header
`<div>` Untuk mebagi bagian-bagian pada HTML
`<a>` Untuk mencantumkan hyperlink
`<tr>` Baris dari sebuah tabel
`<td>` Cell dari sebuah tabel
`<img>` Untuk memasukkan image
`<input>` Untuk melakukan input
`<main>` Menandakan konten utama
`<button>` Untuk membuat sebuah tombol


### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
**1. Element Selector**
Mengambil tag dari HTML untuk nantinya properti pada tag tersebut akan diubah-ubah
**2. Id Selector**
Sebuah id dicantumkan pada tag HTML, lalu di file CSS gunakan Id tersebut sebagai selector
**3. Class Selector**
Sebuah class dicantumkan pada tag HTML, lalu di file CSS gunakan class tersebut sebagai selector

id dan class sekilas mirip, tetapi pada file CSS selector id ditulis didahului dengan `#` sedangkan class selector ditulis didahuli dengan `.`
id hanya bisa digunakan hanya satu elemen
class dapat digunakan untuk banyak elemen


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
`<script src="https://cdn.tailwindcss.com"></script>`
Menambahkan Script ini pada base HTML untuk menggunakan tailwind untuk mempercantik tampilan web

Menggunakan Tailwind untuk mempercantik tampilan Web

**Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.**


## Deskripsi Tugas

Javascript dan AJAX

## Jawaban Pertanyaan

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
**Asynchronous Programming**
Program dapat berjalan secara pararel, yang berarti suatu program bisa berjalan tanpa harus menunggu program lainnya berjalan

**Synchronous Programming**
Berlawanan dengan Asynchronous Programming, Synchronous Programming tidak bisa pararel sehingga program hanya bisa dilakukan secara berurutan

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah ketika sebuah event terjadi baru suatu program dapat tereksekusi. Contoh penerapan pada tugas ini adalah ketika tombol Add Task ditekan ketika kita ingin menambahkan suatu Task, setelah tombol ditekan, baru Task ditambahkan.

### Jelaskan penerapan asynchronous programming pada AJAX.
Dengan AJAX, kita dapat melakukan pembaruan pada halaman website tanpa harus mereload seluruhnya.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Menambahkan fungsi baru di views.py
Menambahkan urlpatterns baru di urls.py
Menerapkan jquery pada todolist.html

