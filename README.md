# Tugas 3

link gdrive berisikan postman : https://drive.google.com/drive/folders/1QivGeecT-umbTiFUjjYXr-ATrA5_YQWt?usp=sharing 

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery dapat membuat komunikasi yang efektif dan efesien, sehingga data dapat ditransfer secara akurat dan tepat waktu. Selain itu, data delivery juga memastikan bahwa semua bagian platform memiliki informasi yang sama dan data harus disinkronkan secara real-time. Dengan mekanisme data delivery yang baik, data dapat dikirimkan dengan cara yang konsisten, mengurangi risiko kehilangan data atau ketidaksesuaian data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, dibanding XML, JSON memiliki kelebihan yang lebih unggul. Beberapa kelebihannya yaitu :
        - JSON memiliki file size yang lebih kecil sehingga membuat transmisi data lebih cepat
        - JSON lebih sederhana, mudah dibaca, dan mudah dipahami ketika sedang bekerja dengan struktur data kompleks
        - JSON lebih intuitif, dimana secara langsung merepresentasikan struktur daya seperti list, dict, dan int.
    Namun, dalam konsep metadata, XML lebih cocok digunakan karena memiliki fitur semacamatribute, schema, dan namesapece.
    Selanjutnya, JSON bisa dibilang cukup populer disebabkan pada app web modern zaman sekarang sering sekali menggunakan JavaScript. Maka dari itu, JSON lebih efisien untuk pertukaran data antara server dan klien dalam format RESTful API.

3.  Jelaskan fungsi dari method is_valid() pada form Django! Mengapa kita membutuhkan method tersebut?
    Method is_valid() digunakan untuk mengecek apakah data kita sudah sesuai dengan aturan validasi yang udah didefinisikan belum pada form. Jika form sudah valid, maka data yang sudah ter-validate akan disimpan di form.cleaned_data. Sehingga, hal ini memungkinkan kita untuk mengakses data yang sudah dibersihkan dan terverifikasi.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    CSRF adalah sebuah serangan cyber pada suatu website tertentu yang di mana penyerang mencoba memanipulasi pengguna untuk mengirimkan permintaan yang tidak diinginkan ke server tanpa sepengetahuannya.

    Maka dari itu, kita harus membuat csrf_token saat membuat form agar aplikasi kita dapat terlindungi dari serangan tersebut. Kelebihan dari token ini yaitu token akan memastikan bahwa permintaan yang dikirim dari form benar-benar berasal dari pengguna yang sah. Jika token ini tidak ada atau tidak valid, Django akan menolak permintaan tersebut.

    Jika kita tidak menambahkan csrf_token, aplikasi kita rentan terhadap serangan CSRF, di mana penyerang dapat mengirimkan permintaan yang valid atas nama pengguna tanpa sepengetahuannya, seperti mengirimkan form untuk melakukan pembelian, penghapusan akun, atau mengubah data penting.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    (a.) Pertama, saya membuat direktori templates pada direktori utama (root folder) dan membuat file HTML baru bernama base.html

    (b.) Lalu, saya menambahkan konten 'templates' pada settings.py yang ada pada direktori proyek (Altique) dan pada baris yang mengandung variabel TEMPLATES. Agar file base.html terdeteksi sebagai file template

    (c.) Lalu mengubah isi kode dari templates/main dengan menambahkan : {% extends 'base.html' %}
    dimana digunakan agar base.html sebagai template utama

    (d.) Selanjutnya, saya membuat file forms.py yang berisikan code saya untuk membuat struktur forms yang akan menerima data item barang ke dalam file forms.py

    (e.) Lalu, pada file views.py saya menambahkan import render dan juga fungsi baru yaitu add_item_barang. Dan tidak lupa untuk menambahkan path url pada urls.py pada main.

    (f.) Kemudian, saya membuat file HTML baru pada main/templates dengan nama add_item_barang.html

    (g.) Lalu, saya meng-import Httpresponse dan Serializer dan membuat fungsi baru yang nerima parameter req dengan nama show_xml yang akan menembalikan function berupa httpresponse yang isinya hasil query yang sudah di serialisasi menjadi XML.

    (h.) Kemudian, saya membuat get function untuk menadapatkan id dari XML dan JSOn dengan membuat function show_xml_by_id dan show_json_by_id. Dan tidak lupa menambahkan ke files path urls serta hasil import-an tadi.

    (i.) Terakhir, saya menjalankan project saya di django terlebih dahulu baru saya membuat request baru di app postman dan mengecek apakah data saya terkirim dengan baik dengan menambahkan id dari input-an web saya.

    (j.) Tidak lupa saya deploy hasil saya ke github dan juga PWS.

# Tugas 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
    - HttpResponseRedirect() : salah satu class di Django yang langsung mengirim response HTTP 302 yang memberi tahu browser untuk melakukan pengalihan ke URL yang sudah ditentukan. Ini juga salah satu bagian dari django.http, sehingga jika ingin menggunakannya harus import terlebih dahulu. Selain itu, diperlukan URL lengkap  secara eksplisit sebagai argumen untuk menarahkan user.
    - redirect() : fungsi ini yang membuat HttpResponseRedirect atau respons pengalihan lain seperti HttpResponsePermanentRedirectlebih mudah. Fungsi ini adalah bagian dari modul django.shortcuts, sehingga jika ingin menggunakannya harus import terlebih dahulu. Selain itu, redirect() lebih sering digunakan karena kemudahannya dalam menghasilkan URL dan fleksibilitas dalam menentukan jenis pengalihan.

2.  Jelaskan cara kerja penghubungan model Product dengan User!
    Menghubungkan model Product dengan model User dilakukan untuk merepresentasikan relasi seperti kepemilikan produk oleh user. Cara yang biasanya dilakukan untuk menghubungkan kedua model ini adalah melalui relasi ForeignKey, yang mengizinkan setiap produk untuk dihubungkan dengan satu pengguna. Berikut ini adalah penjelasan tentang cara kerja penghubungan ini:

    (a.) Import model User dari Django atau model khusus yang telah dibuat.

    (b.) Definisikan model Product Anda dan tambahkan sebuah field ForeignKey yang merujuk ke model User.

    (c.) Pakai Field ForeignKey, dengan menggunakan "settings.AUTH_USER_MODEL" untuk merujuk ke model user yang aktif. Lalu, "on_delete=models.CASCADE" agar produk dihapus secara otomatis jika pengguna yang terkait dihapus. "related_name='products'" untuk mengakses produk dari sisi user, seperti user.products.all().

    (d.) Tambahkan field lain yang diperlukan untuk model Product, seperti name, description, dan price.

    (e.) Dalam views atau templates Django, dapat mengakses produk yang terhubung dengan user tertentu dengan menggunakan related_name yang telah ditetapkan.
 
 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    - Authentication : Proses verifikasi identitas pengguna. Melibatkan langkah-langkah untuk make sure bahwa pengguna adalah siapa yang mereka klaim. Misal, kalau kita mau masuk menggunakan username dan password, autentikasi berbasis token, dan penggunaan OTP (One Time Password).

    - Authorization : Proses menentukan apa yang diizinkan untuk dilakukan oleh pengguna yang telah terotentikasi. Jadi, akan muncul pertanyaan "apa yang Anda diizinkan untuk lakukan?" dan menetapkan hak akses pengguna terhadap sumber daya atau fungsi tertentu dalam sistem. Misal, seorang user terotentikasi mendapat akses untuk mengedit profil mereka sendiri tetapi tidak dapat mengakses halaman admin kecuali mereka memiliki peran atau izin yang sesuai.

    Django mengimplementasikan kedua konsep tersebut dengan cara :
        - Authenication : Django menyediakan framework django.contrib.auth yang mengatur sebagian besar aspek autentikasi. Ini termasuk:
            * Model User untuk menyimpan pengguna dan atribut mereka.
            * Sistem form untuk autentikasi seperti AuthenticationForm.
            * View yang sudah jadi seperti login dan logout untuk mengelola sesi pengguna.
            * Middleware untuk mengelola sesi dan mengasosiasikan pengguna dengan setiap request. 
        
        - Authorization :  Django mengelola otorisasi melalui bbrp fitur antara lain :
            * Permisson: Django memiliki sistem permissions yang dapat didefinisikan per model dan digunakan untuk mengontrol akses CRUD (Create, Read, Update, Delete) pada objek tersebut.
            * Groups: Pengguna dapat dikelompokkan, dan permissions dapat diberikan ke seluruh grup.
            * Decorators: Django menyediakan decorators seperti permission_required dan user_passes_test untuk membatasi akses ke view berdasarkan kriteria tertentu.
    

 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
    Django dapat mengingat user yang telah login melalui penggunaan cookies dan sesi, dan berikut cara kerjanya:
    - Cookies : Saat user berhasil login, Django mengatur cookie pada browser user. Cookie tersebut berisi ID sesi yang unik. Lalu, Cookie  dikirimkan kembali ke server pada setiap request yang dilakukan oleh browser, sehingga Django dapat mengidentifikasi bahwa request tersebut berasal dari user yang sama. 
    - Sesi : Django menggunakan tabel database untuk menyimpan data sesi. Setiap sesi memiliki kunci yang sesuai dengan ID sesi yang disimpan dalam cookie. Data dalam sesi bisa berisi berbagai informasi seperti ID user dan data lain yang diperlukan selama user masih login. Saat server menerima request dengan cookie sesi, Django mencari ID sesi dalam tabel sesi. Jika ditemukan, server dapat memulihkan konteks user dan mengenali user tersebut.

    Kegunaan lain dari cookies adalah untuk menyimpan preferensi user, melacak perilaku user di situs web, dan mempertahankan status login user saat berpindah antar halaman.

    Untuk keamanan cookies, tidak semua cookies aman. Maka dari itu, ada beberapa aspek yang perlu diperhatikan dalam penggunaan cookies untuk menjaga keamanan. Untuk mencegah hal yang tidak diinginkan bisa dilakukan beberapa hal berikut:
    - Cookie harus ditandai sebagai HttpOnly, yang membuatnya tidak dapat diakses melalui JavaScript di sisi klien.
    - Cookies harus ditandai sebagai Secure, yang berarti cookie hanya akan dikirim melalui koneksi HTTPS.
    - Atribut SameSite dapat digunakan untuk mengontrol pengiriman cookies dengan request yang dibuat oleh situs lain.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    (a.) Menambahkan import UserCreationForm dan messages pada bagian paling atas views.py
    (b.) Lalu, menambahkan fungsi register pada file tersebut.
    (c.) Kemudian, membuat file HTML baru dan manamakannya dengan register.html pada main/templates.
    (d.) Tidak lupa menambahkan import register dan path urls register pada urls,py.
    (e.) Membuat fungsi login dengan menambahkan import authenticate, login, dan AuthenticationForm pada bagian paling atas di views.py.
    (f.) Lalu, buat fungsi login user di views.py dan buat file baru HTML dengan nama login.html pada main/templates
    (g.) Tidak lupa menambahkan import login_user dan path urls login_user pada urls,py.
    (h.) Kemudian, membuat fungsi logout dengan meng-import logout dan menambahkan fungsi logout_user pada views.py
    (i.) Lalu, menambahkan button logout pada main.html pada main/templates. Tidak lupa menambahkan import loout_user dan path urls logout_user pada urls.py.
    (j.) Setelah itu, lakukan restriksi akses halaman main dengan meng-import login_required pada bagian paling atas pada views.py
    (k.) Lalu, menambahkan "@login_required(login_url='/login')" diatas fungsi show_main
    (l.) Untuk menambahkan data last login dan menampilkannya ke halaman main, tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas padaview.py
    (m.) Lalu, menambahkan fungsionalitas menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. 
    (n.) Menambahkan kode "'last_login': request.COOKIES['last_login'] ke dalam variabel context." pada fungsi show_main
    (o.) Untuk menghubungkan model ItemBarang dengan user, tambahkan import User pada models.py
    (p.) Lalu, menambahkan kode "user = models.ForeignKey(User, on_delete=models.CASCADE)" pada class ItemBarang
    (q.) Kemudian, megubah value dari ItemBarang dan context menjadi "'name': request.user.username," pada show_main
    (r.) Setelah, itu melakukan python manage.py makemigration dan migrate
    (s.) Terakhir, ganti variabel DEBUG dari berkas settings.py menjadi seperti ini 'PRODUCTION = os.getenv("PRODUCTION", False); DEBUG = not PRODUCTION'
    (t.) Tidak lupa melakukan add, commit dan push untuk memperbarui repositori GitHub.