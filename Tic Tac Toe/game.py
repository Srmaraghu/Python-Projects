class TicTacToe:
    def __init__(self) :
        self.board=[' ' for _ in range(9)] 
        self.current_winner=None

    def print_board(self):
        # To get the rows.
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' +' | '.join(row) + ' |')
        
    @staticmethod
    def print_board_nums():
        number_board=[[str(i) for i in range (j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' +' | '.join(row) + ' |')

    def available_moves(self):
        # moves=[]
        # for (i,spot) in enumerate(self.board):
        #     if spot==' ':   #it means that it's a empty space in the board
        #         moves.append(i)  #it adds the avialbale spot's index to moves empty list

        # return moves  #returns the spots where moves are possible

        #above lines in the function can be condensed to one single line as follows:
        return [i for i, spot in enumerate(self.board) if spot=' ']