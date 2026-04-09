#!/usr/bin/env python3
"""
Week 6 Problem Set: IPv4, IPv6, NAT, and ICMP

EC 441 - Introduction to Computer Networking

This script works through a small set of network-layer problems based on:
- IPv4 header fields
- ICMP
- fragmentation
- NAT / PAT
- IPv4 vs IPv6 design choices

Run:
    python3 week06_ipv4_ipv6_nat_icmp_problem.py
"""

import math


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def problem_1() -> None:
    section("Problem 1: IPv4 Header Basics")

    total_length = 84
    ihl = 5
    ttl = 64
    protocol = 1

    header_length_bytes = ihl * 4
    payload_size = total_length - header_length_bytes

    print("Question:")
    print("An IPv4 datagram has IHL = 5, Total Length = 84, TTL = 64, Protocol = 1.")
    print("Find:")
    print("1. Header length in bytes")
    print("2. Payload size")
    print("3. Which upper-layer protocol is being carried")
    print("\nSolution:")
    print(f"1. Header length = IHL × 4 = {ihl} × 4 = {header_length_bytes} bytes")
    print(f"2. Payload size = Total Length - Header Length = {total_length} - {header_length_bytes} = {payload_size} bytes")
    print(f"3. Protocol = {protocol}, which means ICMP")


def problem_2() -> None:
    section("Problem 2: TTL and Traceroute")

    initial_ttl = 64
    hops = 9
    observed_ttl = initial_ttl - hops

    print("Question:")
    print("A Linux host sends a packet with initial TTL = 64.")
    print("If the reply arrives with observed TTL = 55, approximately how many hops did it travel?")
    print("\nSolution:")
    print(f"Hops ≈ initial TTL - observed TTL = 64 - 55 = {hops}")
    print("So the path length is about 9 hops.")
    print("This is the same TTL idea traceroute uses: routers decrement TTL by 1 at each hop.")


def fragment_datagram(total_size: int, header_size: int, mtu: int):
    payload = total_size - header_size
    max_payload_per_fragment = ((mtu - header_size) // 8) * 8

    fragments = []
    offset = 0
    while offset < payload:
        frag_payload = min(max_payload_per_fragment, payload - offset)
        more_fragments = 0 if offset + frag_payload >= payload else 1
        fragments.append({
            "total_length": header_size + frag_payload,
            "mf": more_fragments,
            "offset_units": offset // 8,
            "offset_bytes": offset,
            "payload_bytes": frag_payload,
        })
        offset += frag_payload
    return fragments


def problem_3() -> None:
    section("Problem 3: Fragmentation Arithmetic")

    total_size = 4000
    header_size = 20
    mtu = 1500

    fragments = fragment_datagram(total_size, header_size, mtu)

    print("Question:")
    print("A 4000-byte IPv4 datagram enters a link with MTU = 1500 bytes.")
    print("Assume a 20-byte IP header. Compute the fragments.")
    print("\nSolution:")
    print(f"Original payload = {total_size} - {header_size} = {total_size - header_size} bytes")
    print(f"Max payload per fragment = floor(({mtu} - {header_size}) / 8) × 8 = {((mtu - header_size) // 8) * 8} bytes")
    print()

    for i, frag in enumerate(fragments, start=1):
        print(
            f"Fragment {i}: Total Length = {frag['total_length']}, "
            f"MF = {frag['mf']}, "
            f"Offset = {frag['offset_units']} "
            f"(= {frag['offset_bytes']} bytes), "
            f"Payload = {frag['payload_bytes']} bytes"
        )

    extra_header_overhead = sum(f["total_length"] for f in fragments) - total_size
    print(f"\nTotal fragments: {len(fragments)}")
    print(f"Extra overhead from added headers: {extra_header_overhead} bytes")
    print("Key point: if any one fragment is lost, the whole datagram is lost.")


def problem_4() -> None:
    section("Problem 4: NAT / PAT Translation")

    public_ip = "128.197.10.1"
    private_ip = "10.0.0.2"
    private_port = 5001
    translated_port = 40001
    destination = "142.250.80.46:443"

    print("Question:")
    print("A host 10.0.0.2:5001 sends a packet to 142.250.80.46:443.")
    print("The NAT router has public IP 128.197.10.1 and assigns WAN port 40001.")
    print("What does the outgoing packet look like, and how is the reply mapped back?")
    print("\nSolution:")
    print(f"Outgoing before NAT:  {private_ip}:{private_port} -> {destination}")
    print(f"Outgoing after NAT:   {public_ip}:{translated_port} -> {destination}")
    print(f"Incoming reply:       142.250.80.46:443 -> {public_ip}:{translated_port}")
    print(f"After reverse NAT:    142.250.80.46:443 -> {private_ip}:{private_port}")
    print("\nThis is Port Address Translation (PAT):")
    print("- NAT rewrites the source IP")
    print("- NAT rewrites the source port")
    print("- NAT stores the mapping in a translation table")


def problem_5() -> None:
    section("Problem 5: Why Fragmentation Is Problematic")

    print("Question:")
    print("List two reasons why IPv4 fragmentation is considered problematic.")
    print("\nSolution:")
    print("1. If one fragment is lost, the destination cannot reassemble the original datagram.")
    print("2. Every fragment carries its own IP header, which adds overhead.")
    print("Other valid reasons:")
    print("- Reassembly is complex")
    print("- Fragmentation has historically caused security issues")
    print("- Path MTU Discovery is preferred in modern networks")


def problem_6() -> None:
    section("Problem 6: IPv4 vs IPv6")

    print("Question:")
    print("Give three major differences between IPv4 and IPv6.")
    print("\nSolution:")
    print("1. Address size:")
    print("   IPv4 = 32 bits")
    print("   IPv6 = 128 bits")
    print("2. Header structure:")
    print("   IPv4 header = 20 to 60 bytes (variable)")
    print("   IPv6 header = 40 bytes (fixed)")
    print("3. Fragmentation:")
    print("   IPv4 routers may fragment packets in transit")
    print("   IPv6 routers do not fragment in transit; only endpoints do")
    print("\nOther good differences:")
    print("- IPv6 removes the header checksum")
    print("- IPv6 replaces broadcast with multicast")
    print("- IPv6 uses Next Header instead of Protocol")


def problem_7() -> None:
    section("Problem 7: ICMP Types")

    print("Question:")
    print("Match each networking task with the ICMP message type used:")
    print("A. ping request")
    print("B. ping reply")
    print("C. traceroute hop discovery")
    print("D. Path MTU Discovery")
    print("\nSolution:")
    print("A. ICMP Echo Request (Type 8, Code 0)")
    print("B. ICMP Echo Reply (Type 0, Code 0)")
    print("C. ICMP Time Exceeded (Type 11, Code 0)")
    print("D. ICMP Destination Unreachable: Fragmentation Needed (Type 3, Code 4)")


def reflection() -> None:
    section("Reflection")

    print("This problem set made the network layer feel more concrete.")
    print("Instead of just memorizing IPv4 fields, I had to actually use them in calculations")
    print("like payload size, fragmentation offsets, TTL, and NAT translation.")
    print("The biggest takeaway for me is that many network-layer features are really tradeoffs.")
    print("Fragmentation makes delivery possible across different MTUs, but it creates overhead")
    print("and reliability issues. NAT saved IPv4, but it breaks clean end-to-end communication.")
    print("IPv6 fixes many older design issues, but the transition is slow because IPv4 plus NAT")
    print('has been "good enough" for a long time.')


def main() -> None:
    print("Week 6 Problem Set: IPv4, IPv6, NAT, and ICMP")
    print("Running worked solutions...")
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()
    problem_7()
    reflection()


if __name__ == "__main__":
    main()
