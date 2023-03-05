import os
from collections import deque

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def compute_height(root, nodes):
    queue = deque([root])
    height = 0

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            for child in node.children:
                queue.append(child)

        height += 1

    return height

if __name__ == '__main__':
    input_type = input("Enter input type (I for input, F for file): ")
    if input_type == "F":
        while True:
            test_name = input("Enter the test name: ")
            filename = f"test/{test_name}"
            if os.path.isfile(filename):
                with open(filename, 'r') as file:
                    n = int(file.readline().strip())
                    parents = list(map(int, file.readline().strip().split()))
                break
            else:
                print("File not found. Please enter a valid test name.")
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    nodes = [Node(i) for i in range(n)]
    root = None
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent_index]
            parent_node.add_child(nodes[i])

    height = compute_height(root, nodes)
    print(height)
