# For rook
def rook_valid_moves(current_path, position_of_other_pieces):
    # vertical_all_possible_moves = [current_path[0] + str(i) for i in range(1, 9)]
    vertical_all_possible_moves = []
    horizontal_all_possible_moves = []
    for i in range(1,9):
        new_path = current_path[0] + str(i)
        if new_path not in position_of_other_pieces:
            vertical_all_possible_moves.append(new_path)
        else:
            if new_path != current_path:
                # vertical_all_possible_moves = [new_path,]
                vertical_all_possible_moves.append(new_path)
                break
    # print(current_path, vertical_all_possible_moves)

    for i in range(65,73):
        new_path = chr(i) + current_path[1]
        if new_path not in position_of_other_pieces:
            horizontal_all_possible_moves.append(new_path)
        else:
            if new_path != current_path:
                # horizontal_all_possible_moves = [new_path,]
                horizontal_all_possible_moves.append(new_path)
                break
    # horizontal_all_possible_moves = [chr(i) + current_path[1] for i in range(65, 73)]

    # Removing current path
    try:
        horizontal_all_possible_moves.remove(current_path)
    except:
        pass
    try:
        vertical_all_possible_moves.remove(current_path)
    except:
        pass
    # print("all possible verical moves", vertical_all_possible_moves)
    # print("all possible horizontal moves", horizontal_all_possible_moves)
    return vertical_all_possible_moves,horizontal_all_possible_moves


def bishop_valid_moves(current_path, all_peices_position):
    # Put separate variables for each direction?
    upward_right = []
    downward_right = []
    horizontal_forward_value = int(current_path[1])
    horizontal_downward_value = int(current_path[1])
    stop_forward_value = False
    stop_downward_value = False

    for i in range(ord(current_path[0]), 73):
        # Vertical Forward( Upward right direction)
        if not stop_forward_value:
            if horizontal_forward_value < 9:
                if chr(i) + str(horizontal_forward_value) in all_peices_position:
                    stop_forward_value = True
                    # upward_right = [chr(i) + str(horizontal_forward_value),]
                    upward_right.append(chr(i) + str(horizontal_forward_value))
                else:
                    upward_right.append(chr(i) + str(horizontal_forward_value))

        # Vertical Forward( Downward right direction)
        if not stop_downward_value:
            if horizontal_downward_value > 0:
                if chr(i) + str(horizontal_forward_value) in all_peices_position:
                    stop_downward_value = True
                    # downward_right = [chr(i) + str(horizontal_downward_value)]
                    downward_right.append(chr(i) + str(horizontal_downward_value))
                else:
                    downward_right.append(chr(i) + str(horizontal_downward_value))

        horizontal_forward_value += 1
        horizontal_downward_value -= 1

    try:
        downward_right.remove(current_path)
    except:
        pass
    try:
        upward_right.remove(current_path)
    except:
        pass
    ver_forward_value = int(current_path[1])
    ver_downward_value = int(current_path[1])
    upward_left = []
    downward_left = []
    stop_forward_value = False
    stop_downward_value = False

    for j in range(ord(current_path[0]), 64, -1):
        # Upward left direction
        if not stop_forward_value:
            if ver_forward_value < 9:
                if chr(j) + str(ver_forward_value) in all_peices_position:
                    # upward_left = [chr(j) + str(ver_forward_value),]
                    upward_left.append(chr(j) + str(ver_forward_value))
                    stop_forward_value = True
                else:
                    upward_left.append(chr(j) + str(ver_forward_value))
        # Downward left direction
        if not stop_downward_value:
            if ver_downward_value > 0:
                if chr(j) + str(ver_downward_value) in all_peices_position:
                    # downward_left = [chr(j) + str(ver_downward_value)]
                    downward_left.append(chr(j) + str(ver_downward_value))
                    stop_downward_value = True
                else:
                    downward_left.append(chr(j) + str(ver_downward_value))


        ver_forward_value += 1
        ver_downward_value -= 1

    #
    try:
        downward_left.remove(current_path)
    except:
        pass
    try:
        upward_left.remove(current_path)
    except:
        pass
    # print("This--",upward_right, downward_right, upward_left, downward_left)
    
    return upward_right, downward_right, upward_left, downward_left


def knight_valid_moves(current_path):
    # (A, 2)
    knight_moves = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (-1, -2),
        (-1, 2),
        (1, -2),
    ]
    possible_path = []
    for i in knight_moves:
        new_path = (ord(current_path[0]) + i[0], int(current_path[1]) + i[1])
        if 0 < new_path[1] <= 8 and 64 < new_path[0] <= 72:
            possible_path.append(chr(new_path[0]) + str(new_path[1]))
    return possible_path


def queen_valid_moves(current_path, all_peices_position):
    diagonal_moves = bishop_valid_moves(current_path, all_peices_position)
    straight_line_moves = rook_valid_moves(current_path,all_peices_position)
    # print(diagonal_moves, straight_line_moves)
    possible_moves = set(diagonal_moves[0]+diagonal_moves[1]+diagonal_moves[2]+diagonal_moves[3]+straight_line_moves[0]+straight_line_moves[1])
    
    return list(possible_moves)

# Get all moves
# separate function which will determine
def valid_moves(moving_peice, all_peices_position):
    queen_position = all_peices_position.get('positions').get('Queen')
    bishop_position = all_peices_position.get('positions').get('Bishop')
    rook_position = all_peices_position.get('positions').get('Rook')
    knight_position = all_peices_position.get('positions').get('Knight')
    
    playable_pieces = []

    rook_next_moves = rook_valid_moves(rook_position, [queen_position,knight_position,bishop_position])
    rook_next_moves = [item for sublist in rook_next_moves for item in sublist]
    bishop_next_moves = bishop_valid_moves(bishop_position, [queen_position,rook_position, knight_position])
    bishop_next_moves = [item for sublist in bishop_next_moves for item in sublist]
    # print("Bishop next", bishop_next_moves)
    knight_next_moves = knight_valid_moves(knight_position)
    queen_next_moves = queen_valid_moves(queen_position,[bishop_position,rook_position, knight_position])
    if moving_peice == 'queen':
        playable_pieces = queen_next_moves
    if moving_peice == 'bishop':
        playable_pieces = bishop_next_moves
    if moving_peice == 'knight':
        playable_pieces = knight_next_moves
    if moving_peice == 'rook':
        playable_pieces = rook_next_moves

    # print(queen_next_moves)
    for i in rook_next_moves:
        if i in playable_pieces and moving_peice!='rook':
            playable_pieces.remove(i)
    for i in bishop_next_moves:
        if i in playable_pieces and moving_peice!='bishop':
            playable_pieces.remove(i)
    for i in knight_next_moves:
        if i in playable_pieces and moving_peice!='knight':
            playable_pieces.remove(i)
    for i in queen_next_moves:
        if i in playable_pieces and moving_peice!='queen':
            playable_pieces.remove(i)
    return playable_pieces

# a = {
#     "positions": {
#         "Queen": "H1",
#         "Bishop": "B7", 
#         "Rook": "H8",  
#         "Knight": "F2",
#     }
# }
# print(valid_moves('rook',a))