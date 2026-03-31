# Week 4 Report: Network Layer – Forwarding and Routing

## Overview

This report covers the network layer, which is responsible for delivering packets across multiple networks. Unlike the physical and link layers that operate one hop at a time, the network layer enables end-to-end communication across the internet.

---

## Key Responsibilities

The network layer has three main responsibilities:

1. Addressing  
Every device must have a unique IP address so packets know where to go.

2. Forwarding  
Routers decide where to send each packet using a forwarding table. This happens very fast and is done for every packet.

3. Routing  
Routing determines what paths packets should take across the network. This is done using algorithms and happens slower than forwarding.

---

## Best-Effort Design

The Internet Protocol (IP) uses a best-effort approach:
- No guarantee of delivery
- No guarantee of order
- No guarantee of timing

This design keeps the network simple. Reliability is handled by higher layers like TCP.

---

## End-to-End Principle

The end-to-end argument says that certain features (like reliability) should be implemented at the endpoints, not inside the network.

Even if routers tried to guarantee delivery, the application would still need to check the data. So it is more efficient to keep the network simple and push complexity to the edges.

---

## Data Plane vs Control Plane

Routers operate using two main parts:

Data Plane:
- Fast
- Handles each packet
- Uses forwarding table

Control Plane:
- Slower
- Computes routes
- Builds routing tables

This separation allows routers to be both fast and flexible.

---

## Forwarding vs Routing

Forwarding:
- Local decision
- Happens per packet
- Very fast

Routing:
- Network-wide decision
- Uses algorithms
- Happens over time

---

## Router Architecture

A router has:
- Input ports (receive packets)
- Switching fabric (moves packets inside router)
- Output ports (send packets)
- Routing processor (runs control plane)

Queues may form when traffic is high, which can cause packet drops.

---

## Longest Prefix Match

Routers use longest-prefix match to decide where to send packets.

If multiple entries match an IP address, the router chooses the most specific one.

Example:
10.1.2.0/24 is preferred over 10.0.0.0/8

---

## Key Takeaways

- The network layer connects different networks together.
- IP is simple by design, which allows it to scale.
- Routers separate fast packet handling from slower route computation.
- Tradeoffs between simplicity and performance are central to networking.

---

## Reflection

This topic made networking feel more real to me. Before, I thought routers just “send stuff,” but now I understand there is a clear structure behind it. The idea of separating fast and slow tasks makes a lot of sense, especially for performance.

It also helped me understand why the internet works the way it does. Instead of trying to be perfect, it is designed to be simple and scalable.
