# implementation using heapq

import heapq

n_workers, n_jobs = map(int, input().split())
jobs = list(map(int, input().split()))
assert len(jobs) == n_jobs
workers = []
for i in range(n_workers):
    heapq.heappush(workers, (0, i))
for i in range(n_jobs):
    time, worker = heapq.heappop(workers)
    print(worker, time)
    heapq.heappush(workers, (time+jobs[i], worker))

##################

# implementation from scratch

# from collections import namedtuple

# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
      
# def sift_down(i, H, size):
#     min_idx = i
#     l = 2 * i + 1
#     if l < size and (H[l][1] < H[min_idx][1] or H[l][1] == H[min_idx][1] and H[l][0] < H[i][0]):
#             min_idx = l
#     r = 2 * i + 2
#     if r < size and (H[r][1] < H[min_idx][1] or H[r][1] == H[min_idx][1] and H[r][0] < H[i][0]):
#             min_idx = r
#     if i != min_idx:
#         H[i], H[min_idx] = H[min_idx], H[i]
#         sift_down(min_idx, H, size)

# def sift_up(i, H):
#     while i > 0 and (H[(i+1)//2][1] > H[i][1] or H[(i+1)//2][1] == H[i][1] and H[(i+1)//2][0] > H[i][0]):
#         H[(i+1)//2], H[i] = H[i], H[(i+1)//2]
#         i = (i+1)//2

# def insert(p, H):
#     H.append(p)
#     sift_up(p, H)

# def extract_min(H):
#     res = H[0]
#     H[0] = H[len(H) - 1]
#     sift_down(0)
#     return res

# def remove(i, H):
#     H[i] = -1
#     sift_up(i, H)
#     extract_min(H)

# def build_heap(H):
#      for i in range(len(H)//2 - 1, -1, -1):
#         sift_down(i, H, len(H))

# def assign_jobs(n_workers, jobs):
#     result = []
#     next_free_time = [[i, 0] for i in range(n_workers)] # min-heap
#     for job in jobs:
#         build_heap(next_free_time)
#         next_worker = next_free_time[0]
#         result.append(AssignedJob(next_worker[0], next_worker[1]))
#         next_free_time[0][1] += job
#         sift_down(0, next_free_time, n_workers)
#     return result

# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     assert len(jobs) == n_jobs
#     assigned_jobs = assign_jobs(n_workers, jobs)
#     for job in assigned_jobs:
#         print(job.worker, job.started_at)


# if __name__ == "__main__":
#     main()
