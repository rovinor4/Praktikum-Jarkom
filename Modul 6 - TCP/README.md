# Tugas Praktikum Week 6 | Modul 6 TCP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---

## Struktur Folder

1. `asset/` berisi gambar hasil screenshot Wireshark, browser, dan grafik TCP.
2. `LIST_IMAGE.md` berisi daftar gambar yang perlu diganti dengan screenshot asli.

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

| No | Pertanyaan | Hasil Analisis |
| --- | --- | --- |
| 1 | Alamat IP client yang digunakan untuk transfer file | [isi dari Wireshark] |
| 2 | Port TCP client | [isi dari Wireshark] |
| 3 | Alamat IP `gaia.cs.umass.edu` | [isi dari Wireshark] |
| 4 | Port TCP server | [isi dari Wireshark] |
| 5 | Nomor paket yang memuat HTTP POST | [isi dari Wireshark] |

---

## Analisis Dasar TCP

| No | Komponen yang Dianalisis | Hasil Analisis |
| --- | --- | --- |
| 1 | Sequence number segmen SYN | [isi dari Wireshark] |
| 2 | Flag yang menandai segmen SYN | [isi dari Wireshark] |
| 3 | Sequence number segmen SYN-ACK | [isi dari Wireshark] |
| 4 | Acknowledgement number pada SYN-ACK | [isi dari Wireshark] |
| 5 | Sequence number segmen yang berisi HTTP POST | [isi dari Wireshark] |
| 6 | Panjang enam segmen TCP pertama | [isi dari Wireshark] |
| 7 | Minimum receive window / buffer penerima | [isi dari Wireshark] |
| 8 | Ada atau tidaknya retransmission | [isi dari Wireshark] |
| 9 | Throughput koneksi TCP | [isi dari Wireshark] |

---

## Tabel Enam Segmen TCP Pertama

| Segmen | Sequence Number | Waktu Kirim | Waktu ACK Diterima | RTT | Estimated RTT | Panjang Segmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 2 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 3 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 4 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 5 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 6 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |

---

## Analisis Congestion Control

Time-Sequence Graph Stevens digunakan untuk melihat perubahan sequence number terhadap waktu. Jika titik-titik awal meningkat secara cepat, bagian tersebut dapat mengindikasikan fase slow start. Setelah kenaikan menjadi lebih stabil, koneksi biasanya mulai masuk ke congestion avoidance.

| Komponen | Hasil Analisis |
| --- | --- |
| Awal slow start | [isi berdasarkan grafik] |
| Akhir slow start | [isi berdasarkan grafik] |
| Awal congestion avoidance | [isi berdasarkan grafik] |
| Perbedaan grafik aktual dengan teori | [isi berdasarkan pengamatan] |

---

## Kesimpulan

Berdasarkan hasil capture, protokol TCP membangun koneksi dengan proses handshake, mengirim data menggunakan sequence number, dan memastikan data diterima melalui acknowledgement. Grafik TCP dapat digunakan untuk melihat pola pengiriman data dan memperkirakan perilaku congestion control selama proses upload file berlangsung.
