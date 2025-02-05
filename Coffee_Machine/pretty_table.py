from prettytable import PrettyTable
coffee_table = PrettyTable()

# add column by column
coffee_table.add_column("Items",["Espresso","Latte","Cappuccino"],align="l")
coffee_table.add_column("Cost",["1.5","2.5","3.5"],align="r")
coffee_table.border = True
table_name = "Menu"
print(table_name)
print(coffee_table)

# conversion table 
# add row by row
from prettytable import PrettyTable

conversion = PrettyTable()
conversion.field_names = ["Name", "Multiplier"]
conversion.add_row(["Quarter", 0.25])
conversion.add_row(["Dimes", 0.10])
conversion.add_row(["Nickles", 0.05])
conversion.add_row(["Pennies", 0.01])
conversion.align = "l"
# Name of the table
table_name = "Currency Conversion Table"
print(table_name)
print(conversion)
