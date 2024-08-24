# import os
# def clear_terminal():
#     _ = os.system('clear')
# clear_terminal()
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(1)
# timmy.bk(.99)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# #figure out how to import packacke into vscode


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("PoKeMoN Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)