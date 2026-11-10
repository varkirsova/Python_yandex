from gameparts import Board

def main():
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display()
    

# А вот вызов этой функции.
if __name__ == '__main__':
    main()