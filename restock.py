def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
 total_units_sold = total_units_sold + number_sold

    inventory_records = {
        "day" : current_day,
        "sold units" : total_units_sold,
        "restocked units" : restock_needed,
        "availible units" : availible_items 
    }

    if current_day % 7 != 0:
        number_sold = random.randint(0,200)
        available_items = available_items - number_sold
    elif current_day % 7 == 0:
        restock_needed = total_units_sold
        available_items = restock_needed + available_items
    else:
        print("Invalid day")
    
    if availible_items > 2000:
        availible_items = 2000
        
    return available_items
