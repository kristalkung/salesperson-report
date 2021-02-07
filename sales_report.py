"""Generate sales report showing total melons each salesperson sold."""


salespeople_melons = {}
# IMPROVEMENT: used an empty dictionary

f = open('sales-report.txt')
# sets a variable, f, that opens the text file, sales-report.txt

for line in f:
# iterates through each line in the sales-report.txt
    line = line.rstrip()
    # removes any trailing characters in each line
    salesperson, total, melons_sold = line.split('|')
    # split strings in line by '|', put all values in a list called entries

    if salesperson in salespeople_melons:
    # if salesperson is in the dictionary salespeople_melons
        salespeople_melons[salesperson] += int(melons_sold)
        # add # melons sold to existing value

    else:
    # if salesperson is not in salespeople
        salespeople_melons[salesperson] = int(melons_sold)

for salesperson in salespeople_melons:
# iterate through all salesperson in salespeople_melon
    print(f'{salesperson} sold {salespeople_melons[salesperson]} melons')
    # prints how many melons each salesperson in salespeople sold
