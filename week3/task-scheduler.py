class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counter = collections.Counter(tasks)
        mostCountOfTasks = counter.most_common(1)[0][1]
        numberOfMostCountOfTasks = len([_ for _, count in counter.items() if count == mostCountOfTasks])
        interval = (mostCountOfTasks - 1) * (n + 1) + numberOfMostCountOfTasks
        return max(len(tasks), interval)
