import random

human_score = 0
computer_score = 0
human = ''
computer = ''
gameboard = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

def game():
    print('   1   2   3')

    for i in range(3):
        print(str(i + 1) + '  ' + gameboard[i][0] + ' | ' + gameboard[i][1] + ' | ' + gameboard[i][2])
        if i < 2:
            print('  -----------')


def score():
    print(f"Human Score: {human_score}\nComputer Score: {computer_score}")


def main():
    global gameboard, human, computer, human_score, computer_score

    print("Welcome to Tic Tac Toe!\n")
    game()  # Print the initial game board

    symbol = input("Would you like to be 'X' or 'O': ")

    if symbol.upper() == 'X':
        human = 'X'
        computer = 'O'
    else:
        human = 'O'
        computer = 'X'

    while True:
        score()

        row = int(input("Please provide an input for the row (1, 2, or 3): "))
        column = int(input("Please provide an input for the column (1, 2, or 3): "))
        gameboard[row - 1][column - 1] = symbol

        game()

        if check_winner(symbol):
            print("Congratulations! You won!")
            human_score += 1
            break

        if is_board_full():
            print("It's a tie!")
            break

        computer_response()  # Call the computer_response function

        game()

        if check_winner(computer):
            print("Sorry, you lost. The computer won.")
            computer_score += 1
            break

        if is_board_full():
            print("It's a tie!")
            break


def computer_response():
    print("Now here is the computer's response")
    while True:
        computer_row = random.randint(0, 2)
        computer_column = random.randint(0, 2)
        if gameboard[computer_row][computer_column] == ' ':
            gameboard[computer_row][computer_column] = computer
            break


def check_winner(symbol):
    # Check rows
    for row in gameboard:
        if row.count(symbol) == 3:
            return True

    # Check columns
    for col in range(3):
        if gameboard[0][col] == symbol and gameboard[1][col] == symbol and gameboard[2][col] == symbol:
            return True

    # Check diagonals
    if gameboard[0][0] == symbol and gameboard[1][1] == symbol and gameboard[2][2] == symbol:
        return True
    if gameboard[0][2] == symbol and gameboard[1][1] == symbol and gameboard[2][0] == symbol:
        return True

    return False


def is_board_full():
    for row in gameboard:
        if ' ' in row:
            return False
    return True


while True:
    main()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        reset_scores = input("Do you want to reset the scores? (yes/no): ")
        if reset_scores.lower() == 'yes':
            human_score = 0
            computer_score = 0
        break
