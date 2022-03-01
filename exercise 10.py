def calc_gst(net_price):
    result = net_price * 1.15
    return result


price = int(input("what is the item price?: "))
print(f"The price with GST is {calc_gst(price)}")
