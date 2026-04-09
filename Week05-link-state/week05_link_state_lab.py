#!/usr/bin/env python3
"""
Week 5 Lab: Link-State Routing and Dijkstra's Algorithm

EC 441 - Intro to Computer Networking

This lab script models a small router network as a weighted graph, runs
Dijkstra's algorithm from a chosen source router, prints a step-by-step trace,
builds a forwarding table from the shortest-path tree, and then simulates a
link failure / large cost increase to show how routing changes.

Run:
    python3 week05_link_state_lab.py
"""

from math import inf


class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, cost):
        self.adj.setdefault(u, {})[v] = cost
        self.adj.setdefault(v, {})[u] = cost

    def nodes(self):
        return sorted(self.adj.keys())

    def neighbors(self, u):
        return self.adj.get(u, {}).items()

    def copy(self):
        g = Graph()
        for u in self.adj:
            for v, cost in self.adj[u].items():
                if u < v:
                    g.add_edge(u, v, cost)
        return g


def build_lecture_graph():
    g = Graph()
    edges = [
        ("u", "v", 2),
        ("u", "w", 1),
        ("u", "x", 5),
        ("v", "y", 3),
        ("w", "y", 3),
        ("w", "z", 2),
        ("x", "z", 1),
        ("y", "z", 4),
    ]
    for u, v, cost in edges:
        g.add_edge(u, v, cost)
    return g


def initialize(g, source):
    dist = {node: inf for node in g.nodes()}
    prev = {node: None for node in g.nodes()}
    dist[source] = 0
    return dist, prev


def dijkstra(g, source):
    dist, prev = initialize(g, source)
    unvisited = set(g.nodes())
    finalized = []
    trace_rows = []

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)
        finalized.append(current)

        for neighbor, cost in g.neighbors(current):
            if neighbor in unvisited:
                new_cost = dist[current] + cost
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    prev[neighbor] = current

        trace_rows.append({
            "selected": current,
            "finalized": finalized.copy(),
            "dist": dist.copy(),
            "prev": prev.copy(),
        })

    return dist, prev, trace_rows


def reconstruct_path(prev, source, dest):
    if dest == source:
        return [source]

    path = []
    current = dest
    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()
    if path and path[0] == source:
        return path
    return None


def print_graph(g, title):
    print("\n" + "=" * 64)
    print(title)
    print("=" * 64)
    for u in g.nodes():
        neighbors = ", ".join(f"{v}(cost={c})" for v, c in sorted(g.neighbors(u)))
        print(f"{u}: {neighbors}")


def print_trace(trace_rows, source):
    nodes = sorted(trace_rows[0]["dist"].keys())
    non_source = [n for n in nodes if n != source]

    print("\nStep-by-step Dijkstra trace")
    header = f"{'Step':<5} {'Selected':<10} {'N_prime':<20}"
    for node in non_source:
        header += f"{'D(' + node + '),p(' + node + ')':<14}"
    print(header)
    print("-" * len(header))

    for i, row in enumerate(trace_rows):
        n_prime = "{" + ",".join(row["finalized"]) + "}"
        line = f"{i:<5} {row['selected']:<10} {n_prime:<20}"
        for node in non_source:
            d = row["dist"][node]
            p = row["prev"][node]
            d_str = "∞" if d == inf else str(int(d))
            p_str = "-" if p is None else p
            line += f"{(d_str + ',' + p_str):<14}"
        print(line)


def print_shortest_paths(dist, prev, source):
    print("\nShortest paths from source router", source)
    print(f"{'Destination':<12} {'Cost':<8} Path")
    print("-" * 40)
    for dest in sorted(dist.keys()):
        if dest == source:
            continue
        path = reconstruct_path(prev, source, dest)
        cost = dist[dest]
        path_str = " -> ".join(path) if path else "unreachable"
        print(f"{dest:<12} {int(cost):<8} {path_str}")


def print_forwarding_table(dist, prev, source):
    print("\nForwarding table derived from the shortest-path tree")
    print(f"{'Destination':<12} {'Next Hop':<10} {'Cost':<8} Path")
    print("-" * 52)
    for dest in sorted(dist.keys()):
        if dest == source:
            continue
        path = reconstruct_path(prev, source, dest)
        if not path or len(path) < 2:
            next_hop = "-"
            path_str = "unreachable"
        else:
            next_hop = path[1]
            path_str = " -> ".join(path)
        print(f"{dest:<12} {next_hop:<10} {int(dist[dest]):<8} {path_str}")


def print_link_change_comparison(old_dist, old_prev, new_dist, new_prev, source):
    print("\nComparison after topology change")
    print(f"{'Dest':<8} {'Old next':<10} {'New next':<10} {'Old cost':<10} {'New cost':<10} Changed")
    print("-" * 68)

    for dest in sorted(old_dist.keys()):
        if dest == source:
            continue

        old_path = reconstruct_path(old_prev, source, dest)
        new_path = reconstruct_path(new_prev, source, dest)

        old_next = old_path[1] if old_path and len(old_path) >= 2 else "-"
        new_next = new_path[1] if new_path and len(new_path) >= 2 else "-"

        changed = (old_next != new_next) or (old_dist[dest] != new_dist[dest])
        changed_str = "yes" if changed else "no"

        print(
            f"{dest:<8} {old_next:<10} {new_next:<10} "
            f"{int(old_dist[dest]):<10} {int(new_dist[dest]):<10} {changed_str}"
        )


def main():
    source = "u"

    g = build_lecture_graph()
    print_graph(g, "Original network graph")
    dist, prev, trace = dijkstra(g, source)
    print_trace(trace, source)
    print_shortest_paths(dist, prev, source)
    print_forwarding_table(dist, prev, source)

    g2 = g.copy()
    g2.add_edge("w", "z", 100)

    print_graph(g2, "Modified graph: link w-z cost changed to 100")
    dist2, prev2, trace2 = dijkstra(g2, source)
    print_trace(trace2, source)
    print_shortest_paths(dist2, prev2, source)
    print_forwarding_table(dist2, prev2, source)

    print_link_change_comparison(dist, prev, dist2, prev2, source)

    print("\nLab conclusion:")
    print("- Link-state routing gives every router the same topology map.")
    print("- Dijkstra builds a shortest-path tree rooted at the source router.")
    print("- The forwarding table only needs the first hop of each shortest path.")
    print("- When a link cost changes, routers recompute and may choose new paths.")


if __name__ == "__main__":
    main()
