def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def create_board():
    sudoku = ""

    for i in range(1, 10):
        msg = f'Ingresa la {i} linea de numeros: '
        filas = input(msg)

        if sudoku != "":
            sudoku += "," + filas
        else:
            sudoku += filas

    board = sudoku.split(",")

    for i, num in enumerate(board):
        board[i] = list(map(int, num))

    return board


def menu():
    print("*" * 48)
    print("Para ver la solución de un tablero de sudoku primero debes cargar sus valores, para hacerlo considera lo siguiente:\n")
    print("Ingresa los numeros de la linea que el programa te indique, teniendo en consideracion que los espacios en blanco del tablero se repesentan con 0 aca.")
    print("\n")

    option = input("Quieres cargar una solución? (y/n): ")

    while True:
        if option == "y" or option == "n":
            break
        option = input("Quieres cargar una solución? (y/n): ")

    return option


def run_program(option):
    if option == "y":
        board = create_board()
        print_board(board)
        print("_________________________")
        solve(board)
        print_board(board)
        exit()
    elif option == "n":
        exit()


if __name__ == "__main__":
    while True:
        option = menu()
        if option == 9:
            break
        else:
            run_program(option)
