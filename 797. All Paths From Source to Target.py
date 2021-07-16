class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = '0'
        output = []

        queue = [(0, path)]
        target = len(graph) - 1
        while queue:
            node, path = queue.pop(0)

            nodes = graph[node]
            for node in nodes:
                new_path = path + ',' + str(node)
                queue.append((node, new_path))

                if node == target:
                    new_path = path + ',' + str(node)
                    output.append(new_path)
                    queue.append((node, new_path))

        result = []
        for path in output:
            np = list(map(int, path.split(',')))
            result.append(np)

        return result
