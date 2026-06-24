# Tugas Praktikum Week 13 | Modul 13 Ethernet and ARP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---


## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja Ethernet dan ARP menggunakan Wireshark.

---

## Pengantar

Ethernet bekerja pada lapisan data link untuk membawa frame di jaringan lokal. ARP atau Address Resolution Protocol digunakan untuk mencari alamat MAC berdasarkan alamat IP dalam satu jaringan lokal. Pada modul ini, percobaan dilakukan dengan mengakses halaman web, lalu mengamati frame Ethernet dan paket ARP yang muncul di Wireshark.

---

## Langkah Percobaan Ethernet

1. Kosongkan cache browser.
2. Buka Wireshark dan mulai capture pada interface aktif.
3. Akses URL berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html
```

4. Hentikan capture.
5. Cari paket HTTP GET yang dikirim dari komputer ke `gaia.cs.umass.edu`.
6. Untuk fokus ke lapisan Ethernet, buka `Analyze > Enabled Protocols`, lalu hilangkan centang pada IP.
7. Amati bagian Ethernet II pada paket yang memuat HTTP GET.

---

## Langkah Percobaan ARP

1. Lihat isi ARP cache.

MacOS atau Linux:

```bash
arp -a
```

Windows:

```bat
arp -a
```

2. Kosongkan ARP cache.

MacOS:

```bash
sudo arp -d -a
```

Windows:

```bat
arp -d *
```

3. Kosongkan cache browser.
4. Mulai capture Wireshark.
5. Akses URL berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-lab-file3.html
```

6. Hentikan capture.
7. Gunakan filter berikut:

```text
arp
```

---

## Output / Hasil Percobaan

### Paket HTTP GET yang dibawa frame Ethernet

![HTTP GET Ethernet](asset/01-http-get-ethernet.avif)

### Detail frame Ethernet II

![Ethernet II](asset/02-detail-ethernet-ii.avif)

### Isi ARP cache di terminal

![ARP cache](asset/03-arp-cache.avif)

### Paket ARP Request

![ARP request](asset/04-arp-request.avif)

### Paket ARP Reply

![ARP reply](asset/05-arp-reply.avif)

---

## Analisis Frame Ethernet

Sumber data yang dipakai adalah `NAT_home_side.pcap`. Paket HTTP GET yang dianalisis adalah paket 20.

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | Destination MAC address | `00:22:6b:45:1f:1b` |
| 2 | Source MAC address | `00:22:68:0d:ca:8f` |
| 3 | Type field | `0x0800` atau IPv4. |
| 4 | Protokol lapisan atas yang dibawa | HTTP di atas TCP di atas IPv4. |
| 5 | Panjang frame | `767 byte` |
| 6 | Nomor paket HTTP GET | Paket `20`, request `GET /safebrowsing/rd/goog-malware-shavar_s_15361-15365.15361-15365.: HTTP/1.1`. |

---

## Analisis ARP Cache

Data ARP cache terminal tidak dapat diambil dari pcap, sehingga bagian ini tetap perlu diisi dari output terminal perangkat yang digunakan saat praktikum.

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | Jumlah entri ARP cache sebelum dihapus | Tidak tersedia dari pcap. Jalankan `arp -a` di terminal. |
| 2 | Gateway / router lokal yang muncul di ARP cache | Tidak tersedia dari pcap. Pada trace, router lokal yang terlihat adalah `192.168.1.1`. |
| 3 | MAC address gateway | Tidak tersedia dari pcap terminal. Pada paket ARP, MAC router adalah `00:22:6b:45:1f:1b`. |
| 4 | Kondisi ARP cache setelah dihapus | Tidak tersedia dari pcap. Perlu screenshot terminal setelah cache dihapus. |

---

## Analisis Paket ARP

Sumber data yang dipakai adalah `NAT_home_side.pcap`, paket 8 dan 9.

| No | Komponen ARP | ARP Request | ARP Reply |
| --- | --- | --- | --- |
| 1 | Opcode | `1` atau request. | `2` atau reply. |
| 2 | Sender MAC address | `00:22:6b:45:1f:1b` | `00:22:68:0d:ca:8f` |
| 3 | Sender IP address | `192.168.1.1` | `192.168.1.100` |
| 4 | Target MAC address | `00:00:00:00:00:00` | `00:22:6b:45:1f:1b` |
| 5 | Target IP address | `192.168.1.100` | `192.168.1.1` |
| 6 | Destination MAC pada Ethernet | `00:22:68:0d:ca:8f` | `00:22:6b:45:1f:1b` |

Secara umum, ARP Request sering dikirim secara broadcast ketika host belum mengetahui MAC address tujuan. Namun, pada trace ini ARP Request terlihat sebagai unicast ke `00:22:68:0d:ca:8f`, sehingga kemungkinan perangkat pengirim sudah mengetahui MAC tujuan dari cache sebelumnya.

---

## Kesimpulan

Ethernet membawa data dalam bentuk frame yang memiliki alamat MAC sumber dan tujuan. ARP membantu host menemukan alamat MAC dari perangkat lain dalam jaringan lokal. Dari capture Wireshark, dapat terlihat bahwa ARP Request menggunakan broadcast, sedangkan ARP Reply menggunakan komunikasi langsung ke host yang meminta.
