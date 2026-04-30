# Week 8 Problem Set: Application Layer - DNS, HTTP, and QUIC

## Overview
This problem set uses Python to print worked application-layer questions and solutions. It focuses on DNS, HTTP, MIME types, HTTP version evolution, QUIC, and WebSocket.

## Topics Covered
- Application-layer protocol design patterns
- DNS resolution and caching
- HTTP/1.1 request/response
- MIME types and Content-Type
- HTTP/2 multiplexing
- HTTP/3 and QUIC
- WebSocket push communication

## Files
- `week08_application_layer_problem_set.py` — main problem set script

## How to Run
```bash
python3 week08_application_layer_problem_set.py
```

## What the Script Does
1. Classifies HTTP/1.1 using protocol design axes
2. Walks through DNS resolution
3. Solves a DNS TTL caching problem
4. Writes and explains a basic HTTP/1.1 request
5. Interprets MIME Content-Type
6. Compares HTTP/1.1, HTTP/2, and HTTP/3
7. Explains why QUIC uses UDP
8. Explains when WebSocket is useful

## Conclusion
The main takeaway is that application-layer protocols are design choices. Different applications choose different tradeoffs depending on latency, state, reliability, debugging, scalability, and deployment constraints.
