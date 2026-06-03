from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calculate(firstStart, firstDur, secondStart, secondDur):

            earliest_end = float('inf')

            for s, d in zip(firstStart, firstDur):
                earliest_end = min(earliest_end, s + d)

            answer = float('inf')

            for s, d in zip(secondStart, secondDur):
                answer = min(answer, max(earliest_end, s) + d)

            return answer

        land_to_water = calculate(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        water_to_land = calculate(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_to_water, water_to_land)