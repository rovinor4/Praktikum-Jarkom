# Tugas Praktikum Week 14 | Modul 14 802.11 WiFi

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---

## Struktur Folder

1. `asset/` berisi screenshot trace 802.11 di Wireshark.
2. `LIST_IMAGE.md` berisi daftar gambar dan instruksi screenshot.

---

## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja WiFi menggunakan Wireshark.

---

## Pengantar

802.11 adalah standar jaringan nirkabel yang digunakan pada WiFi. Berbeda dengan modul sebelumnya yang banyak menggunakan Ethernet kabel, modul ini mengamati frame 802.11 seperti Beacon, Data, Association Request, Association Response, dan Disassociation. Karena tidak semua perangkat mendukung capture frame WiFi mentah, analisis dapat dilakukan menggunakan file trace yang sudah disediakan.

---

## Langkah Percobaan

1. Unduh file trace berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip
```

2. Ekstrak file berikut:

```text
Wireshark_802_11.pcap
```

3. Buka file tersebut di Wireshark.
4. Gunakan filter berikut untuk melihat Beacon frame:

```text
wlan.fc.type_subtype == 0x08
```

5. Untuk melihat Association Request:

```text
wlan.fc.type_subtype == 0x00
```

6. Untuk melihat Association Response:

```text
wlan.fc.type_subtype == 0x01
```

7. Untuk melihat Disassociation:

```text
wlan.fc.type_subtype == 0x0a
```

8. Untuk melihat transfer HTTP, gunakan filter:

```text
http
```

---

## Skenario Trace

| Waktu | Aktivitas |
| --- | --- |
| Awal capture | Host sudah terasosiasi dengan AP `30 Munroe St`. |
| t = 24.82 | Host membuat request HTTP ke `gaia.cs.umass.edu/wireshark-labs/alice.txt`. |
| t = 32.82 | Host membuat request HTTP ke `www.cs.umass.edu`. |
| t = 49.58 | Host memutus koneksi dari AP `30 Munroe St` dan mencoba ke `linksys_ses_24086`. |
| t = 63.00 | Host kembali berasosiasi dengan AP `30 Munroe St`. |

---

## Output / Hasil Percobaan

### Tampilan awal trace 802.11

![Trace 802.11](asset/01-trace-80211.avif)

### Beacon frame

![Beacon frame](asset/02-beacon-frame.avif)

### Data transfer HTTP

![Data transfer HTTP](asset/03-data-transfer-http.avif)

### Association Request

![Association Request](asset/04-association-request.avif)

### Association Response

![Association Response](asset/05-association-response.avif)

### Disassociation

![Disassociation](asset/06-disassociation.avif)

---

## Analisis Beacon Frame

| No | Komponen | Hasil Analisis |
| --- | --- | --- |
| 1 | SSID | [isi dari Wireshark] |
| 2 | BSSID | [isi dari Wireshark] |
| 3 | Source address | [isi dari Wireshark] |
| 4 | Destination address | [isi dari Wireshark] |
| 5 | Beacon interval | [isi dari Wireshark] |
| 6 | Channel | [isi dari Wireshark] |
| 7 | Supported rates | [isi dari Wireshark] |

---

## Analisis Data Transfer

| No | Komponen | Request ke `gaia.cs.umass.edu` | Request ke `www.cs.umass.edu` |
| --- | --- | --- | --- |
| 1 | Waktu paket | [isi] | [isi] |
| 2 | IP tujuan | [isi] | [isi] |
| 3 | MAC client | [isi] | [isi] |
| 4 | MAC AP | [isi] | [isi] |
| 5 | To DS | [isi] | [isi] |
| 6 | From DS | [isi] | [isi] |

---

## Analisis Association dan Disassociation

| No | Frame | Waktu | Source | Destination | Status / Reason |
| --- | --- | --- | --- | --- | --- |
| 1 | Disassociation | [isi] | [isi] | [isi] | [isi] |
| 2 | Association Request | [isi] | [isi] | [isi] | [isi] |
| 3 | Association Response | [isi] | [isi] | [isi] | [isi] |

---

## Kesimpulan

Frame 802.11 menunjukkan proses komunikasi pada jaringan WiFi. Beacon frame digunakan access point untuk mengumumkan keberadaannya. Frame data membawa lalu lintas aplikasi seperti HTTP, sedangkan Association dan Disassociation menunjukkan proses perangkat bergabung atau keluar dari access point.
