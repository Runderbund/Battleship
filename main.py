if __name__ == '__main__':
    game = Game()
    game.run_game()

    # Make 10 x 10 2D list
    # Add border and maybe between
    board = [[" " for j in range(10)] for i in range(10)]
    
    # or 
    my_list = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(" ")
        my_list.append(row)