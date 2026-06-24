# Daftar Gambar dan Instruksi Modul 13 Ethernet and ARP

| File | Isi Screenshot | File Pcap / Sumber | Instruksi |
| --- | --- | --- | --- |
| `asset/01-http-get-ethernet.avif` | Paket HTTP GET | `NAT_home_side.pcap` | Gunakan filter `http.request.method == GET` atau `tcp contains "GET"`. Paket utama: nomor 20. |
| `asset/02-detail-ethernet-ii.avif` | Detail Ethernet II | `NAT_home_side.pcap` | Pilih paket 20, buka bagian Ethernet II, lalu tampilkan source MAC, destination MAC, dan type `IPv4`. |
| `asset/03-arp-cache.avif` | Output `arp -a` | Tidak tersedia di pcap | Jalankan `arp -a` di terminal perangkat praktikum. |
| `asset/04-arp-request.avif` | Paket ARP Request | `NAT_home_side.pcap` | Gunakan filter `arp`, pilih paket 8. |
| `asset/05-arp-reply.avif` | Paket ARP Reply | `NAT_home_side.pcap` | Gunakan filter `arp`, pilih paket 9. |

Catatan: pada trace ini ARP Request terlihat unicast, bukan broadcast.
