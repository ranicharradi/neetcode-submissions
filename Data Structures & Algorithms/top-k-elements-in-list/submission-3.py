class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse=True)
        print(items[0])
        return [i for i, _ in items[:k]]
