class Piece:
    
    def __init__(self,color,position):
        self.color=color
        self.position=position
    
class Pawn(Piece):
    
    def legal_move(self):
        available_move=[]
        if self.color=="White":
            available_move.append([self.position[0],self.position[1]+1])
            if self.position[1]==2:
                available_move.append([self.position[0],self.position[1]+2])
        else:
            available_move.append([self.position[0],self.position[1]-1])
            if self.position[1]==7:
                available_move.append([self.position[0],self.position[1]-2])
        return available_move
    
    def capture(self):
        available_capture=[]
        if self.color=="White":
            available_capture=[[self.position[0]+1,self.position[1]+1],[self.position[0]-1,self.position[1]+1]]
        else:
            available_capture=[[self.position[0]+1,self.position[1]-1],[self.position[0]-1,self.position[1]-1]]
        
        return available_capture
                
    def _logo(self):
        return f"p"
    
    def __str__(self):
        return f"{self.color} Pawn in {self.position}"

class Rook(Piece):
    
    def legal_move(self):
        available_move=[]
        for i in range(1,8):
            if (self.position[0]+i)==9:
                break
            available_move.append([self.position[0]+i,self.position[1]])
        for i in range(1,8):
            if (self.position[0]-i)==0:
                break
            available_move.append([self.position[0]-i,self.position[1]])
        for i in range(1,8):
            if (self.position[1]+i)==9:
                break
            available_move.append([self.position[0],self.position[1]+i])
        for i in range(1,8):
            if (self.position[1]-i)==0:
                break
            available_move.append([self.position[0],self.position[1]-i])
        return available_move
    
    def capture(self):
        return self.legal_move()
    
    def _logo(self):
        return f"R"
    
    def __str__(self):
        return f"{self.color} Rook in {self.position}"

class Bishop(Piece):
    
    def legal_move(self):
        available_move=[]
        for i in range(1,8):
            if (self.position[0]+i)==9 or (self.position[1]+i)==9:
                break
            available_move.append([self.position[0]+i,self.position[1]+i])
        for i in range(1,8):
            if (self.position[0]-i)==0 or (self.position[1]-i)==0:
                break
            available_move.append([self.position[0]-i,self.position[1]-i])
        for i in range(1,8):
            if (self.position[0]+i)==9 or (self.position[1]-i)==0:
                break
            available_move.append([self.position[0]+i,self.position[1]-i])
        for i in range(1,8):
            if (self.position[0]-i)==0 or (self.position[1]+i)==9:
                break
            available_move.append([self.position[0]-i,self.position[1]+i])
        return available_move
    
    def capture(self):
        return self.legal_move()
    
    def _logo(self):
        return f"B"
    
    def __str__(self):
        return f"{self.color} Bishop in {self.position}"

class Knight(Piece):
    
    def legal_move(self):
        available_move=[]
        if (self.position[0]+1)<=8 and (self.position[1]+2)<=8:
            available_move.append([self.position[0]+1,self.position[1]+2])
        if (self.position[0]+1)<=8 and (self.position[1]-2)>=1:
            available_move.append([self.position[0]+1,self.position[1]-2])
        if (self.position[0]+2)<=8 and (self.position[1]+1)<=8:
            available_move.append([self.position[0]+2,self.position[1]+1])
        if (self.position[0]+2)<=8 and (self.position[1]-1)>=1:
            available_move.append([self.position[0]+2,self.position[1]-1])
        if (self.position[0]-1)>=1 and (self.position[1]+2)<=8:
            available_move.append([self.position[0]-1,self.position[1]+2])
        if (self.position[0]-1)>=1 and (self.position[1]-3)>=1:
            available_move.append([self.position[0]-1,self.position[1]-2])
        if (self.position[0]-2)>=1 and (self.position[1]+1)<=8:
            available_move.append([self.position[0]-2,self.position[1]+1])
        if (self.position[0]-2)>=1 and (self.position[1]-1)>=1:
            available_move.append([self.position[0]-2,self.position[1]-1])
        return available_move
    
    def capture(self):
        return self.legal_move()
    
    def _logo(self):
        return f"N"
    
    def __str__(self):
        return f"{self.color} Knight in {self.position}"

class Queen(Piece):
    
    def legal_move(self):
        available_move=[]
        for i in range(1,8):
            if (self.position[0]+i)==9 or (self.position[1]+i)==9:
                break
            available_move.append([self.position[0]+i,self.position[1]+i])
        for i in range(1,8):
            if (self.position[0]-i)==0 or (self.position[1]-i)==0:
                break
            available_move.append([self.position[0]-i,self.position[1]-i])
        for i in range(1,8):
            if (self.position[0]+i)==9 or (self.position[1]-i)==0:
                break
            available_move.append([self.position[0]+i,self.position[1]-i])
        for i in range(1,8):
            if (self.position[0]-i)==0 or (self.position[1]+i)==9:
                break
            available_move.append([self.position[0]-i,self.position[1]+i])
        for i in range(1,8):
            if (self.position[0]+i)==9:
                break
            available_move.append([self.position[0]+i,self.position[1]])
        for i in range(1,8):
            if (self.position[0]-i)==0:
                break
            available_move.append([self.position[0]-i,self.position[1]])
        for i in range(1,8):
            if (self.position[1]+i)==9:
                break
            available_move.append([self.position[0],self.position[1]+i])
        for i in range(1,8):
            if (self.position[1]-i)==0:
                break
            available_move.append([self.position[0],self.position[1]-i])
        return available_move
    
    def capture(self):
        return self.legal_move()
    
    def _logo(self):
        return f"Q"
    
    def __str__(self):
        return f"{self.color} Queen in {self.position}"

class King(Piece):
    
    def __init__(self,color,position):
        super().__init__(color,position)
        self.king_move=0
        
    
    def legal_move(self):
        available_move=[]
        x_move_plus=self.position[0]+1
        x_move_minus=self.position[0]-1
        y_move_plus=self.position[1]+1
        y_move_minus=self.position[1]-1
        if (x_move_plus) <=8:
            available_move.append([x_move_plus,self.position[1]])
        if (x_move_minus) >=1:
            available_move.append([x_move_minus,self.position[1]])
        if ( y_move_plus) <=8:
            available_move.append([self.position[0], y_move_plus])
        if (y_move_minus) >=1:
            available_move.append([self.position[0],y_move_minus])
        if (x_move_plus) <=8 and ( y_move_plus) <=8:
            available_move.append([x_move_plus, y_move_plus])
        if (x_move_plus) <=8 and (y_move_minus) >=1:
            available_move.append([x_move_plus,y_move_minus])
        if (x_move_minus) >=1 and ( y_move_plus) <=8:
            available_move.append([x_move_minus, y_move_plus])
        if (x_move_minus) >=1 and (y_move_minus) >=1:
            available_move.append([x_move_minus,y_move_minus])
        return available_move
    
    def capture(self):
        return self.legal_move()
    
    def _logo(self):
        return f"K"
    
    def __str__(self):
        return f"{self.color} King in {self.position}"

class Board:
    """
    I would like to make this a custom dictionary with default initialization so that the ugly self.board.board[position] in object Chess lose one of its board
    
    """
    
    """
    Class to represent the chess board :
    
    board: dict(square:typePiece)
    should be filled with either None or Piece type aka child of Piece object: Pawn, Rook, Knight, Bishop, Queen and King
    
    print_board(): -->None
    Print the board's configuration
    """
    
    def __init__(self):
        file="abcdefgh"
        rank="12345678"
        self.board={(x+y):None for x in file for y in rank}
        for i in range(len(file)):
            self.board[file[i]+'2']=Pawn('White',[i+1,2])
            self.board[file[i]+'7']=Pawn('Black',[i+1,7])
        self.board['a1']=Rook('White',[1,1])
        self.board['h1']=Rook('White',[8,1])
        self.board['b1']=Knight('White',[2,1])
        self.board['g1']=Knight('White',[7,1])
        self.board['c1']=Bishop('White',[3,1])
        self.board['f1']=Bishop('White',[6,1])
        self.board['d1']=Queen('White',[4,1])
        self.board['e1']=King('White',[5,1])
        self.board['a8']=Rook('Black',[1,8])
        self.board['h8']=Rook('Black',[8,8])
        self.board['b8']=Knight('Black',[2,8])
        self.board['g8']=Knight('Black',[7,8])
        self.board['c8']=Bishop('Black',[3,8])
        self.board['f8']=Bishop('Black',[6,8])
        self.board['d8']=Queen('Black',[4,8])
        self.board['e8']=King('Black',[5,8])
        
    def print_board(self):
        file="abcdefgh"
        rank="87654321"
        for y in rank:
            buffer="| "
            for x in file:
                if self.board[x+y]==None:
                    buffer += "  | "
                else:
                    buffer += (self.board[x+y]._logo()+" | ")
            print(buffer)
            
class Chess:
    '''
    
    Need future implementation:
    1. Castling, as in detection of legality of castling
    2. Proper check & checkmate implementation i.e detecting the only move to escape check, and declaring checkmate 
    if no legal move detected 
    3. simplifying the ungodly amount of if else
    
    '''
    """
    This should handle input parsing, which is determining whether it's a move, capture, castle, promotion, or en passant
    Also determine the state of the board i.e check, checkmate, stalemate.
    
    move(moves):
    this is the main parser, will parse the type of move the piece will play, moves should be in modern chess notation, 
    which should infers about which pieces should be moved. 
    
    In case of normal move, it also determine whether the piece is blocked (and basically other type of moves too)
    
    promotion(square):
    square is the last 2 character in string, which should be parsed by Chess.move. Should only be accessed by Chess.move
    
    en_passant(square):
    detect if en_passant is possible, then call the Pawn.capture() if it does. Should only be accessed by Chess.move
    
    capture(square):
    call the Piece.capture() if possible. Should only be accessed by Chess.move
    
    castle:
    play castling if possible. Should only be accessed by Chess.move

    """
    
    def __init__(self):
        self.side="White"
        self.board=Board()
    
    def check_empty_square(self,position):
        if ("+" in position) or ("#" in position):
            position=position[:len(position)-1] #this removes the check/mate mark
        if len(position)>2 and ('=' not in position):
            position=position[len(position)-2:] #example, Bd5, d5 is the square we want to check whether it's empty
        elif len(position)>2 and ('=' in position):
            position=position[:2]
            #there's 2 type of promotion annotation, b8=Q and bxc8=Q, the x implies the square is not empty.
        
        if self.board.board[position] !=None:
            return False
        return True
    
    def capture_legality(self,position):
        if ("+" in position) or ("#" in position):
            position=position[:len(position)-1] #this removes the check/mate mark
        if len(position)>2 and ('=' not in position):
            position=position[len(position)-2:] #example, Bd5, d5 is the square we want to check whether it's empty
        elif len(position)>2 and ('=' in position):
            position=position[:2]
        
        if self.board.board[position].color==self.side:
            return False
        return True
    
    def promotion(self, pieces, position, poslist):
        # poslist should be converted from position input i.e e8 is converted into [5,8] in method self.move
        #hopefully work
        if pieces=="Q":
            self.board.board[position]=Queen(self.side,poslist)
        elif pieces=="R":
            self.board.board[position]=Rook(self.side,poslist)
        elif pieces=="B":
            self.board.board[position]=Bishop(self.side,poslist)
        elif pieces=="N":
            self.board.board[position]=Knight(self.side,poslist)
        return
    
    def castle(self,moves):
        if self.side=="White":
            if moves=="0-0" or moves=="0-0+":
                self.board.board["g1"]=King(self.side,[7,1])
                self.board.board["f1"]=Rook(self.side,[6,1])
                self.board.board["e1"]=None
                self.board.board["h1"]=None
            else:
                self.board.board["c1"]=King(self.side,[3,1])
                self.board.board["d1"]=Rook(self.side,[4,1])
                self.board.board["e1"]=None
                self.board.board["a1"]=None
        else:
            if moves=="0-0" or moves=="0-0+":
                self.board.board["g8"]=King(self.side,[7,8])
                self.board.board["f8"]=Rook(self.side,[6,8])
                self.board.board["e8"]=None
                self.board.board["h8"]=None
            else:
                self.board.board["c8"]=King(self.side,[3,8])
                self.board.board["d8"]=Rook(self.side,[4,8])
                self.board.board["e8"]=None
                self.board.board["a8"]=None    
        return
    
    def capture(self,pos_start,pos_end):
        self.board.board[pos_end]=self.board.board[pos_start]
        self.board.board[pos_start]=None
        return

    def move(self,moves):
        if 'x' not in moves:
                if !(self.check_empty_square(moves)):
                    print("illegal Move")
                    return
        elif 'x' in moves:
            if self.check_empty_square(moves) or self.capture_legality(moves):
                print("illegal Move")
                return
        if "=" in moves:
            self.promotion("Q", 'e8', [5,8])
        if self.side=="White":
            self.side="Black"
        else:
            self.side="White"
        return

if __name__=="__main__":
    Board=Chess()
    print(Board.side)
    Board.move("a4")
    print(Board.side)
    Board.move("a6")
    print(Board.side)
    print(Board.board.board['e8'])
    
    
    
