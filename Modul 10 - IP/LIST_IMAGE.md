# Daftar Gambar dan Instruksi Modul 10 IP

| File | Isi Screenshot | Instruksi |
| --- | --- | --- |
| `asset/01-ipv4-traceroute.avif` | Paket UDP dan ICMP hasil traceroute | Gunakan filter `udp || icmp`, lalu screenshot daftar paket. |
| `asset/02-filter-udp-client-server.avif` | Paket UDP dari client ke `gaia.cs.umass.edu` | Gunakan filter `ip.src == [IP_CLIENT] && ip.dst == 128.119.245.12 && udp && !icmp`. |
| `asset/03-fragmentasi-ipv4.avif` | Field fragmentasi IPv4 | Cari paket besar dari traceroute 3000 byte, buka bagian Internet Protocol Version 4. |
| `asset/04-trace-ipv6.avif` | Tampilan awal trace IPv6 | Buka `ip-wireshark-trace2-1.pcapng`, lalu screenshot daftar paket. |
| `asset/05-dns-aaaa-ipv6.avif` | DNS AAAA di atas IPv6 | Pilih paket DNS AAAA untuk `youtube.com`, buka detail IPv6 dan DNS. |

Catatan: Ganti `[IP_CLIENT]` dengan alamat IP komputer yang muncul di trace.
