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

# Tugas 5

1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    - Inline styles (misalnya, style="...") memiliki prioritas tertinggi.    
    - ID selectors (misalnya, #id) memiliki prioritas lebih tinggi daripada class, attribute, dan pseudo-class selectors.
    - Class selectors, attribute selectors, dan pseudo-class selectors (misalnya, .class, [attribute], :hover) memiliki prioritas lebih tinggi daripada element selectors.
    - Element selectors dan pseudo-element selectors (misalnya, div, :before) memiliki prioritas terendah.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
    Alasan : Karena dapat membantu website untuk menyesuaikan tampilannya
    based screen size perangkat apa yang dipakai oleh user. Sehingga, dapat make sure konten dapat diakses oleh semua pengguna, termasuk mereka yang menggunakan perangkat dengan layar kecil atau bahkan di berbagai perangkat, baik itu desktop, tablet, atau ponsel.

    Contoh : Apilkasi yang sudah mengimplementasikan responsice design yang saya ketahui yaitu Twitter, Instagram, Traveloka, dan lain-lain. Sementara itu, untuk aplikasi yang belum mengimplementasikannya mungkin cukup sulit untuk lebih spesifiknya tapi biasanya adalah situs web lama, situs web pemerintahan, atau situs web perusahaan.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    - Margin: Ruang di luar border elemen. Digunakan untuk memberikan jarak antara elemen.
    - Border: Garis yang mengelilingi padding dan konten elemen. Digunakan untuk memberikan batas visual pada elemen.
    - Padding: Ruang di dalam border elemen, antara border dan konten. Digunakan untuk memberikan ruang di dalam elemen.

5. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    - Flex Box : Digunakan untuk mengatur tata letak elemen dalam satu dimensi (baris atau kolom). Berguna untuk membuat tata letak yang fleksibel dan responsif.
    - Grid Layout: Digunakan untuk mengatur tata letak elemen dalam dua dimensi (baris dan kolom). Sangat berguna untuk membuat tata letak yang kompleks dan responsif.

6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    (a.) Pertama, saya menambahkan tag <meta name="viewport"> agar screen size dapat disesuaikan dengan peranggkat user
    (b.) Lalu, menambahkan script CDN untuk menyambungkan Django dengann tailwind
    (c.) Kemudian, saya membuat fungsi baru yaitu edit_item_barang pad aviews.py agar user bisa mengedit produk yang sudah di add.
    (d.) Membuat file html baru dengan nama edit_item_barang dan membuat template di file tersebut 
    (e.) Tidak lupa membuat route dari url dengan mengimport fungsi edit_item_barang dan menambahkan path url agar bisa mengakses import an tadi
    (f.) lalu, membuat fungsi baru yaitu delete_item_barang untuk user menghapus item yang sudah di add
    (g.) Membuat file html baru dengan nama delete_item_barang dan membuat template di file tersebut 
    (h.) Tidak lupa membuat route dari url dengan mengimport fungsi delete_item_barang dan menambahkan path url agar bisa mengakses import an tadi.
    (i.) Menambahkan button edit dan hapus pada main.html
    (j.) Menambahkan navigation bar dengan membuat file html baru dan diisi dengan design serta header apa saja yang dibutuhkan.
    (k.) Tidak lupa agar navbar akan terus ada di setiap page, harus menambahkan include 'navbar.html' pada add_barang_item, edit_item_barang, dan delete_item_barang
    (l.) Menambahkan middleware WhiteNoise pada settings.py, Django dapat mengelola file statis secara otomatis dalam mode produksi (DEBUG=False) tanpa perlu konfigurasi yang kompleks
    (m.) Kemudian, untuk step ui/ux nya saya membuat file css pada root dir dan menghubungankannya ke file base.html. Lalu, melakukan styling design2 di masing2 page html yang menurut saya imut dan lucu xixixi.
    (n.) Selanjutnya, saya menambahkan card product agar dapat ditampilkan produk yang sudah di add oleh user di main page beserta detail dari produk tersebut seperti nama, harga, desc, dan kategori.
    (o.) Selesaii deh, tidak lupa untuk melakukan add-commit-push ke GitHub.