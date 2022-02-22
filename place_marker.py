def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board, "X", 8)
display_board(test_board)