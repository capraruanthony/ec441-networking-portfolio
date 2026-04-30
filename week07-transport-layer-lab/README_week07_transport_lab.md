# Week 7 Lab: Transport Layer - Stop-and-Wait vs Sliding Window

## Overview
This lab explores reliable data transfer at the transport layer. It compares Stop-and-Wait with sliding window behavior and shows why pipelining is needed on high-bandwidth-delay-product paths.

## Topics Covered
- Transport-layer reliability
- Stop-and-Wait utilization
- Bandwidth-delay product
- Sliding window throughput
- Go-Back-N behavior during loss
- Selective Repeat behavior during loss

## Files
- `week07_transport_stop_and_wait_lab.py` — main Python lab script

## How to Run
```bash
python3 week07_transport_stop_and_wait_lab.py
```

## What the Script Does
1. Calculates packet transmission time
2. Computes Stop-and-Wait utilization
3. Computes bandwidth-delay product
4. Estimates the window size needed to fill the pipe
5. Compares different sliding window sizes
6. Demonstrates how Go-Back-N and Selective Repeat respond to a lost packet

## Conclusion
The main takeaway is that correctness is not enough. Stop-and-Wait can deliver data reliably, but it wastes most of the link on high-delay paths. Sliding window protocols improve utilization by keeping multiple packets in flight.
