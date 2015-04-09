def update_melon_tallies(file_name):    #"orders-by-type.txt"
    open_file = open(file_name)
    for line in open_file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    open_file.close()


def generate_sales_report(file_name):
    total_revenue = 0
    update_melon_tallies(file_name)
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)


def generate_internet_phonesales_report(file_name):
    file_name = open(file_name)
    internet_sales = 0
    salespeople_sales = 0
    for line in file_name:
        data = line.split("|")
        if data[1] == "0":
            internet_sales += float(data[3])
        else:
            salespeople_sales += float(data[3])

    print "Salespeople generated %0.2f in revenue." % salespeople_sales
    print "Internet sales generated %0.2f in revenue." % internet_sales

    if salespeople_sales > internet_sales:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


melon_tallies = {"Musk":0,
                 "Hybrid":0,
                 "Watermelon":0,
                 "Winter": 0}

melon_prices = {"Musk": 1.15,
                "Hybrid": 1.30,
                "Watermelon": 1.75, 
                "Winter": 4.00 }

section_separator = 80


print "*" * section_separator

generate_sales_report("orders-by-type.txt")

print "*" * section_separator

generate_internet_phonesales_report("orders-with-sales.txt")
