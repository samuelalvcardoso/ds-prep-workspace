from tictactoe import TicTacToe
from players import human_player, computer_player
from constants import CROSS
import pygame


def main():
    # Create a new game
    pygame.init()

    game = TicTacToe()
    
    # Game loop
    while game.running:
        
        if game.turn == CROSS:
            human_player(game)
        else:
            computer_player(game)

    
if __name__ == "__main__":
    main()
