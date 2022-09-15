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

![](https://github.com/bryannaufal/Tugas-2/blob/main/assets/Diagram_MVT.png)

Client melakukan request dengan url yang dimasukkan pada browser, lalu request tersebut akan masuk ke server django. Pada `urls.py`, request tersebut akan diarahkan ke `views.py` yang sesuai. Di `views.py` akan terjadi pemrosesan data yang nantinya akan dijadikan response ke client. `views.py` juga mengirimkan query ke `models.py`. `models.py` berguna untuk menghubungkan dengan database sehingga akan terjadi transaksi data antara `models.py` dengan database. `views.py` juga menghubungkan ke `templates` yang berikan file HTML yang merupakan kerangka tampilan dari suatu website. Data yang diperoleh dari `models.py` akan diterima oleh template melalui `views.py`. Hal terakhir yang terjadi adalah response. Setelah data diolah, `views.py` akan merender template lalu akan dikirim ke Client.

#### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual Environment berfungsi untuk mengisolasi environment yang menjadi tempat project kita berjalan. Dengan adanya virtual environment, kita dapat mengembangkan project yang membutuhkan package dengan berbeda-beda versi. Hal ini dapat dilakukan karena masing-masing package akan terisolasi pada environmentnya masing-masing. 

Jika kita ingin menjalankan project yang menggunakan python versi lama, sedangkan pada laptop kita terdapat python versi terbaru, maka kita perlu menghapus python versi terbaru dan meng-install python versi lama yang diperlukan. Agak merepotkan bukan? Dengan virtual environment kita tidak perlu menghapus python versi baru, tetapi python versi baru tersebut dapat berfungsi dengan baik selagi kita menggunakan python versi lama pada project kita. Hal itu, disebabkan karena masing-masing environment saling terisolasi sehingga tidak terjadi clash.

Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, kita akan lumayan kesulitan ketika kita ingin menjalankan project dengan berbeda package yang diperlukan. Jadi penggunaan virtual environment sangat disarankan

#### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
**Poin1**
Di dalam fungsi saya memanggil query ke model database lalu menyimpan hasil query yang diperoleh ke suatu variabel.
```shell
catalog_data = CatalogItem.objects.all()
    context = {
    'catalog_data': catalog_data,
    'nama': 'Rahmat Bryan Naufal',
    'npm': '2106635650'
    }
```
Lalu saya mereturn sebuah halaman HTML yang dirender. Saya juga menambahkan context pada argumen agar context juga dirender sehingga data bisa muncul pada halaman HTML.

**Poin2**
Routings dilakukan pada file urls.py
pada urls.py di folder katalog saya tambahkan kode berikut
```shell
app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

pada urls.py di folder project_django saya menambahkan path pada urlpatterns
```shell
path('katalog/', include('katalog.urls'))
```
Dengan melakukan kedua hal di atas, ketika kita dapat mengakses halaman katalog dengan memasukkan url dengan /katalog

**Poin3**
Context yang ikut dirender pada poin 1 perlu saya masukkan pada template HTML menggunakan sintaks Django. Saya melakukan iterasi kepada catalogs. Iterasi tersebut masih berupa objek sehingga kita perlu memanggil atributnya secara langsung. Berikut kode yang ditambahkan pada template HTML katalog:
```shell
{% for catalog in catalog_data %}
      <tr>
        <th>{{ catalog.item_name }}</th>
        <th>{{ catalog.item_price }}</th>
        <th>{{ catalog.item_stock }}</th>
        <th>{{ catalog.rating }}</th>
        <th>{{ catalog.description }}</th>
        <th>{{ catalog.item_url }}</th>
      </tr>
    {% endfor %}
```
**Poin4**
Pertama-tama, saya membuat aplikasi baru pada Heroku, lalu simpan nama aplikasi tersebut beserta key account saya. Lakukan pull, add, commit, dan push repositori tugas-2 yang ada di lokal. Setelah itu, kita perlu menambahkan dua variabel repositori secret pada github. Variabel tersebut digunakan untuk menyimpan nama aplikasi pada heroku dan juga key heroku saya. Setelah itu, kita dapat mendeploy aplikasi kita.

## Link Aplikasi Katalog Tugas-2
Berikut link yang dapat diakses untuk membuka aplikasi yang sudah berhasil di-deploy
[PBP-Tugas-2](https://katalog-tugas-2.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.