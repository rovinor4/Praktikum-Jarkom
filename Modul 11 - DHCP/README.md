# Tugas Praktikum Week 11 | Modul 11 DHCP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---

## Struktur Folder

1. `asset/` berisi screenshot proses DHCP di Wireshark.
2. `LIST_IMAGE.md` berisi daftar gambar yang perlu diganti dengan screenshot asli.

---

## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol DHCP menggunakan Wireshark.

---

## Pengantar

DHCP atau Dynamic Host Configuration Protocol digunakan untuk memberikan konfigurasi jaringan secara otomatis kepada host. Konfigurasi tersebut meliputi alamat IP, subnet mask, default gateway, DNS server, dan masa sewa alamat IP. Alur umum DHCP dikenal sebagai DORA, yaitu Discover, Offer, Request, dan Acknowledgement.

---

## Langkah Percobaan

### MacOS

1. Cek nama interface aktif di Wireshark melalui `Capture > Options`.
2. Jika interface adalah `en0`, jalankan perintah berikut di terminal:

```bash
sudo ipconfig set en0 none
```

3. Mulai capture Wireshark pada interface tersebut.
4. Jalankan perintah berikut:

```bash
sudo ipconfig set en0 dhcp
```

5. Tunggu beberapa detik, lalu hentikan capture.
6. Gunakan filter berikut:

```text
dhcp
```

Jika filter `dhcp` tidak menampilkan paket, gunakan:

```text
bootp
```

### Linux

```bash
sudo ip addr flush en0
sudo dhclient -r
sudo dhclient en0
```

### Windows

```bat
ipconfig /release
ipconfig /renew
```

Jika capture langsung tidak berhasil, gunakan trace `dhcp-wireshark-trace1-1.pcapng` dari file berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip
```

---

## Output / Hasil Percobaan

### Capture DHCP Discover, Offer, Request, dan ACK

![DHCP DORA](asset/01-dhcp-dora.avif)

### Detail DHCP Discover

![DHCP Discover](asset/02-dhcp-discover.avif)

### Detail DHCP Offer

![DHCP Offer](asset/03-dhcp-offer.avif)

### Detail DHCP Request

![DHCP Request](asset/04-dhcp-request.avif)

### Detail DHCP ACK

![DHCP ACK](asset/05-dhcp-ack.avif)

---

## Analisis Proses DHCP

| Tahap | Arah Paket | Source IP | Destination IP | Source MAC | Destination MAC | Keterangan |
| --- | --- | --- | --- | --- | --- | --- |
| Discover | Client ke jaringan | [isi] | [isi] | [isi] | [isi] | Client mencari DHCP server. |
| Offer | Server ke client | [isi] | [isi] | [isi] | [isi] | Server menawarkan alamat IP. |
| Request | Client ke server | [isi] | [isi] | [isi] | [isi] | Client meminta alamat IP yang ditawarkan. |
| ACK | Server ke client | [isi] | [isi] | [isi] | [isi] | Server menyetujui konfigurasi. |

---

## Detail Konfigurasi yang Diberikan DHCP

| Komponen | Hasil Analisis |
| --- | --- |
| Alamat IP yang diberikan | [isi dari Wireshark] |
| Subnet mask | [isi dari Wireshark] |
| Default gateway / router | [isi dari Wireshark] |
| DNS server | [isi dari Wireshark] |
| Lease time | [isi dari Wireshark] |
| DHCP server identifier | [isi dari Wireshark] |
| Transaction ID | [isi dari Wireshark] |

---

## Kesimpulan

DHCP memungkinkan komputer memperoleh konfigurasi jaringan secara otomatis tanpa pengaturan manual. Dari hasil capture, proses DORA memperlihatkan komunikasi antara client dan DHCP server mulai dari pencarian server hingga pemberian alamat IP dan konfigurasi jaringan.
