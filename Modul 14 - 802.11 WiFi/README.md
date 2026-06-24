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

802.11 adalah standar jaringan nirkabel yang digunakan pada WiFi. Berbeda dengan modul sebelumnya yang banyak
menggunakan Ethernet kabel, modul ini mengamati frame 802.11 seperti Beacon, Data, Association Request, Association
Response, dan Disassociation. Karena tidak semua perangkat mendukung capture frame WiFi mentah, analisis dapat dilakukan
menggunakan file trace yang sudah disediakan.

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

| Waktu        | Aktivitas                                                                       |
|--------------|---------------------------------------------------------------------------------|
| Awal capture | Host sudah terasosiasi dengan AP `30 Munroe St`.                                |
| t = 24.82    | Host membuat request HTTP ke `gaia.cs.umass.edu/wireshark-labs/alice.txt`.      |
| t = 32.82    | Host membuat request HTTP ke `www.cs.umass.edu`.                                |
| t = 49.58    | Host memutus koneksi dari AP `30 Munroe St` dan mencoba ke `linksys_ses_24086`. |
| t = 63.00    | Host kembali berasosiasi dengan AP `30 Munroe St`.                              |

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

Sumber data yang dipakai adalah `Wireshark_802_11.pcap`, paket 1.

| No | Komponen            | Hasil Analisis                                                                                           |
|----|---------------------|----------------------------------------------------------------------------------------------------------|
| 1  | SSID                | `30 Munroe St`                                                                                           |
| 2  | BSSID               | `00:16:b6:f7:1d:51`                                                                                      |
| 3  | Source address      | `00:16:b6:f7:1d:51`                                                                                      |
| 4  | Destination address | `ff:ff:ff:ff:ff:ff`                                                                                      |
| 5  | Beacon interval     | `100 TU`                                                                                                 |
| 6  | Channel             | `6`                                                                                                      |
| 7  | Supported rates     | `1`, `2`, `5.5`, `11` Mbps. Extended supported rates: `6`, `9`, `12`, `18`, `24`, `36`, `48`, `54` Mbps. |

---

## Analisis Data Transfer

Sumber data yang dipakai adalah `Wireshark_802_11.pcap`, paket 480 untuk request ke `gaia.cs.umass.edu` dan paket 1016
untuk request ke `www.cs.umass.edu`.

| No | Komponen    | Request ke `gaia.cs.umass.edu` | Request ke `www.cs.umass.edu` |
|----|-------------|--------------------------------|-------------------------------|
| 1  | Waktu paket | `24,828253 s`, paket 480.      | `32,825992 s`, paket 1016.    |
| 2  | IP tujuan   | `128.119.245.12`               | `128.119.240.19`              |
| 3  | MAC client  | `00:13:02:d1:b6:4f`            | `00:13:02:d1:b6:4f`           |
| 4  | MAC AP      | `00:16:b6:f7:1d:51`            | `00:16:b6:f7:1d:51`           |
| 5  | To DS       | `1`                            | `1`                           |
| 6  | From DS     | `0`                            | `0`                           |

---

## Analisis Association dan Disassociation

Pada trace yang dikirim, frame pemutusan koneksi yang jelas adalah `Deauthentication`, bukan `Disassociation`. Jika
Wireshark tidak menampilkan `wlan.fc.type_subtype == 0x0a`, gunakan `wlan.fc.type_subtype == 0x0c` untuk melihat
deauthentication.

| No | Frame                | Waktu                      | Source              | Destination         | Status / Reason                            |
|----|----------------------|----------------------------|---------------------|---------------------|--------------------------------------------|
| 1  | Deauthentication     | `63,059233 s`, paket 2142. | `00:13:02:d1:b6:4f` | `00:18:39:f5:ba:bb` | Reason code `1`, unspecified reason.       |
| 2  | Association Request  | `63,169910 s`, paket 2162. | `00:13:02:d1:b6:4f` | `00:16:b6:f7:1d:51` | SSID `30 Munroe St`, listen interval `10`. |
| 3  | Association Response | `63,192101 s`, paket 2166. | `00:16:b6:f7:1d:51` | `00:13:02:d1:b6:4f` | Status code `0`, successful.               |

---

## Kesimpulan

Frame 802.11 menunjukkan proses komunikasi pada jaringan WiFi. Beacon frame digunakan access point untuk mengumumkan
keberadaannya. Frame data membawa lalu lintas aplikasi seperti HTTP, sedangkan Association dan Deauthentication
menunjukkan proses perangkat bergabung atau keluar dari access point pada trace yang tersedia.
