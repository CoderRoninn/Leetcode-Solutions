class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        extra_fuel = min(additionalTank, (mainTank -1)//4)

        return (mainTank + extra_fuel) * 10
        