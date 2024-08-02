import random
import sys
from colorama import Fore
from emoji import emojize as e

def get_types() -> list[dict]:
    """
    Return a list of eight dictionaries *IN THE ORDER LISTED BELOW*
    
    Each dictionary must have a 'name' property and a 'code' property, and the values for each dictionary must be unique
    
    The (string) name values must be:
        Kiwis
        Watermelons
        Cherries
        Lemons
        Grapes
        Bananas
        Apples
        Peaches
        
    and the corresponding (string) code values must be exactly:
        :kiwi_fruit:
        :watermelon:
        :cherries:
        :lemon:
        :grapes:
        :banana:
        :green_apple:
        :peach:
    """
    return [
        {'name': 'Kiwis', 'code': ':kiwi_fruit:'},
        {'name': 'Watermelons', 'code': ':watermelon:'},
        {'name': 'Cherries', 'code': ':cherries:'},
        {'name': 'Lemons', 'code': ':lemon:'},
        {'name': 'Grapes', 'code': ':grapes:'},
        {'name': 'Bananas', 'code': ':banana:'},
        {'name': 'Apples', 'code': ':green_apple:'},
        {'name': 'Peaches', 'code': ':peach:'}
    ]

def list_double(l: list) -> list:
    """
    Return a new list where all the values in l are repeated and placed at the end of the list,
        e.g. 
        if the input l is the list [1, 2, 3, 4], the output must be [1, 2, 3, 4, 1, 2, 3, 4]
        if the input l is the list ['a', 'b', 'c'], the output must be ['a', 'b', 'c', 'a', 'b', 'c']
    """
    return l + l

def valid_cards(cards: list[dict[str, str]]) -> bool:
    """
    Return True if all the following conditions are true:
        - Each card in the list of cards must be of type dict
        - Each card must have a 'name' property
        - Each card must have a 'code' property
        - The value of 'name' must be of type str
        - The value of 'code' must be of type str
        - Each card must appear in the list of cards twice

    else: 
        return False
    """
    names = set()
    for card in cards:
        if not isinstance(card, dict):
            return False
        if 'name' not in card or 'code' not in card:
            return False
        if not isinstance(card['name'], str) or not isinstance(card['code'], str):
            return False
        if card['name'] in names:
            return False
        names.add(card['name'])
    return len(names) == len(cards) // 2

def create_board(cards: list[dict[str, str]]) -> list[list[dict[str, str]]]:
    """
    Given a list of 16 shuffled cards, e.g.
        [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    
    create a new list of length 4 where the shuffled cards are placed, in order, into four rows (lists), e.g.:
        [
            [{}, {}, {}, {}],
            [{}, {}, {}, {}],
            [{}, {}, {}, {}],
            [{}, {}, {}, {}]
        ]

    and return the new list
    """
    board = []
    for i in range(0, len(cards), 4):
        board.append(cards[i:i+4])
    return board

def get_state(row: int, col: int, board: list[list[dict[str, str]]], revealed: set[tuple[int, int]], found: set[tuple[int, int]]) -> str:
    """
    If a tuple containing the row and col(umn), i.e. (row, col), is in the 'found' set:
        return the string ':black_large_square:'

    else if the tuple is in the 'revealed' set:
        return the 'code' property of the dictionary found in the board (at the position specified by the row and col parameters)

    else return the string ':white_large_square:'
    """
    if (row, col) in found:
        return ':black_large_square:'
    elif (row, col) in revealed:
        return board[row][col]['code']
    else:
        return ':white_large_square:'

def found_match(row: int, col: int, board: list[list[dict[str, str]]], revealed: set[tuple[int, int]], found: set[tuple[int, int]]) -> bool:
    """
    Extract the row and column found in the first (and only) tuple in the 'revealed' set
        (hint: use list(revealed)[0] to extract the values)
    and store them in variables called revealed_row and revealed_col

    If the 'name' values of the dictionaries found at the board positions specified by row/col and revealed_row/revealed_col match:
        add a tuple to the found set containing the row and col values e.g. (row, col)
        add another tuple to the found set containining the revealed_row and revealed_col values 
        clear the revealed set
        and return True
    
    else:
        add a tuple to the revealed set containing the row and col values
        and return False
    """
    if len(revealed) == 1:
        revealed_row, revealed_col = list(revealed)[0]
        if board[row][col]['name'] == board[revealed_row][revealed_col]['name']:
            found.add((row, col))
            found.add((revealed_row, revealed_col))
            revealed.clear()
            return True
        else:
            revealed.add((row, col))
            return False
    else:
        revealed.add((row, col))
        return False

def print_board(board: list[list[dict[str, str]]], revealed: set[tuple[int, int]], found: set[tuple[int, int]]) -> None:
    print()
    for row in range(len(board)):
        for col in range(len(board[row])):
            state = get_state(row, col, board, revealed, found)
            print(e(state), end='')
        print()

if __name__ == '__main__':
    cards = list_double(get_types())
    random.shuffle(cards)
    revealed = set()
    found = set()

    if valid_cards(cards):
        board = create_board(cards)
        while True:
            print_board(board, revealed, found)

            if len(found) == len(cards) // 2:
                print("Congratulations! You've found all the matches!")
                sys.exit()

            row = int(input("Please enter the row: ")) - 1
            col = int(input("Please enter the column: ")) - 1




