# Tugas Praktikum Week 6 | Modul 6 TCP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---


## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol TCP menggunakan Wireshark.

---

## Pengantar

TCP adalah protokol transport yang menyediakan komunikasi andal antara client dan server. Pada modul ini, percobaan dilakukan dengan mengunggah file `alice.txt` ke server `gaia.cs.umass.edu`, lalu menganalisis segmen TCP yang terbentuk. Analisis utama mencakup proses pembukaan koneksi, nomor urut, acknowledgement, retransmission, throughput, dan grafik congestion control.

---

## Langkah Percobaan

1. Buka URL berikut di browser untuk mengunduh file `alice.txt`:

```text
http://gaia.cs.umass.edu/wireshark-labs/alice.txt
```

2. Buka halaman upload berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html
```

3. Pilih file `alice.txt`, tetapi jangan langsung menekan tombol upload.
4. Buka Wireshark dan mulai capture pada interface jaringan yang sedang dipakai.
5. Kembali ke browser, tekan tombol upload, lalu tunggu sampai proses selesai.
6. Hentikan capture di Wireshark.
7. Gunakan display filter berikut:

```text
tcp
```

8. Untuk melihat TCP tanpa interpretasi HTTP, buka menu `Analyze > Enabled Protocols`, lalu hilangkan centang pada HTTP.
9. Jika capture langsung tidak berhasil, gunakan trace dari file berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip
```

File yang dipakai: `tcp-ethereal-trace-1`.

---

## Output / Hasil Percobaan

### Halaman upload file `alice.txt`

![Halaman upload TCP](asset/01-halaman-upload-tcp.avif)

### Upload berhasil

![Upload berhasil](asset/02-upload-berhasil.avif)

### Tampilan Wireshark dengan filter TCP

![Filter TCP](asset/03-filter-tcp.avif)

### Tampilan Wireshark setelah HTTP dinonaktifkan

![HTTP disabled](asset/04-http-disabled.avif)

### Grafik Time-Sequence Graph Stevens

![TCP graph](asset/05-time-sequence-graph.avif)

---

## Analisis Awal Trace TCP

Catatan: file yang tersedia tidak berisi trace upload `alice.txt` ke `gaia.cs.umass.edu`. Oleh karena itu, analisis di bawah memakai aliran HTTP POST yang ditemukan pada `NAT_home_side.pcap`, yaitu paket 4 sampai 14. Server pada trace ini adalah `74.125.91.113`, bukan `gaia.cs.umass.edu`.

| No | Pertanyaan | Hasil Analisis |
| --- | --- | --- |
| 1 | Alamat IP client yang digunakan untuk transfer file | `192.168.1.100` |
| 2 | Port TCP client | `4330` |
| 3 | Alamat IP `gaia.cs.umass.edu` | Tidak ditemukan pada pcap yang dikirim. Server HTTP yang dianalisis adalah `74.125.91.113`. |
| 4 | Port TCP server | `80` |
| 5 | Nomor paket yang memuat HTTP POST | Paket `7` pada `NAT_home_side.pcap`. |

---

## Analisis Dasar TCP

| No | Komponen yang Dianalisis | Hasil Analisis |
| --- | --- | --- |
| 1 | Sequence number segmen SYN | `952809727`, paket 4. |
| 2 | Flag yang menandai segmen SYN | `SYN`. |
| 3 | Sequence number segmen SYN-ACK | `2709749795`, paket 5. |
| 4 | Acknowledgement number pada SYN-ACK | `952809728`. |
| 5 | Sequence number segmen yang berisi HTTP POST | `952809728`, paket 7. |
| 6 | Panjang enam segmen TCP pertama | `0`, `0`, `0`, `981`, `6`, dan `799` byte payload untuk paket 4, 5, 6, 7, 10, dan 11. |
| 7 | Minimum receive window / buffer penerima | `121` byte pada paket server ke client dalam flow yang sama. |
| 8 | Ada atau tidaknya retransmission | Ada indikasi retransmission pada response `HTTP/1.1 200 OK`, karena paket 13 mengulang sequence number `2709749796` yang sudah muncul pada paket 11. |
| 9 | Throughput koneksi TCP | Sekitar `4,6 KB/s` jika dihitung dari payload unik `1.786` byte selama sekitar `0,388` detik. Nilai ini tidak mewakili upload besar karena trace bukan file `alice.txt`. |

---

## Tabel Enam Segmen TCP Pertama

| Segmen | Sequence Number | Waktu Kirim | Waktu ACK Diterima | RTT | Estimated RTT | Panjang Segmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `952809727` | `1,140302 s` | `1,207818 s` | `0,067516 s` | `0,067516 s` | `0 byte` |
| 2 | `2709749795` | `1,207818 s` | `1,207873 s` | `0,000055 s` | `0,059333 s` | `0 byte` |
| 3 | `952809728` | `1,207873 s` | Tidak tersedia | Tidak tersedia | Tidak tersedia | `0 byte` |
| 4 | `952809728` | `1,208040 s` | `1,269675 s` | `0,061635 s` | `0,059621 s` | `981 byte` |
| 5 | `2709749796` | `1,269675 s` | Tidak tersedia | Tidak tersedia | Tidak tersedia | `6 byte` |
| 6 | `2709749796` | `1,274062 s` | `1,474508 s` | `0,200446 s` | `0,077224 s` | `799 byte` |

---

## Analisis Congestion Control

Time-Sequence Graph Stevens digunakan untuk melihat perubahan sequence number terhadap waktu. Pada file `NAT_home_side.pcap`, aliran yang dianalisis hanya berisi HTTP POST kecil dan response HTTP, bukan transfer file besar. Karena itu, grafik congestion control tidak cukup kuat untuk menyimpulkan fase `slow start` dan `congestion avoidance`.

| Komponen | Hasil Analisis |
| --- | --- |
| Awal slow start | Tidak dianalisis dari file yang tersedia. |
| Akhir slow start | Tidak dianalisis dari file yang tersedia. |
| Awal congestion avoidance | Tidak dianalisis dari file yang tersedia. |
| Perbedaan grafik aktual dengan teori | File yang tersedia tidak memuat transfer TCP besar seperti modul asli, sehingga grafik tidak sebanding dengan teori congestion control pada upload file. |

---

## Kesimpulan

Berdasarkan hasil capture yang tersedia, protokol TCP membangun koneksi dengan proses handshake, mengirim data menggunakan sequence number, dan memastikan data diterima melalui acknowledgement. Namun, file pcap yang dianalisis bukan trace upload besar ke `gaia.cs.umass.edu`, sehingga bagian congestion control perlu divalidasi lagi menggunakan trace TCP resmi atau capture upload ulang.
