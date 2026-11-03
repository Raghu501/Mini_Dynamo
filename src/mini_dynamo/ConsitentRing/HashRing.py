#!/usr/bin/env python3
"""
Consistent Hash Ring
Commands (one per line from stdin):
  ADD <node> <position>   - add a node at the given ring position
  REMOVE <node>           - remove a node from the ring
  LOOKUP <position>       - print the node responsible for this position
"""
import sys
import bisect

class HashRing:
    def __init__(self):
        self.positions = []   # sorted list of integer positions
        self.ring = {}        # position -> node_id


#self.positions = [300, 700]
#self.ring = {
  #  300: "nodeB",
   # 700: "nodeC"
#}
    #Every position in self.positions must also exist as a key in self.ring.

    def add(self, node_id: str, *positions: int) -> None:
        """Add a node at a specific ring position."""

        for position in positions:
         if position in self.ring:
            raise ValueError(f"Position {position} already exists")

        for position in positions:
         bisect.insort(self.positions, position)
         self.ring[position] = node_id  


    def distribution(self) -> dict:
        """Count how many positions from 0 to 999 belong to each node."""

        dist = {}

        for position in range(1000):
            node = self.lookup(position)

            if node:
                dist[node] = dist.get(node, 0) + 1

        return dist

    def remove(self, node_id: str) -> None:
        # TODO: remove all positions belonging to node_id
        """Remove all positions belonging to the given node."""
        positions_to_remove = [pos for pos, current_node in self.ring.items() if current_node == node_id]

        for pos in positions_to_remove:
            del self.ring[pos]
            self.positions.remove(pos)       

    def lookup(self, position: int) -> str:
        #Find the first available node clockwise from the given position. If no node exists after that position, wrap around to the first node.
        # TODO: find the first node clockwise from position
        # Wrap around if position > all node positions
        #For example, if position is 950, there is no node after it. So we return to the first position, 100.
        #bisect_left() finds where to look in the sorted list. The dictionary then tells you which node owns that position.
        if not self.positions:
         return ""
        index = bisect.bisect_left(self.positions,position)
        if index==len(self.positions):
            index=0

        return self.ring[self.positions[index]]
def main():
    ring = HashRing()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]
        if cmd == 'ADD':
            ring.add(parts[1], *map(int, parts[2:]))
        elif cmd == 'REMOVE':
            ring.remove(parts[1])
        elif cmd == 'LOOKUP':
            print(ring.lookup(int(parts[1])))
        elif cmd == 'DISTRIBUTION':
            dist = ring.distribution()
            for node in sorted(dist):
                print(f'{node}:{dist[node]}')

if __name__ == '__main__':
    main()
