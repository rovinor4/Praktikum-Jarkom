# Tugas Praktikum Week 12 | Modul 12 ICMP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---

## Struktur Folder

1. `asset/` berisi screenshot ping, traceroute, dan detail paket ICMP.
2. `code/icmp_pinger.py` berisi program ICMP Pinger sederhana.
3. `LIST_IMAGE.md` berisi daftar gambar yang perlu diganti dengan screenshot asli.

---

## Tujuan Praktikum

1. Mahasiswa dapat menginvestigasi cara kerja protokol ICMP menggunakan Wireshark.
2. Mahasiswa dapat membuat program ICMP Pinger.

Bagian asistensi tugas besar diabaikan sesuai instruksi.

---

## Pengantar

ICMP digunakan untuk mengirim pesan kontrol dan pesan kesalahan pada jaringan IP. Pada modul ini, ICMP diamati melalui perintah ping dan traceroute. Ping menghasilkan pesan ICMP Echo Request dan Echo Reply, sedangkan traceroute memanfaatkan pesan ICMP TTL exceeded dari router perantara.

---

## Langkah Percobaan Ping

1. Buka Wireshark dan mulai capture pada interface aktif.
2. Jalankan perintah ping. Pada MacOS atau Linux:

```bash
ping -c 10 www.ust.hk
```

Pada Windows:

```bat
ping -n 10 www.ust.hk
```

3. Hentikan capture setelah ping selesai.
4. Gunakan filter berikut:

```text
icmp
```

---

## Langkah Percobaan Traceroute

Pada MacOS atau Linux:

```bash
traceroute www.inria.fr
```

Pada Windows:

```bat
tracert www.inria.fr
```

Setelah selesai, hentikan capture dan gunakan filter:

```text
icmp
```

---

## Program ICMP Pinger

File program tersedia pada:

```text
code/icmp_pinger.py
```

Cara menjalankan di MacOS atau Linux:

```bash
sudo python3 code/icmp_pinger.py google.com
```

Program ini membutuhkan hak akses administrator karena raw socket ICMP biasanya tidak boleh dibuat oleh user biasa.

---

## Penjelasan Program `icmp_pinger.py`

1. Program menerima hostname dari argument terminal.
2. Hostname diubah menjadi alamat IP dengan `socket.gethostbyname()`.
3. Program membuat raw socket dengan protokol ICMP.
4. Program membentuk paket Echo Request berisi header ICMP dan payload waktu pengiriman.
5. Program mengirim paket ke host tujuan.
6. Program menunggu Echo Reply sampai batas timeout.
7. Jika balasan diterima, program menghitung RTT berdasarkan selisih waktu kirim dan waktu terima.

---

## Output / Hasil Percobaan

### Output ping di terminal

![Output ping](asset/01-output-ping.avif)

### Paket ICMP hasil ping di Wireshark

![ICMP ping Wireshark](asset/02-icmp-ping-wireshark.avif)

### Detail ICMP Echo Request

![ICMP Echo Request](asset/03-icmp-echo-request.avif)

### Output traceroute di terminal

![Output traceroute](asset/04-output-traceroute.avif)

### Detail ICMP TTL exceeded

![ICMP TTL exceeded](asset/05-icmp-ttl-exceeded.avif)

### Output program ICMP Pinger Python

![Python ICMP Pinger](asset/06-python-icmp-pinger.avif)

---

## Analisis ICMP Ping

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | Jumlah Echo Request | [isi dari Wireshark] |
| 2 | Jumlah Echo Reply | [isi dari Wireshark] |
| 3 | Type dan Code Echo Request | [isi dari Wireshark] |
| 4 | Type dan Code Echo Reply | [isi dari Wireshark] |
| 5 | Identifier | [isi dari Wireshark] |
| 6 | Sequence number | [isi dari Wireshark] |
| 7 | Rata-rata RTT | [isi dari terminal / Wireshark] |

---

## Analisis ICMP Traceroute

| Hop | IP Router | ICMP Type | ICMP Code | RTT | Keterangan |
| --- | --- | --- | --- | --- | --- |
| 1 | [isi] | [isi] | [isi] | [isi] | [isi] |
| 2 | [isi] | [isi] | [isi] | [isi] | [isi] |
| 3 | [isi] | [isi] | [isi] | [isi] | [isi] |
| 4 | [isi] | [isi] | [isi] | [isi] | [isi] |
| 5 | [isi] | [isi] | [isi] | [isi] | [isi] |

---

## Kesimpulan

ICMP membantu proses diagnosis jaringan. Ping menggunakan Echo Request dan Echo Reply untuk menguji apakah host tujuan dapat dijangkau. Traceroute menggunakan perubahan TTL untuk mengetahui router yang dilewati paket menuju tujuan. Program ICMP Pinger menunjukkan bahwa konsep ping dapat dibuat sendiri dengan raw socket.
