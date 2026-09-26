class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        size = len(nums)
        for num in nums:
            freq[num] += 1
            if len(freq) <= 2:
                continue
            else:
                for k,v in freq.items():
                    freq[k] -= 1

                new_freq = freq.copy()
                for k,v in freq.items():
                    if v == 0:
                        new_freq.pop(k)
                
                freq = new_freq

        res = []
        for k, v in freq.items():
            if nums.count(k) > size//3:
                res.append(k)

        return res