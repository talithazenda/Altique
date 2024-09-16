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
