# Week 5 Lab: Link-State Routing and Dijkstra's Algorithm

## Overview
This lab explores how routers compute shortest paths in a network using **link-state routing** and **Dijkstra’s algorithm**. A network is modeled as a weighted graph where routers are nodes and links are edges with costs.

## Objectives
- Represent a network as a graph
- Run Dijkstra’s algorithm from a source router
- Build a shortest-path tree (SPT)
- Generate a forwarding table
- Observe how routing changes when a link cost increases

## Files
- `week05_link_state_lab.py` — main lab script

## How to Run
```bash
python3 week05_link_state_lab.py
```

## What the Script Does
1. Builds the network graph from lecture
2. Runs Dijkstra’s algorithm step by step
3. Prints shortest paths from the source router
4. Generates a forwarding table (next-hop decisions)
5. Simulates a link failure (cost increase)
6. Recomputes routes and compares changes

## Key Concepts
- Link-state routing gives every router a full network map
- Dijkstra finds the lowest-cost paths from a source
- The forwarding table uses only the **first hop** of each path
- Routing updates when topology changes

## Conclusion
This lab demonstrates how routers dynamically compute and update routes using graph algorithms. It shows why Dijkstra’s algorithm is essential for protocols like OSPF.
