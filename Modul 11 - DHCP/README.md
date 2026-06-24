# Tugas Praktikum Week 11 | Modul 11 DHCP

Nama : Rovino Ramadhani
NIM : 103072400031
Kelas : IF-04-01

---


## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol DHCP menggunakan Wireshark.

---

## Pengantar

DHCP atau Dynamic Host Configuration Protocol digunakan untuk memberikan konfigurasi jaringan secara otomatis kepada
host. Konfigurasi tersebut meliputi alamat IP, subnet mask, default gateway, DNS server, dan masa sewa alamat IP. Alur
umum DHCP dikenal sebagai DORA, yaitu Discover, Offer, Request, dan Acknowledgement.

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

### Detail DHCP ACK

![DHCP ACK](asset/05-dhcp-ack.avif)

---

## Analisis Proses DHCP

Sumber data yang ditemukan adalah `NAT_ISP_side.pcap`, paket 170. File tersebut hanya memuat DHCP ACK, bukan rangkaian
DORA lengkap.

| Tahap    | Arah Paket         | Source IP       | Destination IP    | Source MAC          | Destination MAC     | Keterangan                                            |
|----------|--------------------|-----------------|-------------------|---------------------|---------------------|-------------------------------------------------------|
| Discover | Client ke jaringan | Tidak ditemukan | Tidak ditemukan   | Tidak ditemukan     | Tidak ditemukan     | Tidak ada paket DHCP Discover pada pcap yang dikirim. |
| Offer    | Server ke client   | Tidak ditemukan | Tidak ditemukan   | Tidak ditemukan     | Tidak ditemukan     | Tidak ada paket DHCP Offer pada pcap yang dikirim.    |
| Request  | Client ke server   | Tidak ditemukan | Tidak ditemukan   | Tidak ditemukan     | Tidak ditemukan     | Tidak ada paket DHCP Request pada pcap yang dikirim.  |
| ACK      | Server ke client   | `73.160.28.1`   | `255.255.255.255` | `00:0e:d6:bf:6c:01` | `ff:ff:ff:ff:ff:ff` | Server mengirim DHCP ACK.                             |

---

## Detail Konfigurasi yang Diberikan DHCP

| Komponen                 | Hasil Analisis                                                                                    |
|--------------------------|---------------------------------------------------------------------------------------------------|
| Alamat IP yang diberikan | `0.0.0.0` pada field `yiaddr`; trace ini tidak menampilkan pemberian alamat client secara normal. |
| Subnet mask              | `255.255.248.0`                                                                                   |
| Default gateway / router | `71.192.32.1`                                                                                     |
| DNS server               | Tidak ditemukan pada opsi DHCP ACK yang tersedia.                                                 |
| Lease time               | Tidak ditemukan pada opsi DHCP ACK yang tersedia.                                                 |
| DHCP server identifier   | `68.87.71.11`                                                                                     |
| Transaction ID           | `0x897ac1ec`                                                                                      |

---

## Kesimpulan

DHCP memungkinkan komputer memperoleh konfigurasi jaringan secara otomatis tanpa pengaturan manual. Dari hasil capture,
proses DORA memperlihatkan komunikasi antara client dan DHCP server mulai dari pencarian server hingga pemberian alamat
IP dan konfigurasi jaringan.
