# Tugas Praktikum Week 12 | Modul 12 ICMP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---


## Tujuan Praktikum

1. Mahasiswa dapat menginvestigasi cara kerja protokol ICMP menggunakan Wireshark.
2. Mahasiswa dapat membuat program ICMP Pinger.

Bagian asistensi tugas besar diabaikan sesuai instruksi.

---

## Pengantar

ICMP digunakan untuk mengirim pesan kontrol dan pesan kesalahan pada jaringan IP. Pada modul ini, ICMP diamati melalui
perintah ping dan traceroute. Ping menghasilkan pesan ICMP Echo Request dan Echo Reply, sedangkan traceroute
memanfaatkan pesan ICMP TTL exceeded dari router perantara.

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

![Output traceroute](asset/01-output-ping.avif)

---

## Analisis ICMP Ping

File pcap yang dikirim tidak memuat ICMP Echo Request dan Echo Reply dari percobaan ping. ICMP yang ditemukan adalah
`Destination unreachable, Port unreachable` pada `NAT_home_side.pcap` paket 49 dan `NAT_ISP_side.pcap` paket 53.

| No | Komponen                   | Hasil Analisis                                                        |
|----|----------------------------|-----------------------------------------------------------------------|
| 1  | Jumlah Echo Request        | `0`, tidak ditemukan pada pcap yang dikirim.                          |
| 2  | Jumlah Echo Reply          | `0`, tidak ditemukan pada pcap yang dikirim.                          |
| 3  | Type dan Code Echo Request | Tidak tersedia.                                                       |
| 4  | Type dan Code Echo Reply   | Tidak tersedia.                                                       |
| 5  | Identifier                 | Tidak tersedia.                                                       |
| 6  | Sequence number            | Tidak tersedia.                                                       |
| 7  | Rata-rata RTT              | Tidak tersedia karena tidak ada pasangan Echo Request dan Echo Reply. |

---

## Analisis ICMP Traceroute

Tidak ditemukan pesan ICMP TTL exceeded dari traceroute pada pcap yang dikirim. Tabel berikut mencatat ICMP yang
tersedia sebagai pembanding.

| Hop | IP Router        | ICMP Type       | ICMP Code       | RTT            | Keterangan                                                                      |
|-----|------------------|-----------------|-----------------|----------------|---------------------------------------------------------------------------------|
| 1   | `69.183.241.120` | `3`             | `3`             | Tidak tersedia | `Destination unreachable, Port unreachable` pada `NAT_home_side.pcap` paket 49. |
| 2   | Tidak ditemukan  | Tidak ditemukan | Tidak ditemukan | Tidak tersedia | Tidak ada ICMP TTL exceeded.                                                    |
| 3   | Tidak ditemukan  | Tidak ditemukan | Tidak ditemukan | Tidak tersedia | Tidak ada ICMP TTL exceeded.                                                    |
| 4   | Tidak ditemukan  | Tidak ditemukan | Tidak ditemukan | Tidak tersedia | Tidak ada ICMP TTL exceeded.                                                    |
| 5   | Tidak ditemukan  | Tidak ditemukan | Tidak ditemukan | Tidak tersedia | Tidak ada ICMP TTL exceeded.                                                    |

---

## Kesimpulan

ICMP membantu proses diagnosis jaringan. Ping menggunakan Echo Request dan Echo Reply untuk menguji apakah host tujuan
dapat dijangkau. Traceroute menggunakan perubahan TTL untuk mengetahui router yang dilewati paket menuju tujuan. Program
ICMP Pinger menunjukkan bahwa konsep ping dapat dibuat sendiri dengan raw socket.
