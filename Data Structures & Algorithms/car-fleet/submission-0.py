class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed = [s for _, s in sorted(zip(position, speed))]
        position.sort()
        m_time = (target - position[-1])/(speed[-1])
        fleet = 1

        for i in range(len(position)-2, -1, -1):
            if (target - position[i])/(speed[i]) <= m_time:
                continue
            else:
                m_time = (target - position[i])/(speed[i])
                fleet += 1
        return fleet
