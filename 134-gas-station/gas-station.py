class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas, total_gas = 0, 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]

        if total_gas < 0:
            return -1
        
        station_index = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                station_index = i+1
                current_gas = 0
        return station_index
        