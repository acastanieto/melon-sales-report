def order_tally(orders_by_type_file):
    """Return tally of melons by type."""

    tallies = {"Musk": 0,
               "Hybrid": 0,
               "Watermelon": 0,
               "Winter": 0}

    orders = open(orders_by_type_file)

    for order in orders:
        # Each line has "id|melontype|count"
        # We want to split this and get the melontype and count.
        data = order.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        tallies[melon_type] = tallies[melon_type] + melon_count

    orders.close()

    return tallies


def total_revenue(tallies):
    """Return total revenue in sales."""

    MELON_PRICES = {"Musk": 1.15,
                    "Hybrid": 1.30,
                    "Watermelon": 1.75,
                    "Winter": 4.00}

    revenue = 0

    print "TOTAL REVENUE"

    for melon_type in tallies:
        price = MELON_PRICES[melon_type]
        revenue = price * tallies[melon_type]
        revenue = revenue + revenue

        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (
            tallies[melon_type],
            melon_type,
            price,
            revenue
        )

    return revenue


def sales_comparison(orders_with_sales_file):
    """Compare online and salesperson-generated sales."""

    orders = open(orders_with_sales_file)
    online_revenue = 0
    salespeople_revenue = 0

    for order in orders:
        # The third column of each line has either the saleperson
        # name or ONLINE. We'll find that and then use it to decide
        # who gets credit for this sale.
        data = order.split("|")

        if data[2] == "ONLINE":
            online_revenue = online_revenue + float(data[3])

        else:
            salespeople_revenue = salespeople_revenue + float(data[3])

    print "SALES DATA"
    print "Salespeople generated %0.2f in revenue." % salespeople_revenue
    print "Internet sales generated %0.2f in revenue." % online_revenue

    if salespeople_revenue > online_revenue:
        print "Guess there's some value to those salespeople after all."

    else:
        print "Time to fire the sales team! Online sales rule all!"

    orders.close()


# Get the tallies by melon type
melon_tallies = order_tally("orders-by-type.txt")

# Print total revenue report
total_revenue(melon_tallies)

print

# Print online-v-salesperson report
sales_comparison("orders-with-sales.txt")