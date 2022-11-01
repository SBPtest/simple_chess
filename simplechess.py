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
    
    def __str__(self):
        return f"{self.color} King in {self.position}"

def board():
    file="abcdefgh"
    rank="12345678"
    playboard={(x+y):0 for x in file for y in rank}
    for i in range(len(file)):
        playboard[file[i]+'2']=Pawn('White',[i+1,2])
        playboard[file[i]+'7']=Pawn('Black',[i+1,7])
    playboard['a1']=Rook('White',[1,1])
    playboard['h1']=Rook('White',[8.1])
    playboard['b1']=Knight('White',[2,1])
    playboard['g1']=Knight('White',[7,1])
    playboard['c1']=Bishop('White',[3,1])
    playboard['f1']=Bishop('White',[6,1])
    playboard['d1']=Queen('White',[4,1])
    playboard['e1']=King('White',[5,1])
    playboard['a8']=Rook('Black',[1,8])
    playboard['h8']=Rook('Black',[8,8])
    playboard['b8']=Knight('Black',[2,8])
    playboard['g8']=Knight('Black',[7,8])
    playboard['c8']=Bishop('Black',[3,8])
    playboard['f8']=Bishop('Black',[6,8])
    playboard['d8']=Queen('Black',[4,8])
    playboard['e8']=King('Black',[5,8])
    return playboard
if __name__=="__main__":
    Board=board()
    print (Board['h1'].legal_move())
