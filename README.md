1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

(a.) Saya membuat pryek dhango baru dengan memasukkan perintah berikut di cmd folder PBP saya dengan nama "Altique": 
django-admin startproject Altique

(b.) Setelah proyek dibuat, saya membuat aplikasi bernama main menggunakan perintah:
python manage.py startapp main

(c.) Lalu, saya melakukan routing di Altique/urls.py agar aplikasi main dapat dijalankan, dengan cara menambahkan kode:
from django.urls import include
urlpatterns = [
    path('', include('main.urls')),
]

(d.) Kemudian, pada main/models.py, saya membuat model Product dengan atribut name, price, dan description:
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

(e.) Setelah itu, saya membuat fungsi product_list di main/views.py untuk mengambil semua data produk dari database dan mengirimkannya ke template:
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

(f.) Terakhir, saya membuat routing di main/urls.py untuk fungsi product_list agar dapat diakses:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]

(g.) Tidak lupa untuk melakukan deploy ke PWS setelah saya sudah menge-cek proyek saya berjalan dengan baik.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Visualisasi proses : 
Client Request --> urls.py --> views.py --> models.py --> templates --> Client Response

(a.) Client request : User mengirimkan request dengan mengakses URL tertentu di browser.
(b.) urls.py : Django akan mapping URL yang diakses oleh user ke fungsi view yang sesuai. 
(c.) views.py : Terjadinya pemrosesan logika bisnis dan meminta data dari models.py
(d.) models.py : Django ORM mengambil data dari database sesuai dengan model yang telah didefinisikan.
(e.) templates : Data yang didapat dari models kemudian diolah dan ditampilkan di template dalam bentuk HTML.
(f.) Client response : Hasil akhir yang berbentuk HTML dan dikirim kembali ke browser untuk ditampilkan kepada user.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
(a.) Version control: Git dapat membuat developer untuk melacak perubahan kode secara historis. Jadi, setiap perubahan yang dilakukan dapat dicatat dan dikembalikan jika diperlukan.
(b.) Collaborative development: Git dapat membuat beberapa developer untuk bekerja pada proyek yang sama secara bersamaan tanpa saling menimpa pekerjaan satu sama lain. 
(c.) Branching: Git menyediakan fitur branch yang memungkinkan developer untuk bekerja pada fitur baru atau bug fixes secara independen tanpa mengganggu kode yang ada. Sehingga, dapat meminimalisir ke-error-an kode akibat perubahan yang dilakukan.
(d.) Backup & Recovery: Dengan menggunakan layanan seperti GitHub atau GitLab, proyek disimpan secara aman di cloud dan dapat diambil kembali jika terjadi masalah.

4.  Menurut anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Sesuai yang saya ketahui, framework Django menyediakan banyak fitur seperti ORM, form handling, user authentication, dan admin panel, yang memudahkan beginner developer untuk fokus pada logika aplikasi tanpa harus memulai semuanya dari awal. Selain itu, Django menerapkan pola Model-View-Template yang rapi, dimana pola tersebut merupakan pola arsitektur umum dalam pengembangan aplikasi web. Selebihnya, Django adalah salah satu framework yang banyak digunakan di dunia industri saat ini.

5. Mengapa model pada Django disebut sebagai ORM?

Hal tersebut disebabkan karena Django dapat berinteraksi dengan database menggunakan objek Python, bukan dengan query SQL langsung. Pada Django juga memudahkan para developer untuk menggunakan kelas dan objek Python tanpa perlu menulis query SQL secara manual. Dengan ORM, interaksi dengan database lebih aman dari kesalahan sintaks SQL, dan juga memastikan data yang konsisten.