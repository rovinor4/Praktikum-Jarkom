# Daftar Gambar dan Instruksi Modul 12 ICMP

| File | Isi Screenshot | Instruksi |
| --- | --- | --- |
| `asset/01-output-ping.avif` | Output ping di terminal | Jalankan `ping -c 10 www.ust.hk`, lalu screenshot hasilnya. |
| `asset/02-icmp-ping-wireshark.avif` | Daftar paket ICMP ping | Gunakan filter `icmp`, lalu screenshot daftar Echo Request dan Echo Reply. |
| `asset/03-icmp-echo-request.avif` | Detail Echo Request | Pilih paket Echo Request, buka bagian Internet Control Message Protocol. |
| `asset/04-output-traceroute.avif` | Output traceroute | Jalankan `traceroute www.inria.fr`, lalu screenshot hasilnya. |
| `asset/05-icmp-ttl-exceeded.avif` | Detail ICMP TTL exceeded | Pilih paket ICMP dari router, buka detail Type dan Code. |
| `asset/06-python-icmp-pinger.avif` | Output program Python | Jalankan `sudo python3 code/icmp_pinger.py google.com`, lalu screenshot output. |

Catatan: Jika `www.ust.hk` atau `www.inria.fr` tidak merespons, gunakan host lain yang stabil, misalnya `google.com` atau `cloudflare.com`, lalu tulis alasan penggantian host.
