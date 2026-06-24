# Tugas Praktikum Week 13 | Modul 13 Ethernet and ARP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---

## Struktur Folder

1. `asset/` berisi screenshot frame Ethernet, ARP cache, dan paket ARP.
2. `LIST_IMAGE.md` berisi daftar gambar dan instruksi screenshot.

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

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | Destination MAC address | [isi dari Wireshark] |
| 2 | Source MAC address | [isi dari Wireshark] |
| 3 | Type field | [isi dari Wireshark] |
| 4 | Protokol lapisan atas yang dibawa | [isi dari Wireshark] |
| 5 | Panjang frame | [isi dari Wireshark] |
| 6 | Nomor paket HTTP GET | [isi dari Wireshark] |

---

## Analisis ARP Cache

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | Jumlah entri ARP cache sebelum dihapus | [isi dari terminal] |
| 2 | Gateway / router lokal yang muncul di ARP cache | [isi dari terminal] |
| 3 | MAC address gateway | [isi dari terminal] |
| 4 | Kondisi ARP cache setelah dihapus | [isi dari terminal] |

---

## Analisis Paket ARP

| No | Komponen ARP | ARP Request | ARP Reply |
| --- | --- | --- | --- |
| 1 | Opcode | [isi] | [isi] |
| 2 | Sender MAC address | [isi] | [isi] |
| 3 | Sender IP address | [isi] | [isi] |
| 4 | Target MAC address | [isi] | [isi] |
| 5 | Target IP address | [isi] | [isi] |
| 6 | Destination MAC pada Ethernet | [isi] | [isi] |

ARP Request biasanya dikirim secara broadcast karena host belum mengetahui MAC address tujuan. ARP Reply dikirim kembali secara unicast karena penerima sudah mengetahui alamat MAC pengirim request.

---

## Kesimpulan

Ethernet membawa data dalam bentuk frame yang memiliki alamat MAC sumber dan tujuan. ARP membantu host menemukan alamat MAC dari perangkat lain dalam jaringan lokal. Dari capture Wireshark, dapat terlihat bahwa ARP Request menggunakan broadcast, sedangkan ARP Reply menggunakan komunikasi langsung ke host yang meminta.
