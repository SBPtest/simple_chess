class Piece:
    
    def __init__(self,color,position):
        self.color=color
        self.position=position
        
    def _logo(self):
        return f"."
    
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
    
    def _logo(self):
        return f"Q"
    
    def __str__(self):
        return f"{self.color} Queen in {self.position}"

class King(Piece):
    
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
    
    def _logo(self):
        return f"K"
    
    def __str__(self):
        return f"{self.color} King in {self.position}"

class Board:
    '''
    "I would like to make this a custom dictionary with default initialization so that the ugly Chess.board.board['e4'] lose one of its board"
    '''
    file="abcdefgh"
    rank="12345678"
    
    def __init__(self):
        file="abcdefgh"
        rank="12345678"
        self.board={(x+y):Piece(None,None) for x in file for y in rank}
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
            print("|",self.board["a"+y]._logo(),"|",self.board["b"+y]._logo(),"|",self.board["c"+y]._logo(),"|",self.board["d"+y]._logo(),"|",self.board["e"+y]._logo(),"|",self.board["f"+y]._logo(),"|",self.board["g"+y]._logo(),"|",self.board["h"+y]._logo(),"|")
  
class Chess:
    '''
    
    Need future implementation:
    1. Castling, as in detection of legality of castling
    2. Proper check & checkmate implementation i.e detecting the only move to escape check, and declaring checkmate 
    if no legal move detected 
    3. simplifying the ungodly amount of if else
    
    '''
    
    def __init__(self):
        self.side="White"
        self.board=Board()
    
    def move(self,moves):
        if len(moves)==2:
            if self.side=="White":
                pass
            else:
                pass
            pass
        elif len(moves)==3:
            if self.side=="White":
                pass
            else:
                pass
            pass
        elif len(moves)==4:
            if self.side=="White":
                pass
            else:
                pass
            pass
        elif len(moves)==5:
            if self.side=="White":
                pass
            else:
                pass
            pass
        if self.side=="White":
            self.side="Black"
        else:
            self.side=="White"

if __name__=="__main__":
    Board=Board()
    Board.print_board()
 
