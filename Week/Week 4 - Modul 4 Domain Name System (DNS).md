# Modul 4 Domain Name System (DNS)
Nama : Rovino Ramadhani <br>
NIM : 103072400031 <br>
Kelas : IF-04-01

## Penjelasan
### 1. Fungis ifconfig -a
![Screenshot Contoh ifconfig -a](../Assets/week4/modul4/sc_pj1.avif)
Perintah `ifconfig -a` digunakan untuk menampilkan semua network interface pada sistem, baik yang aktif maupun tidak.
Dari output ini, pengguna dapat melihat alamat IP (IPv4/IPv6), MAC address, serta status setiap interface. Perintah ini biasanya digunakan untuk mengetahui IP address dan memeriksa kondisi jaringan.

### 2. Fungis scutil --dns
![Screenshot Contoh scutil --dns](../Assets/week4/modul4/sc_pj2.avif)
Perintah `scutil --dns` digunakan untuk menampilkan konfigurasi DNS yang sedang digunakan oleh sistem. Output ini menunjukkan server DNS (nameserver) yang dipakai untuk menerjemahkan nama domain menjadi alamat IP.
Pada hasil tersebut, sistem menggunakan DNS `172.20.10.1`, sehingga semua permintaan domain akan diarahkan ke server tersebut. Selain itu, terdapat resolver tambahan untuk domain lokal dan reverse lookup, namun beberapa di antaranya tidak aktif (Not Reachable).
Perintah ini umumnya digunakan untuk mengecek konfigurasi DNS dan membantu troubleshooting jaringan.

### 3. Fungis sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
![Screenshot Contoh sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder](../Assets/week4/modul4/sc_pj3.avif)
Perintah `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` digunakan untuk membersihkan (flush) cache DNS pada sistem macOS.
Perintah ini akan menghapus cache DNS yang tersimpan dan memaksa sistem untuk mengambil ulang data DNS terbaru dari server. Biasanya digunakan untuk mengatasi masalah seperti domain tidak ter-update, error resolusi, atau perubahan DNS yang belum terbaca.

## Menjawab Pertanyaan
### 4.2 Nslookup
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP
server tersebut?
   ![Screenshot Soal 4.2.1](../Assets/week4/modul4/sc_soal_4.2.1.avif)
   Alamat IP server: 104.21.83.80 dan 172.67.217.156
1. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
   ![Screenshot Soal 4.2.2](../Assets/week4/modul4/sc_soal_4.2.2.avif)
   Server DNS otoritatif:
   - use5.akam.net
   - asia1.akam.net
   - use2.akam.net
   - asia2.akam.net
   - ns1-37.akam.net
   - ns1-173.akam.net
   - eur5.akam.net
   - usw2.akam.net
1. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail
      melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?
   ![Screenshot Soal 4.2.3](../Assets/week4/modul4/sc_soal_4.2.3.avif)
   Alamat IP tidak ditampilkan langsung, karena perintah `-type=MX` hanya menampilkan nama mail server (hostname).
   Mail server Yahoo:
   - mta5.am0.yahoodns.net
   - mta6.am0.yahoodns.net
   - mta7.am0.yahoodns.net
   Untuk mendapatkan alamat IP, perlu dilakukan query lanjutan ke masing-masing hostname tersebut.
   ![Screenshot Soal 4.2.3(2)](../Assets/week4/modul4/sc_soal_4.2.3(2).avif)
   Alamat IP server email Yahoo berhasil didapatkan melalui query lanjutan ke hostname mail server.
   Contoh alamat IP:
   - 98.136.96.74
   - 98.136.96.77
   - 67.195.228.111
   - 98.136.96.76
   - 67.195.228.109
   - 98.136.96.75
   - 67.195.204.72
   - 67.195.228.94
   Satu hostname dapat memiliki banyak alamat IP karena menggunakan load balancing.

### 4.4.1 Tracing DNS dengan Wireshark
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP
atau TCP?
1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?
      Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda
      (gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama?
1. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan
   permintaan tersebut mengandung ”jawaban” atau ”answers”?
1. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di
   dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?
1. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP
   pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?
1. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa
   gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin
   mengakses suatu gambar?

### 4.4.2 Tracing DNS dengan Wireshark
1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasan DNS?
2. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut
   merupakan default alamat IP server DNS lokal Anda?
3. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan
   tersebut mengandung ”jawaban” atau ”answers”?
4. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di
   dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?
5. Sertakan hasil tangkapan layar.


### 4.4.2 Tracing DNS dengan Wireshark
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut
   merupakan default alamat IP server DNS lokal Anda?
1. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan
   tersebut mengandung ”jawaban” atau ”answers”?
1. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan?
   Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut?
   JARINGAN KOMPUTER 28
1. Sertakan hasil tangkapan layar.

### 4.4.3 Tracing DNS dengan Wireshark
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut
   merupakan default alamat IP server DNS lokal Anda?
1. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan
   tersebut mengandung ”jawaban” atau ”answers”?
1. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di
   dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?
1. Sertakan hasil tangkapan layar.