# Daftar Gambar dan Instruksi Modul 13 Ethernet and ARP

| File | Isi Screenshot | Instruksi |
| --- | --- | --- |
| `asset/01-http-get-ethernet.avif` | Paket HTTP GET | Cari paket HTTP GET ke `gaia.cs.umass.edu`, lalu screenshot daftar paket. |
| `asset/02-detail-ethernet-ii.avif` | Detail Ethernet II | Pilih paket HTTP GET, buka bagian Ethernet II, screenshot source MAC, destination MAC, dan type. |
| `asset/03-arp-cache.avif` | Output `arp -a` | Jalankan `arp -a` di terminal sebelum menghapus cache, lalu screenshot. |
| `asset/04-arp-request.avif` | Paket ARP Request | Gunakan filter `arp`, pilih ARP Request, lalu screenshot detailnya. |
| `asset/05-arp-reply.avif` | Paket ARP Reply | Pilih ARP Reply yang berpasangan dengan request, lalu screenshot detailnya. |

Catatan: Hati-hati saat menghapus ARP cache karena koneksi dapat terputus sementara. Jika koneksi terganggu, matikan dan nyalakan ulang WiFi.
