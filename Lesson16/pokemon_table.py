import prettytable
table = prettytable.PrettyTable()

table.field_names = ["Name", "Type"]
table.add_row(["Mudkip", "Water"])
table.add_row(["Emolge", "Electric"])
table.add_row(["Gengar", "Ghost"])
table.align = "l"

print(table)
