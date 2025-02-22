class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, column = 0, 0

        for operation in commands:
            if operation == "UP":
                row -= 1
            elif operation == "DOWN":
                row += 1
            elif operation == "LEFT":
                column -= 1
            else:
                column += 1

        return (row * n) + column                   

        