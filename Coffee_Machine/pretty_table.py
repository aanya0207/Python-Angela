from prettytable import PrettyTable
table = PrettyTable()

# add column by column
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],align="l")
table.add_column("Type",["Electric","Water","Fire"],align="l")

table.border = True

print(table)