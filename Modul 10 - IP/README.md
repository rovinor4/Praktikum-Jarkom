# Tugas Praktikum Week 10 | Modul 10 IP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---

## Struktur Folder

1. `asset/` berisi screenshot Wireshark untuk IPv4, fragmentasi, dan IPv6.
2. `LIST_IMAGE.md` berisi daftar gambar dan instruksi screenshot.

---

## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol IP menggunakan Wireshark.

---

## Pengantar

Modul IP membahas datagram IPv4, proses traceroute, fragmentasi IP, dan contoh paket IPv6. Traceroute digunakan karena setiap paket memiliki nilai TTL yang berbeda. Ketika TTL habis di router, router akan mengirim pesan ICMP TTL exceeded kembali ke host asal.

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
3. Perhatikan perbedaan field IPv6 dibanding IPv4, seperti `Traffic Class`, `Flow Label`, `Payload Length`, `Next Header`, dan `Hop Limit`.

---

## Output / Hasil Percobaan

### Tampilan paket UDP dan ICMP dari traceroute

![IPv4 traceroute](asset/01-ipv4-traceroute.avif)

### Filter paket UDP dari client ke server

![Filter UDP client server](asset/02-filter-udp-client-server.avif)

### Analisis fragmentasi IPv4

![Fragmentasi IPv4](asset/03-fragmentasi-ipv4.avif)

### Tampilan trace IPv6

![Trace IPv6](asset/04-trace-ipv6.avif)

### Paket DNS AAAA dalam IPv6

![DNS AAAA IPv6](asset/05-dns-aaaa-ipv6.avif)

---

## Analisis IPv4 Dasar

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | Alamat IP sumber | [isi dari Wireshark] |
| 2 | Alamat IP tujuan | [isi dari Wireshark] |
| 3 | Nilai TTL awal yang diamati | [isi dari Wireshark] |
| 4 | Protocol pada header IP | [isi dari Wireshark] |
| 5 | Header length IPv4 | [isi dari Wireshark] |
| 6 | Total length datagram | [isi dari Wireshark] |
| 7 | Identification | [isi dari Wireshark] |
| 8 | Router yang mengirim ICMP TTL exceeded | [isi dari Wireshark] |

---

## Analisis Fragmentasi

| Fragmen | Identification | Total Length | Flags | Fragment Offset | More Fragments | Keterangan |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 2 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |
| 3 | [isi] | [isi] | [isi] | [isi] | [isi] | [isi] |

Fragmentasi terjadi ketika ukuran datagram lebih besar dari MTU jaringan. Datagram akan dibagi menjadi beberapa fragmen dengan nilai `Identification` yang sama, sedangkan `Fragment Offset` menunjukkan posisi fragmen dalam datagram asli.

---

## Analisis IPv6

| No | Komponen IPv6 | Hasil Analisis |
| --- | --- | --- |
| 1 | Alamat IPv6 sumber | [isi dari Wireshark] |
| 2 | Alamat IPv6 tujuan | [isi dari Wireshark] |
| 3 | Traffic Class | [isi dari Wireshark] |
| 4 | Flow Label | [isi dari Wireshark] |
| 5 | Payload Length | [isi dari Wireshark] |
| 6 | Next Header | [isi dari Wireshark] |
| 7 | Hop Limit | [isi dari Wireshark] |
| 8 | Query DNS AAAA | [isi dari Wireshark] |

---

## Kesimpulan

Traceroute memperlihatkan cara kerja TTL pada IP karena setiap router yang menerima paket dengan TTL habis akan mengembalikan pesan ICMP. Pada ukuran paket besar, IPv4 dapat mengalami fragmentasi. IPv6 memiliki struktur header yang berbeda dan menggunakan field seperti Flow Label dan Next Header untuk mendukung pemrosesan paket yang lebih sederhana.
