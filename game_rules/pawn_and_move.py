from random import randint


def yellow_case_move(self, x_start, y_start, x_end, y_end):#deplacement fou/bishop0
        if abs(x_end - x_start) != abs(y_end - y_start):
            return False

        step_x = 1 if x_end > x_start else -1
        step_y = 1 if y_end > y_start else -1
        x, y = x_start + step_x, y_start + step_y

        while x != x_end and y != y_end:
            if self.get_board()[x][y] != 0:
                return False
            x += step_x
            y += step_y

        if self.get_board()[x_end][y_end] !=0:
            return False

        return True

def blue_case_move(self, x_start, y_start, x_end, y_end):#deplacement roi
        if abs(x_end - x_start) > 1 or abs(y_end - y_start) > 1: #abs = valeur absolue
            return False

        if self.get_board()[x_end][y_end] != 0:
            return False

        return True
    
def green_case_move(self, x_start, y_start, x_end, y_end):#deplacement cavalier
    
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        dx = x_end - x_start
        dy = y_end - y_start

        if (dx, dy) in knight_moves:

            if self.get_board()[x_end][y_end] == 0:
                return True
        return False


def red_case_move(self, x_start, y_start, x_end, y_end):  # Déplacement d'une tour 
    # check si mouvement est ok ou non
    if x_start != x_end and y_start != y_end:
        return False
    
    # Déplacement horizontal
    if x_start == x_end:
        step = 1 if y_end > y_start else -1
        for y in range(y_start + step, y_end, step):
            if self.get_board()[x_start][y] != 0:  # case libre ou non
                return False
            if self.get_board()[x_start][y] == 4:  # case rouge ou non
                # Si case rouge on s'arrete 
                if y == y_end:
                    return True
                return False  # Si la case rouge est avant la destination ==arret



#same que pour horizontale
    # Déplacement vertical
    if y_start == y_end:
        step = 1 if x_end > x_start else -1
        for x in range(x_start + step, x_end, step):
            if self.get_board()[x][y_start] != 0:  
                return False
            if self.get_board()[x][y_start] == 4: 
                
                if x == x_end:
                    return True
                return False  
    
    # check si la case d'arrivée est vide ou rouge
    if self.get_board()[x_end][y_end] != 0 and self.get_board()[x_end][y_end] != 4:
        return False

    return True
