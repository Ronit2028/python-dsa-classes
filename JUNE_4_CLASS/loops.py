list = [1, 2, 3,4,5,6,7,8,9,10]

for number in list:
    print(number)

for number in range(1, 11):
    print(number)

order_queue = {"table_1": "aaloo paratha", "table_2": "gobi paratha", "table_3": "paneer paratha"}
for table, order in order_queue.items():   
    print("Table: " + table + ", Order: " + order)


#.item() whenever we use it on a dictonary it will return a list of tuples where each tuple is a key value pair from the dictionary.
print(order_queue.items())



quantity_aaloo_paratha = 10
while quantity_aaloo_paratha > 0:
    quantity_aaloo_paratha -= 1

    if quantity_aaloo_paratha == 5:
        print("Half of the aaloo parathas are prepared. Time to start preparing gobi parathas.")
        continue
    print("Preparing aaloo paratha. Remaining quantity: " + str(quantity_aaloo_paratha))
    if quantity_aaloo_paratha == 1:
        print("Only one aaloo paratha left. Need to prepare more.")
        break



rows = [1,2,3,4,5]
for row in rows:
    # print("Row: " + str(row))
    for seat in range(1, 6):
        print("  Seat: " + str(seat), "row: " + str(row))
