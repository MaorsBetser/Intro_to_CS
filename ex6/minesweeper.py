

from random import randint

class MSSquare:
    '''
        Mine Sweeper Square class
        3 main attributes 
        has_mine -> True if mine has a mine inside
        hidden -> if player have yet to pick that square, 
        neighbour mines -> how many mines are nearby in a sqaure of 3x3 around the square
        for each attribute i've made setters and getters, checking for the type of data inserted.
        each attribue in __init__ is specified with type and default value.
    '''
    def __init__(self,has_mine:bool=False, hidden:bool=True, neighbour_mines:int=0):
        self.__has_mine = has_mine
        self.__hidden = hidden
        self.__neighbour_mines = neighbour_mines

    @property
    def has_mine(self):
        return self.__has_mine

    @has_mine.setter
    def has_mine(self,value):
        if not isinstance(value,bool):
            raise ValueError("has_mine expected type bool check type inserted...")
        self.__has_mine = value

    def show_mine(self,state):
        '''
            function used inorder to show all the mines at End game getting called by display game
            state is the current game state True if game is ongoing and false otherwise
        '''
        if self.__has_mine == True and state == False:
            return 'X'
        else:
            return ' '

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self,value):
        if not isinstance(value,bool):
            raise ValueError("hidden expected type bool check type inserted...")
        self.__hidden = value
    
    @property
    def neighbour_mines(self):
        return self.__neighbour_mines

    @neighbour_mines.setter
    def neighbour_mines(self,value):
        if not isinstance(value,int):
            raise ValueError("neighbour_mines expected type int.. check type inserted")
        self.__neighbour_mines = value

    def __str__(self):
        if self.has_mine == True:
            return ' '
        if self.hidden == True:
            return ' '
        return f'{self.__neighbour_mines}'


def game_init(ts):
    '''
        Initialize the game, creating the board by the size specified, with nested list comprehension, calling MSSquare() with it's default values on each cell
        "Activating" mines means placing mines on the board by randomly picking a coordinate and placing it making has_mine -> True and turning hidden off
        if the coordinate was already placed it just skips until it have place all the mines on the board by comparing the length of the coordinates list with
        the mine count then returning the game table
    '''
    placed = []
    mine_count = randint(ts,2*ts)
    table = [[MSSquare() for i in range(ts)] for j in range(ts)]
    activated = 0
    while activated != mine_count:
        x = randint(0,(ts-1))
        y = randint(0,(ts-1))
        if (x,y) not in placed:
            table[x][y].has_mine = True
            table[x][y].hidden = False
            activated += 1
            placed.append((x,y))
    return table


def check_mines(gt,x,y,ts):
    '''
        input game table (x,y) pos and table size
        then checks for the range it can run
        by choosing the max between x-1 or 0 meaning its in the left side of the grid
        and the chossing x+1 or ts -1 if its in the right side of the grid
        does the same for y values
        then counts the number of mines in the given grid.

    '''
    n_mines = 0
    for i in range(max((x-1),0),min(((x+1)),ts-1)+1):
        for j in range(max((y-1),0),min(((y+1),ts-1))+1):
            if gt[i][j].has_mine == True:
                n_mines +=1
    return n_mines


def check_neighbours(gt,x,y,ts):
    '''
        off sets is the places for checking neighbours meaning up down left and right
        for each pair in offset 
        nex x pos = current x pos + x in offset
        new y pos = current y pos + y in offset
        checking if offset is in the grid boundries
        if the position nx ny has mine means it should not search there
        if it is hidden then reveal it and check mines at the new location
        and then only if the mines around it is 0 it calls itself with new location
    '''
    off_set = [(-1,0),(0,-1),(1,0),(0,1)]
    for pair in off_set:
        nx = x + pair[0]
        ny = y + pair[1]
        if (nx < 0 or nx > (ts-1)) or (ny < 0 or ny > (ts-1)):
            print(nx,ny)
            continue
        elif gt[nx][ny].has_mine:
            continue
        elif gt[nx][ny].hidden:
            gt[nx][ny].hidden = False
            gt[nx][ny].neighbour_mines = check_mines(gt,nx,ny,ts)
            if gt[nx][ny].neighbour_mines == 0:
                check_neighbours(gt,nx,ny,ts)


def display_game(gt,ts,state):
    '''
    This was a hasssle... trying to print it correctly 
    most of the code is just formating for lines to be in the correct sizing
    if statement inside means to print the str representation when the cell doesnt have mine, and only show mines when the game state is false
    meaning the game has ended and its time to show all squares
    '''
    print('{:2}'.format('')+'{:4}'.format('+---')*ts,end="+\n")
    for i in range(ts):
        if i != 0:
            print('|')
            print('{:2}'.format('')+'{:4}'.format('+---')*ts,end="+\n")
        for j in range(ts):
            if j != 0:
                print('{:2}{:2}'.format('|' ,gt[i][j].__str__() if gt[i][j].has_mine == False else gt[i][j].show_mine(state)) ,end='')
            else:
                print('{:2}'.format(i+1), end='')
                print('{:2}{:2}'.format('|' , gt[i][j].__str__()),end='')
    print('|')
    print('{:2}'.format("")+'{:4}'.format('+---')*ts,end="+\n")
    for i in range(ts):
        if i == 0:
            print('{:2}'.format('')+'{:3}'.format(i+1),end='')
        else:
            print('{:4}'.format(i+1),end='')
    print()


def get_size():
    '''
        standard getting the input from user, while checking for validity of given input
        valid input being between 4 - 9 and can be cast to int
    '''
    print('type "exit" to stop program')
    while True:
        try:
            _input  = input("Please insert size for game table between 4 - 9: ")
            if _input == 'exit':
                break
            _input = int(_input)
            if _input >= 4 and _input <= 9:
                return _input
            print('Please insert a number between 4 - 9')
            continue
        except:
            print('incorrect value inserted please insert a number')
    quit()


def game_loop(gt,ts):
    '''
        Main game loop, prompt user for input and then splits the input to x y coordinates 
        the format is first y and then x because when indexing in a nested list first index to rows and then cols
        so first y and then x.
        after getting input if the given location on the grid has a mine the function calls display_game and shows hidden mines
        then returns false to break the game loop
        otherwise meaning we picked a square without a mine inside
        reveals the square checks for mines and sets it in the given square then if it has 0 mines nearby it checks the neighbour mines and so on
        until hitten a square with atleast one mine nearby.
        every turn the game_loop function calls check_win that should return false if the game is ongoing otherwise returns true if game is won
    '''
    print('When entering coordinates please do as follows first y and then x seperated by space "y x"')
    ui = input('Please enter your desired coordinates: ')
    loc = ui.split()
    x = int(loc[0])
    y = int(loc[1])
    x -= 1
    y -= 1
    if gt[x][y].has_mine:
        display_game(gt,ts,False)
        print(f'You have hit a mine at ({x+1},{y+1})')
        return False
    else:
        gt[x][y].hidden = False
        gt[x][y].neighbour_mines = check_mines(gt,x,y,ts)
        if gt[x][y].neighbour_mines == 0:
            check_neighbours(gt,x,y,ts)
        display_game(gt,ts,True)

        if check_win(gt,ts):
            return True
        else:
            return False


def check_win(gt,ts):
    '''
        checks if there is any squares left on the grid that are mines or are still hidden meaning the game is ongoing 
        otherwise the game have ended and returns false
    '''
    for i in range(ts):
        for j in range(ts):
            if gt[i][j].has_mine == True:
                continue
            if gt[i][j].hidden:
                return True
    print('You HAVE WON!')
    return False

def main():
    '''
        Calls all the functions in order to run the game properly
        and sets the game_state to true in the start
    '''
    game_state = True
    t_size = get_size()
    table = game_init(t_size)
    display_game(table,t_size,True)
    while game_state:
        game_state = game_loop(table,t_size)


if __name__ == '__main__':
    main()

