import argparse
import os
import select
import socket
import struct
import sys
import time


def checksum(data):
    if len(data) % 2:
        data += b'\x00'
    total = 0
    for i in range(0, len(data), 2):
        total += (data[i] << 8) + data[i + 1]
    total = (total >> 16) + (total & 0xffff)
    total += total >> 16
    return (~total) & 0xffff


def create_packet(identifier, sequence):
    payload = struct.pack('!d', time.time()) + b'RovinoICMP' * 4
    header = struct.pack('!BBHHH', 8, 0, 0, identifier, sequence)
    packet_checksum = checksum(header + payload)
    header = struct.pack('!BBHHH', 8, 0, packet_checksum, identifier, sequence)
    return header + payload


def ping_once(sock, host, identifier, sequence, timeout):
    packet = create_packet(identifier, sequence)
    sent_at = time.time()
    sock.sendto(packet, (host, 1))
    ready = select.select([sock], [], [], timeout)
    if not ready[0]:
        return None
    data, addr = sock.recvfrom(1024)
    received_at = time.time()
    ip_header_length = (data[0] & 0x0f) * 4
    icmp_header = data[ip_header_length:ip_header_length + 8]
    icmp_type, code, _, packet_id, packet_sequence = struct.unpack('!BBHHH', icmp_header)
    if icmp_type == 0 and code == 0 and packet_id == identifier and packet_sequence == sequence:
        return addr[0], (received_at - sent_at) * 1000
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    parser.add_argument('-c', '--count', type=int, default=4)
    parser.add_argument('-t', '--timeout', type=float, default=2.0)
    args = parser.parse_args()

    try:
        destination = socket.gethostbyname(args.host)
    except socket.gaierror:
        print('Host tidak ditemukan')
        return 1

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        print('Raw socket membutuhkan akses administrator. Jalankan dengan sudo atau mode administrator.')
        return 1

    identifier = os.getpid() & 0xffff
    print(f'PING {args.host} ({destination})')

    received = 0
    rtts = []
    try:
        for sequence in range(1, args.count + 1):
            result = ping_once(sock, destination, identifier, sequence, args.timeout)
            if result is None:
                print(f'seq={sequence} timeout')
            else:
                address, rtt = result
                received += 1
                rtts.append(rtt)
                print(f'64 bytes from {address}: icmp_seq={sequence} time={rtt:.2f} ms')
            time.sleep(1)
    finally:
        sock.close()

    loss = ((args.count - received) / args.count) * 100
    print(f'--- {args.host} ping statistics ---')
    print(f'{args.count} packets transmitted, {received} received, {loss:.1f}% packet loss')
    if rtts:
        print(f'rtt min/avg/max = {min(rtts):.2f}/{sum(rtts) / len(rtts):.2f}/{max(rtts):.2f} ms')
    return 0


if __name__ == '__main__':
    sys.exit(main())
