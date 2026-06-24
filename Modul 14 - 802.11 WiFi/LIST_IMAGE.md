# Daftar Gambar dan Instruksi Modul 14 802.11 WiFi

| File | Isi Screenshot | Instruksi |
| --- | --- | --- |
| `asset/01-trace-80211.avif` | Tampilan awal file `Wireshark_802_11.pcap` | Buka trace di Wireshark, lalu screenshot daftar paket awal. |
| `asset/02-beacon-frame.avif` | Beacon frame | Gunakan filter `wlan.fc.type_subtype == 0x08`, pilih satu beacon, buka detail IEEE 802.11. |
| `asset/03-data-transfer-http.avif` | HTTP data transfer | Gunakan filter `http`, cari request pada waktu sekitar 24.82 atau 32.82. |
| `asset/04-association-request.avif` | Association Request | Gunakan filter `wlan.fc.type_subtype == 0x00`, lalu screenshot detailnya. |
| `asset/05-association-response.avif` | Association Response | Gunakan filter `wlan.fc.type_subtype == 0x01`, lalu screenshot detailnya. |
| `asset/06-disassociation.avif` | Disassociation | Gunakan filter `wlan.fc.type_subtype == 0x0a`, lalu screenshot alasan disassociation. |

Catatan: Jika Wireshark tidak menampilkan protokol 802.11 saat capture langsung, gunakan trace bawaan karena tidak semua driver WiFi mendukung monitor mode.
