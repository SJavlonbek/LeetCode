def queensAttacktheKing(queens, king):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    queens_set = {(x, y) for x, y in queens}
    print(queens_set)
    attacking_queens = []

    for dx, dy in directions:
        x, y = king[0], king[1]
        while 0 <= x < 8 and 0 <= y < 8:
            if (x, y) in queens_set:
                attacking_queens.append([x, y])
                break
            x += dx
            y += dy

    return attacking_queens

queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0, 0]
print(queensAttacktheKing(queens, king))  
