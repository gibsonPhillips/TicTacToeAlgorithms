from Gamefourpi import *
import time


def main():
    tic = time.perf_counter()
    game = TicTacToe()
    nextState = game.initial
    game.display(nextState)
    print()
    print("Current State: ", nextState)
    player = nextState.to_move
    print("Available Action by the Player " + player + ": ",
          game.actions(nextState))
    randomPlayerAction = random_player(game, nextState)
    print("The Action by the Player " + nextState.to_move + " Is", randomPlayerAction)
    nextState = game.result(nextState, randomPlayerAction)
    game.display(nextState)
    print()
    utility = game.compute_utility(nextState.board, randomPlayerAction, player)
    print("Player " + player + "'s Utility: ", utility)
    print()
    player = nextState.to_move
    mctsPlayerAction = mcts_player(game, nextState)
    nextState = game.result(nextState, mctsPlayerAction)
    game.display(nextState)
    print()
    utility = game.compute_utility(nextState.board, mctsPlayerAction, player)
    print("Player " + player + "'s Utility: ", utility)
    print()
    terminate = game.terminal_test(nextState)

    while not terminate:
        player = nextState.to_move


    if player == "X":
        randomPlayerAction = random_player(game, nextState)
        nextState = game.result(nextState, randomPlayerAction)
        game.display(nextState)
        print()
        utility = game.compute_utility(nextState.board, randomPlayerAction, player)
        print("Player " + player + "'s Utility: ", utility)

        if utility == 1:
            print("Player " + player + " won the game.")
        terminate = game.terminal_test(nextState)
        print()
    else:
        mctsPlayerAction = mcts_player(game, nextState)
        nextState = game.result(nextState, mctsPlayerAction)
        game.display(nextState)
        print()
        utility = game.utility(nextState, player)
        print("Player " + player + "'s Utility: ", utility)
        if utility == 1:
            print("Player " + player + " won the game.")
        terminate = game.terminal_test(nextState)
        print()
    toc = time.perf_counter()
    print(f"Game Completion in {toc - tic:0.4f} seconds")
if __name__ == "__main__":
    main()
