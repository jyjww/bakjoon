def move(no: int, x: int, y: int, moves:list) -> int:
    if no > 1:
        move(no-1, x, 6-x-y, moves)
    moves.append(f'{x} {y}')
    if no > 1 and x != y:
        move(no-1, 6-x-y, y, moves)
if __name__ == '__main__':
    n = int(input())
    moves = []
    print((2**n)-1)
    if n <= 20 : 
        total_moves = move(n, 1, 3, moves)
        for move_step in moves :
            print(move_step)