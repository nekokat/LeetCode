from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        o = sorted(Counter(words).items(), key=lambda k: (-k[1], k[0]))
        return [i for i,j in o[0:k]]
