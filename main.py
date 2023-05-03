import board

a = [board.board() for i in range(2)]
a[0].set_small_aero(6,6,0)
a[0].set_big_aero(13,13,0)
a[0].display()
# for i in board.board.list_of_board:
#     i.display()