class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        carFleet = []

        pair = [[p,s] for p,s in zip(position, speed)]

        for p,s in sorted(pair)[::-1]:
            carFleet.append((float(target) - p) / s)
            if len(carFleet) >= 2 and carFleet[-1] <= carFleet[-2]:
                carFleet.pop()
        return len(carFleet)
            