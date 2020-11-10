# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:03:14 2020

@author: v.a.subhash.krishna
"""

import sys
table = ['#','#','#','#','#','#','#','#','#']

def display():
    rows = [table[i:i+3] for i in range(9) if not i % 3]
    for row in rows:
        print('-------------')
        print('| '+' | '.join(row).replace('#',' ')+' |')
    print('-------------')
    

def marker_selection():
    while True:
        player1 = input('Please Pick a marker for Player 1 ("X" or "O"): ')
        if player1 == 'X':
            player2 = 'O'
            break
        elif player1 == 'O':
            player2 = 'X'
            break
        else:
            print('Invalid marker. Please try again...')
    print(f'Player1 is {player1}, Player2 is {player2}')
    return player1,player2

def check_win(table, marker):
    result = False
    rows = [table[i:i+3] for i in range(9) if not i % 3]
    cols = [[],[],[]]
    dgl = [[],[]]
    for i in range(len(rows)):
        cols[0].append(rows[i][0])
        cols[1].append(rows[i][1])
        cols[2].append(rows[i][2])
        dgl[0].append(rows[i][2-i])
        dgl[1].append(rows[i][i])
        result = all(element == marker for element in rows[i])
        if result:
            return result
    for col in cols:
        result = all(element == marker for element in col)
        if result:
            return result
    for val in dgl:
        result = all(element == marker for element in val)
        if result:
            return result
    
    return result


def start_game():
    global table
    player1 = ''
    player2 = ''
    player1, player2 = marker_selection()
    P1_turn = True
    while True:
        display()
        if P1_turn:
            marker = player1
            no = 1
        else:
            marker = player2
            no = 2
        pos = int(input(f'Enter position player {no} want to mark: '))-1
        if table[pos] != '#' or pos:
            print('Invalid position... Enter valid position!!!')
            continue
        table[pos] = marker
        P1_turn = False if P1_turn else True
        if check_win(table, marker):
            display()
            print(f'Congratulations player {no} won the game...!!!')
            option = input('Want to play again (Yes or No): ')
            table = ['#','#','#','#','#','#','#','#','#']
            if option.lower() == 'yes':
                start_game()
            break
                
        if '#' not in table:
            display()
            option = input('Matched tied....Want to play again (Yes or No): ')
            table = ['#','#','#','#','#','#','#','#','#']
            if option.lower() == 'yes':
                start_game()
            break

if __name__ == '__main__':
    start_game()