"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
# empty list for salespeople and melons_sold
# IMPROVEMENT: can use a empty dictionary instead

f = open('sales-report.txt')
# sets a variable, f, that opens the text file, sales-report.txt

for line in f:
# iterates through each line in the sales-report.txt
    line = line.rstrip()
    # removes any trailing characters in each line
    entries = line.split('|')
    # split strings in line by '|', put all values in a list called entries

    salesperson = entries[0]
    # set salesperson to the value of entries at index 0
    melons = int(entries[2])
    # set melons to an integer conversion of entries at index 2
    # IMPROVEMENT: will not need lines 19-22 if a dictionary is used
    
    if salesperson in salespeople:
    # if salesperson is in the list salespeople
        position = salespeople.index(salesperson)
        # set position as the index of where salesperson is in salespeople

        melons_sold[position] += melons
        # add melons to existing value in melons_sold list
    else:
    # if salesperson is not in salespeople
        salespeople.append(salesperson)
        # add salesperson to the end of salespeople
        melons_sold.append(melons)
        # add melons sold to the end of salespeople


for i in range(len(salespeople)):
# iterate through from index zero to the length of salespeople
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    # prints how many melons each salesperson in salespeople sold
