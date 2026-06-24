# Tugas Praktikum Week 10 | Modul 10 IP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---


## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol IP menggunakan Wireshark.

---

## Pengantar

Modul IP membahas datagram IPv4, proses traceroute, fragmentasi IP, dan contoh paket IPv6. Traceroute digunakan karena
setiap paket memiliki nilai TTL yang berbeda. Ketika TTL habis di router, router akan mengirim pesan ICMP TTL exceeded
kembali ke host asal.

---

## Langkah Percobaan

### Bagian 1 - IPv4 Dasar

1. Jalankan Wireshark dan mulai capture pada interface aktif.
2. Jalankan perintah berikut di terminal MacOS atau Linux:

```bash
traceroute gaia.cs.umass.edu 56
```

3. Jalankan traceroute kedua dengan ukuran paket lebih besar:

```bash
traceroute gaia.cs.umass.edu 3000
```

4. Hentikan capture Wireshark.
5. Gunakan filter berikut untuk melihat paket UDP dan ICMP:

```text
udp || icmp
```

6. Jika menggunakan Windows, gunakan perintah berikut untuk bagian IPv4 dasar:

```bat
tracert gaia.cs.umass.edu
```

7. Jika capture langsung tidak berhasil, gunakan trace `ip-wireshark-trace1-1.pcapng` dari file berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip
```

### Bagian 2 - Fragmentasi

1. Hapus semua display filter.
2. Urutkan paket berdasarkan kolom Time.
3. Cari datagram dari traceroute ukuran 3000 byte.
4. Amati field `Identification`, `Flags`, `Fragment Offset`, dan `Total Length` pada header IPv4.

### Bagian 3 - IPv6

1. Buka file trace `ip-wireshark-trace2-1.pcapng`.
2. Amati paket DNS AAAA untuk domain `youtube.com`.
3. Perhatikan perbedaan field IPv6 dibanding IPv4, seperti `Traffic Class`, `Flow Label`, `Payload Length`,
   `Next Header`, dan `Hop Limit`.

---

## Output / Hasil Percobaan

### Tampilan paket UDP dan ICMP dari traceroute

![IPv4 traceroute](asset/01-ipv4-traceroute.avif)

### Filter paket UDP dari client ke server

![Filter UDP client server](asset/02-filter-udp-client-server.avif)

### Tampilan trace IPv6

![Trace IPv6](asset/04-trace-ipv6.avif)

---

## Analisis IPv4 Dasar

Sumber data yang dipakai adalah `udp-wireshark-trace.pcap`, terutama paket 7 yang berisi DNS query `www.mit.edu` melalui
UDP. File yang dikirim tidak memuat trace traceroute lengkap, sehingga bagian ICMP TTL exceeded tidak ditemukan.

| No | Komponen                               | Hasil Analisis                          |
|----|----------------------------------------|-----------------------------------------|
| 1  | Alamat IP sumber                       | `192.168.1.101`                         |
| 2  | Alamat IP tujuan                       | `68.87.71.226`                          |
| 3  | Nilai TTL awal yang diamati            | `128`                                   |
| 4  | Protocol pada header IP                | `UDP (17)`                              |
| 5  | Header length IPv4                     | `20 byte`                               |
| 6  | Total length datagram                  | `57 byte`                               |
| 7  | Identification                         | `15612`                                 |
| 8  | Router yang mengirim ICMP TTL exceeded | Tidak ditemukan pada pcap yang dikirim. |

---

## Analisis Fragmentasi

Pada semua file pcap yang dikirim, tidak ditemukan paket IPv4 dengan `Fragment Offset` lebih dari 0 atau flag
`More Fragments`. Artinya, bagian fragmentasi dari modul asli belum dapat diisi dari file yang tersedia.

| Fragmen | Identification | Total Length   | Flags          | Fragment Offset | More Fragments | Keterangan                                     |
|---------|----------------|----------------|----------------|-----------------|----------------|------------------------------------------------|
| 1       | Tidak tersedia | Tidak tersedia | Tidak tersedia | Tidak tersedia  | Tidak tersedia | Tidak ada fragmen IPv4 pada pcap yang dikirim. |
| 2       | Tidak tersedia | Tidak tersedia | Tidak tersedia | Tidak tersedia  | Tidak tersedia | Tidak ada fragmen IPv4 pada pcap yang dikirim. |
| 3       | Tidak tersedia | Tidak tersedia | Tidak tersedia | Tidak tersedia  | Tidak tersedia | Tidak ada fragmen IPv4 pada pcap yang dikirim. |

Fragmentasi terjadi ketika ukuran datagram lebih besar dari MTU jaringan. Namun, trace yang dikirim tidak memuat
traceroute ukuran 3000 byte atau datagram IPv4 yang terfragmentasi.

---

## Analisis IPv6

Sumber data IPv6 yang ditemukan berasal dari `NAT_ISP_side.pcap`, paket 65. Paket tersebut adalah UDP LLMNR ke multicast
IPv6, bukan DNS AAAA untuk `youtube.com`.

| No | Komponen IPv6      | Hasil Analisis                                                                          |
|----|--------------------|-----------------------------------------------------------------------------------------|
| 1  | Alamat IPv6 sumber | `fe80::d04:b072:4f6:f791`                                                               |
| 2  | Alamat IPv6 tujuan | `ff02::1:3`                                                                             |
| 3  | Traffic Class      | `0`                                                                                     |
| 4  | Flow Label         | `0`                                                                                     |
| 5  | Payload Length     | `34 byte`                                                                               |
| 6  | Next Header        | `UDP (17)`                                                                              |
| 7  | Hop Limit          | `1`                                                                                     |
| 8  | Query DNS AAAA     | Tidak ditemukan. Paket IPv6 yang tersedia adalah LLMNR UDP port `5355`, bukan DNS AAAA. |

---

## Kesimpulan

Traceroute memperlihatkan cara kerja TTL pada IP karena setiap router yang menerima paket dengan TTL habis akan
mengembalikan pesan ICMP. Pada ukuran paket besar, IPv4 dapat mengalami fragmentasi. IPv6 memiliki struktur header yang
berbeda dan menggunakan field seperti Flow Label dan Next Header untuk mendukung pemrosesan paket yang lebih sederhana.
