# This line not needed?  SALESPERSON_INDEX = 0
# This line not needed? INTERNET_INDEX = 1
section_separator = 80

print "*" * section_separator

melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

def gen_orders_by_type_report(file_name):    #"orders-by-type.txt"
    open_file = open(file_name)


    for line in open_file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    f.close()


melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
total_revenue = 0
for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

print "*" * section_separator

f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print "Salespeople generated %0.2f in revenue." % sales[1]
print "Internet sales generated %0.2f in revenue." % sales[0]
if sales[1] > sales[0]:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"
print "*" * section_separator

gen_orders_by_type_report("orders-by-type.txt")
