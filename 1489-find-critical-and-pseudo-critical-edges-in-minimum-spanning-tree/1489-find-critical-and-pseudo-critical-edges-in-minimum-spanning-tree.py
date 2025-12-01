class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges_with_indices = [(weight, fr, to, idx) for idx, [fr, to, weight] in enumerate(edges)]
        edges_with_indices.sort(key=lambda x: x[0])

        def find(x, parent):
            if x != parent[x]:
                parent[x] = find(parent[x], parent)

            return parent[x]

        def union(x, y, parent):
            r_x = find(x, parent)
            r_y = find(y, parent)

            if r_x == r_y:
                return False

            parent[r_x] = parent[r_y]
            return True
            

        def find_MST(exclude_idx=set(), parent=None, num_edge_in_mst=0, init_w=0):
            if parent == None:
                parent = [i for i in range(n)]
            mst_weight = init_w
            
            for w, fr, to, idx in edges_with_indices:
                if idx in exclude_idx:
                    continue
                if num_edge_in_mst == n - 1:
                    break
                
                if find(fr, parent) == find(to, parent):
                    continue
                
                union(fr, to, parent)
                mst_weight += w
                num_edge_in_mst += 1

            return mst_weight if num_edge_in_mst == n - 1 else -1
                
        min_w = find_MST()
        critical_edges = set()

        for i in range(len(edges)):
            weight = find_MST(set([i]))
            if weight != min_w:
                critical_edges.add(i)

        pesudo_critical_edges = set()
        for i in range(len(edges)):
            if i in critical_edges:
                continue
            fr, to, w = edges[i]

            parent = [i for i in range(n)]
            union(fr, to, parent)

            weight = find_MST(set(), parent, 1, init_w=w)

            if weight == min_w:
                pesudo_critical_edges.add(i)
        
        return [list(critical_edges), list(pesudo_critical_edges)]
            
        