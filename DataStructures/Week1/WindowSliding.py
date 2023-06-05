def max_sliding_window_naive(sequence, m):
    maximums = []
    queue = []
    for i in range(len(sequence)):
        if queue and queue[0] == i-m:
            queue.pop(0)
        while queue and sequence[queue[-1]] < sequence[i]:
            queue.pop()
        queue.append(i)
        if i >= m-1:
            maximums.append(sequence[queue[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window_naive(input_sequence, window_size))