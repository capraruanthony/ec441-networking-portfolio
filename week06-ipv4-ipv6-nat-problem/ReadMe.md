# Week 6 Problem Set: IPv4, IPv6, NAT, and ICMP

## Overview
This problem set uses Python to work through several network-layer problems based on Lecture 17. The script prints both the questions and fully worked solutions.

## Topics Covered
- IPv4 header fields
- TTL and traceroute
- IP fragmentation
- NAT / PAT translation
- ICMP message types
- IPv4 vs IPv6 design differences

## Files
- `week06_ipv4_ipv6_nat_icmp_problem.py` — main problem set script

## How to Run
```bash
python3 week06_ipv4_ipv6_nat_icmp_problem.py
```

## What the Script Does
1. Solves an IPv4 header interpretation problem
2. Computes hop count using TTL
3. Calculates fragmentation for a 4000-byte datagram on a 1500-byte MTU link
4. Simulates NAT translation for a private host
5. Explains why fragmentation is problematic
6. Compares IPv4 and IPv6
7. Matches ICMP types to networking tasks

## Why This Fits the Course
This problem set directly applies the core ideas from Lecture 17:
- what routers examine in the IPv4 header
- how ICMP supports ping, traceroute, and PMTUD
- why fragmentation is problematic
- how NAT rewrites addresses and ports
- how IPv6 simplifies the network layer

## Conclusion
This file is a worked problem set, not just a demo. It shows how the concepts from the lecture can be turned into concrete calculations and protocol-level reasoning.
