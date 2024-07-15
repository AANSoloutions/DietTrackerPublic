import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd
from tkinter import ttk, StringVar
from datetime import datetime

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

breakfast_menu_file_path = "breakfast_items.csv"
lunch_menu_file_path = "lunch_items.csv"
dinner_menu_file_path = "dinner_items.csv"
diary_file_path = "diary_items.csv"

window = tk.Tk()
window.geometry('1200x750')
window.title('diet tracker')
window.rowconfigure(1, weight=1, minsize=50)
    
breakfast_var = StringVar()
lunch_var = StringVar()
dinner_var = StringVar()

###################################################################################################################################################################################
########################################################################        populate array from file       ###########################################################################
###################################################################################################################################################################################

breakfast_items = []
lunch_items = []
dinner_items = []

total_items = []

diary_diet = []

selected_breakfast_items = []
selected_lunch_items = []
selected_dinner_items = []


def populate_array():
    global breakfast_items
    global lunch_items
    global dinner_items
    global diary_diet
    
    breakfast_items = pd.read_csv(breakfast_menu_file_path).values.tolist()
    lunch_items = pd.read_csv(lunch_menu_file_path).values.tolist()
    dinner_items = pd.read_csv(dinner_menu_file_path).values.tolist()
    diary_diet = pd.read_csv(diary_file_path).values.tolist()
                            
populate_array()

###################################################################################################################################################################################
########################################################################        Add Item Window        ###########################################################################
###################################################################################################################################################################################

def store_food_to_file(food_name, protein_val, calories_val, total_fat_val, carbohydrate_val, sodium_val):
    #Stores the entry item and stores it into the 2D array

    if breakfast_var.get():
        breakfast_items.append([food_name.get(), protein_val.get(), calories_val.get(), total_fat_val.get(), carbohydrate_val.get(), sodium_val.get()])

        with open(breakfast_menu_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            #Stores 2D array into file
            writer.writerows(breakfast_items)
            print("2D array saved to file:", breakfast_menu_file_path)
        
    if lunch_var.get():
        lunch_items.append([food_name.get(), protein_val.get(), calories_val.get(), total_fat_val.get(), carbohydrate_val.get(), sodium_val.get()])

        with open(lunch_menu_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            #Stores 2D array into file
            writer.writerows(lunch_items)
            print("2D array saved to file:", lunch_menu_file_path)


    if dinner_var.get():
        dinner_items.append([food_name.get(), protein_val.get(), calories_val.get(), total_fat_val.get(), carbohydrate_val.get(), sodium_val.get()])

        with open(dinner_menu_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            #Stores 2D array into file
            writer.writerows(dinner_items)
            print("2D array saved to file:", dinner_menu_file_path)
        
def update_button_state():
    if any([breakfast_var.get(), lunch_var.get(), dinner_var.get()]):
        add_nutrition_button.config(state="normal")
    else:
        add_nutrition_button.config(state="disabled")

# Create the figure and axes
fig = Figure(figsize=(6, 6))
ax = fig.add_subplot(111)
fig.set_facecolor('darkgrey') 

# add item too menu
def add_item():

    def update_pie_chart(*args):
        calories = float(calories_val.get()) if calories_val.get() else 1
        protein = float(protein_val.get()) if protein_val.get() else 1
        total_fat = float(total_fat_val.get()) if total_fat_val.get() else 1
        total_carbohydrate = float(carbohydrate_val.get()) if carbohydrate_val.get() else 1
        total_sodium = float(sodium_val.get()) if sodium_val.get() else 1

        values = [calories, protein, total_fat, total_carbohydrate, total_sodium]
        categories = ['calories', 'protein', 'fat', 'carbohydrate', 'fat']

        ax.clear()
        ax.set_title(food_name.get(), fontsize=14, color='Black', loc='center', fontweight='bold', pad=20)
        ax.pie(values, radius=1, labels=categories, autopct="%1.2f%%")
        ax.axis('equal')  # Equal aspect ratio ensures that pie is circular.
        chart1.draw()

    global add_nutrition_button
    
    add_item_window = tk.Toplevel()
    add_item_window.title("Add item")
    add_item_window.geometry('1150x600')

    add_item_Frame = ttk.Frame(add_item_window, width=500, height=500)
    add_item_Frame.pack_propagate(False)
    add_item_Frame.grid(row = 0, column = 0, sticky = tk.W,padx=10, pady=10)

    food_name = tk.StringVar(value='test')
    calories_val = tk.IntVar(value=0)
    protein_val = tk.IntVar(value=0)
    total_fat_val = tk.IntVar(value=0)
    carbohydrate_val = tk.IntVar(value=0)
    sodium_val = tk.IntVar(value=0)

    nutrition_Label = ttk.Label(add_item_Frame, text="Nutrition Information")
    nutrition_Label.config(font=("Helvetica", 35))
    nutrition_Label.grid(row = 0, column = 0, columnspan = 1, sticky = "ew")

    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 1, column = 0, columnspan = 3, sticky="ew", pady=10)
    
    food_name_label = ttk.Label(add_item_Frame, text="Food name")
    food_name_label.grid(row = 2, column = 0, sticky = tk.W)
    food_name_Entry = ttk.Entry(add_item_Frame, textvariable=food_name)
    food_name_Entry.grid(row = 2, column = 1, sticky = tk.W)
    food_name_Entry.bind('<KeyRelease>', update_pie_chart)

    
    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 3, column = 0, columnspan = 3, sticky="ew", pady=10)
    
    calories_value_label = ttk.Label(add_item_Frame, text="Energy")
    calories_value_label.grid(row = 4, column = 0, sticky = tk.W)
    calories_value_entry = ttk.Entry(add_item_Frame, textvariable=calories_val)
    calories_value_entry.grid(row = 4, column = 1, sticky = tk.W)
    calories_value_entry.bind('<KeyRelease>', update_pie_chart)

    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 5, column = 0, columnspan = 3, sticky="ew", pady=10)
                                                
    protein_value_label = ttk.Label(add_item_Frame, text="Protein")
    protein_value_label.grid(row = 6, column = 0, sticky = tk.W)
    protein_value_Entry = ttk.Entry(add_item_Frame, textvariable=protein_val)
    protein_value_Entry.grid(row = 6, column = 1, sticky = tk.W)
    protein_value_Entry.bind('<KeyRelease>', update_pie_chart)


    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 7, column = 0, columnspan = 3, sticky="ew", pady=10)

    total_fat_Label = ttk.Label(add_item_Frame, text = "Fat")
    total_fat_Label.grid(row = 8, column = 0, sticky = tk.W)
    total_fat_Entry = ttk.Entry(add_item_Frame, textvariable=total_fat_val)
    total_fat_Entry.grid(row = 8, column = 1, sticky = tk.W)
    total_fat_Entry.bind('<KeyRelease>', update_pie_chart)

    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 9, column = 0, columnspan = 3, sticky="ew", pady=10)

    total_carbohydrate_Label = ttk.Label(add_item_Frame, text = "Carbohydrate")
    total_carbohydrate_Label.grid(row = 10, column = 0, sticky = tk.W)
    total_carbohydrate_Entry = ttk.Entry(add_item_Frame, textvariable=carbohydrate_val)
    total_carbohydrate_Entry.grid(row = 10, column = 1, sticky = tk.W)
    total_carbohydrate_Entry.bind('<KeyRelease>', update_pie_chart)

    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 11, column = 0, columnspan = 3, sticky="ew", pady=10)

    total_sodium_Label = ttk.Label(add_item_Frame, text = "Sodium")
    total_sodium_Label.grid(row = 12, column = 0, sticky = tk.W)
    total_sodium_Entry = ttk.Entry(add_item_Frame, textvariable=sodium_val)
    total_sodium_Entry.grid(row = 12, column = 1, sticky = tk.W)
    total_carbohydrate_Entry.bind('<KeyRelease>', update_pie_chart)
    
    separator = ttk.Separator(add_item_Frame, orient='horizontal')
    separator.grid(row = 13, column = 0, columnspan = 3, sticky="ew", pady=10)

    breakfast_option = tk.Checkbutton(add_item_Frame, text='Breakfast', variable=breakfast_var, onvalue="breakfast_items", offvalue="" ''',command=update_button_state''')
    breakfast_option.grid(row=14, column=0, columnspan=1, sticky="ew")

    lunch_option = tk.Checkbutton(add_item_Frame, text='Lunch', variable=lunch_var, onvalue="lunch_items", offvalue="" ''',command=update_button_state''')
    lunch_option.grid(row=15, column=0, columnspan=1, sticky="ew")

    dinner_option = tk.Checkbutton(add_item_Frame, text='Dinner', variable=dinner_var, onvalue="dinner_items", offvalue=""''',command=update_button_state''')
    dinner_option.grid(row=16, column=0, columnspan=1, sticky="ew")

    #stores entry varaible data
    add_nutrition_button = ttk.Button(add_item_Frame, text="enter value", command=lambda: store_food_to_file(food_name, protein_val, calories_val, total_fat_val, carbohydrate_val, sodium_val), state="disabled")
    add_nutrition_button.grid(row = 17, column = 0, columnspan = 3, sticky="ew", pady=10)

    add_pie = ttk.Frame(add_item_window, width=480, height=480)
    add_pie.pack_propagate(False)
    add_pie.grid(row = 0, column = 1, sticky = tk.W)

    chart1 = FigureCanvasTkAgg(fig, add_pie)
    chart1.get_tk_widget().grid(row = 0, column = 1, sticky = tk.W, padx = 10, pady=0)

    update_pie_chart()

###################################################################################################################################################################################
########################################################################        Add breakfast Window        ###########################################################################
###################################################################################################################################################################################

def add_breakfast_item_menu():
    global breakfast_items
    
    breakfast_window = tk.Toplevel()
    breakfast_window.title("Add breakfast item")
    breakfast_window.geometry('1000x1000')

    breakfasttable_frame = ttk.Frame(breakfast_window, width=1998, height=100, borderwidth=0)
    breakfasttable_frame.pack_propagate(False)
    breakfasttable_frame.pack()

    # Create the Treeview widget
    table = ttk.Treeview(breakfasttable_frame, columns=('food item', 'protein amount', 'calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings', height=150)
    table.heading('food item', text='food item')
    table.heading('protein amount', text='protein amount')
    table.heading('calories amount', text='calories amount')
    table.heading('Fat amount', text='Fat amount')
    table.heading('Carbohydrate amount', text='Carbohydrate amount')
    table.heading('Sodium amount', text='Sodium amount')

    #populates the table
    for i in range(0, len(breakfast_items)):
        # Insert a top-level item
        table.insert(parent='', index=0, values=(breakfast_items[i][0], breakfast_items[i][1], breakfast_items[i][2], breakfast_items[i][3],breakfast_items[i][4], breakfast_items[i][5]))
    table.pack(fill='both', expand=True)

    button_frame = ttk.Frame(breakfast_window, width=1998, height=50, borderwidth=0)
    button_frame.pack_propagate(False)
    button_frame.pack()

    #stores entry varaible data
    select_menu = ttk.Button(button_frame, text="enter selected items")
    select_menu.pack()
    
    def delete_items(_):
        for i in table.selection():
            #Find the index of the item selected
            index = table.index(i)
            #Delte the item from the array based on the index given 
            del breakfast_items[index]
            #delte the item from the table based on the index given 
            table.delete(i)

            # Read the contents of the file
            df = pd.read_csv(breakfast_menu_file_path)
            # Delete row by index
            df = df.drop(index)
            # Write the updated data back to the file
            df.to_csv(breakfast_menu_file_path, index=False)

  # add breakfast item to menu
    def item_select(_):
        global selected_breakfast_items 
        for item in table.selection():
            value = table.item(item)['values']
            selected_breakfast_items.append(value)
            #adds value to total array 
            total_items.append(value)

        for item in selected_breakfast_items:
            print("selected_breakfast_items", item)
        print("enter")

        breakfast_main_menu()
        total_main_menu()

    #Calls item delete  function when row is selected in table
    table.bind('<Delete>', delete_items)

    #Calls item select function when row is selected in table
    table.bind('<<TreeviewSelect>>', item_select)


###################################################################################################################################################################################
########################################################################        Add lunch Window        ###########################################################################
###################################################################################################################################################################################

def add_lunch_item_menu():
    global lunch_items
    
    lunch_window = tk.Toplevel()
    lunch_window.title("Add lunch item")
    lunch_window.geometry('1000x1000')

    lunchtable_frame = ttk.Frame(lunch_window, width=1998, height=200, borderwidth=0)
    lunchtable_frame.pack_propagate(False)
    lunchtable_frame.pack()

    # Create the Treeview widget
    table = ttk.Treeview(lunchtable_frame, columns=('food item', 'protein amount', 'calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
    table.heading('food item', text='food item')
    table.heading('protein amount', text='protein amount')
    table.heading('calories amount', text='calories amount')
    table.heading('Fat amount', text='Fat amount')
    table.heading('Carbohydrate amount', text='Carbohydrate amount')
    table.heading('Sodium amount', text='Sodium amount')

    #populates the table
    for i in range(0, len(lunch_items)):
        # Insert a top-level item
        table.insert(parent='', index=0, values=(lunch_items[i][0], lunch_items[i][1], lunch_items[i][2], lunch_items[i][3],lunch_items[i][4], lunch_items[i][5]))
    table.pack(fill='both', expand=True)

    button_frame = ttk.Frame(lunch_window, width=1998, height=50, borderwidth=0)
    button_frame.pack_propagate(False)
    button_frame.pack()

    #stores entry varaible data
    select_menu = ttk.Button(button_frame, text="enter selected items")
    select_menu.pack()
    
    def delete_items(_):
        for i in table.selection():
            #Find the index of the item selected
            index = table.index(i)
            #Delte the item from the array based on the index given 
            del lunch_items[index]
            #delte the item from the table based on the index given 
            table.delete(i)

            # Read the contents of the file
            df = pd.read_csv(lunch_menu_file_path)
            # Delete row by index
            df = df.drop(index)
            # Write the updated data back to the file
            df.to_csv(lunch_items, index=False)

  # add breakfast item to menu
    def item_select(_):
        global selected_lunch_items 
        for item in table.selection():
            value = table.item(item)['values']
            selected_lunch_items.append(value)
            total_items.append(value)

        for item in selected_lunch_items:
            print("selected_lunch_items", item)
        print("enter")

        lunch_main_menu()
        total_main_menu()
        

    #Calls item delete  function when row is selected in table
    table.bind('<Delete>', delete_items)

    #Calls item select function when row is selected in table
    table.bind('<<TreeviewSelect>>', item_select)


###################################################################################################################################################################################
########################################################################        Add dinner Window        ###########################################################################
###################################################################################################################################################################################

#####
def add_dinner_item_menu():
    global dinner_items
    
    dinner_window = tk.Toplevel()
    dinner_window.title("Add dinner item")
    dinner_window.geometry('1000x1000')

    dinnertable_frame = ttk.Frame(dinner_window, width=1998, height=200, borderwidth=0)
    dinnertable_frame.pack_propagate(False)
    dinnertable_frame.pack()

    # Create the Treeview widget
    table = ttk.Treeview(dinner_window, columns=('food item', 'protein amount', 'calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
    table.heading('food item', text='food item')
    table.heading('protein amount', text='protein amount')
    table.heading('calories amount', text='calories amount')
    table.heading('Fat amount', text='Fat amount')
    table.heading('Carbohydrate amount', text='Carbohydrate amount')
    table.heading('Sodium amount', text='Sodium amount')

    #populates the table
    for i in range(0, len(dinner_items)):
        # Insert a top-level item
        table.insert(parent='', index=0, values=(dinner_items[i][0], dinner_items[i][1], dinner_items[i][2], dinner_items[i][3],dinner_items[i][4], dinner_items[i][5]))
    table.pack(fill='both', expand=True)

    button_frame = ttk.Frame(dinner_window, width=1998, height=50, borderwidth=0)
    button_frame.pack_propagate(False)
    button_frame.pack()

    #stores entry varaible data
    select_menu = ttk.Button(button_frame, text="enter selected items")
    select_menu.pack()
    
    def delete_items(_):
        for i in table.selection():
            #Find the index of the item selected
            index = table.index(i)
            #Delte the item from the array based on the index given 
            del dinner_items[index]
            #delte the item from the table based on the index given 
            table.delete(i)

            # Read the contents of the file
            df = pd.read_csv(dinner_menu_file_path)
            # Delete row by index
            df = df.drop(index)
            # Write the updated data back to the file
            df.to_csv(dinner_items, index=False)

  # add breakfast item to menu
    def item_select(_):
        global selected_dinner_items 
        for item in table.selection():
            value = table.item(item)['values']
            selected_dinner_items.append(value)
            total_items.append(value)

        for item in selected_dinner_items:
            print("selected_dinner_items", item)
        print("enter")

        dinner_main_menu()
        total_main_menu()

    #Calls item delete  function when row is selected in table
    table.bind('<Delete>', delete_items)

    #Calls item select function when row is selected in table
    table.bind('<<TreeviewSelect>>', item_select)

###################################################################################################################################################################################
########################################################################        Diary total window      ###########################################################################
###################################################################################################################################################################################

def diary_total_window():
    diary_window = tk.Toplevel()
    diary_window.title("Add dinner item")
    diary_window.geometry('1000x1000')

    dinnertable_frame = ttk.Frame(diary_window, width=1998, height=200, borderwidth=0)
    dinnertable_frame.pack_propagate(False)
    dinnertable_frame.grid()

    global total_items

    # Create the Treeview widget
    table = ttk.Treeview(dinnertable_frame, columns=('Date', 'protein amount', 'calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
    table.heading('Date', text='food item')
    table.heading('protein amount', text='protein amount')
    table.heading('calories amount', text='calories amount')
    table.heading('Fat amount', text='Fat amount')
    table.heading('Carbohydrate amount', text='Carbohydrate amount')
    table.heading('Sodium amount', text='Sodium amount')

    protein_amount = 0
    calories_amount= 0
    fat_amount = 0
    carbohydrate_amount = 0
    sodium_amount = 0

    for i in range(0,len(total_items)):
        protein_amount += total_items[i][1]
        calories_amount += total_items[i][2]
        fat_amount += total_items[i][3]
        carbohydrate_amount += total_items[i][4]
        sodium_amount += total_items[i][5]
    
    total_items.clear()
    
    '''store items from total items into diary entry list'''
    if diary_diet[-1][0] == (datetime.today().strftime('%Y-%m-%d')): 
        del diary_diet[-1]
        diary_diet.append([(datetime.today().strftime('%Y-%m-%d')), protein_amount-120, calories_amount-2400, fat_amount-95, carbohydrate_amount-325, sodium_amount-230])
    else: 
        diary_diet.append([(datetime.today().strftime('%Y-%m-%d')), protein_amount-120, calories_amount-2400, fat_amount-95, carbohydrate_amount-325, sodium_amount-230])
        '''take diary entry list and store it in file'''
        
    with open(diary_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        #Stores 2D array into file
        writer.writerows(diary_diet)
    print("2D array saved to file:", diary_file_path)

    '''wipe last table entries'''
    for item in table.get_children():
        table.delete(item)
    
    '''populate table from diary diet'''
    for row in diary_diet:
        table.insert(parent='', index=0, values=row)
        table.grid(row = 10, column = 0, columnspan = 1, sticky="ew", pady=10)

    # Configure the row tags
    table.tag_configure('PASS', background="green")
    table.tag_configure('FAIL', background="red")

    # Apply the row tags based on protein and calorie values
    for row in table.get_children():
        values = table.item(row)['values']
        protein_val = int(values[1])
        calories_val = int(values[2])
        
        if protein_val >= 100 and calories_val >= 2000:
            table.item(row, tags='PASS')
        else:
            table.item(row, tags='FAIL')

        
    for item in breakfast_table.get_children():
        breakfast_table.delete(item)

    for item in lunch_table.get_children():
        lunch_table.delete(item)

    for item in dinner_table.get_children():
        dinner_table.delete(item)
    
    for item in total_table.get_children():
        total_table.delete(item)

    def delete_menu(_):
        for i in table.selection():
            #Find the index of the item selected
            index = table.index(i)
            #Delete the item from the array based on the index given 
            del diary_diet[index]
            #delte the item from the table based on the index given 
            table.delete(i)

    table.bind('<Delete>', delete_menu)

    total_main_menu()
###################################################################################################################################################################################
########################################################################        target amount window        ###########################################################################
###################################################################################################################################################################################


###################################################################################################################################################################################
########################################################################        MAIN MENU Frame        ###########################################################################
###################################################################################################################################################################################

add_item_to_menu = ttk.Button(window, text="add item to menu", command=add_item)
add_item_to_menu.grid(row=0, column=0,columnspan=1, sticky="e")

breakfast_label = ttk.Label(window, text="breakfast")
breakfast_label.grid(row=1, column=0, columnspan=1, sticky="n")

breakfast_menu = ttk.Button(window, text="add breakfast item",command=add_breakfast_item_menu)
breakfast_menu.grid(row=2, column=0, columnspan=3, sticky="ew")

# Create the Treeview widget
breakfast_table = ttk.Treeview(window, columns=('Food item', 'Protein amount', 'Calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
breakfast_table.heading('Food item', text='food item')
breakfast_table.heading('Protein amount', text='Protein amount')
breakfast_table.heading('Calories amount', text='Calories amount')
breakfast_table.heading('Fat amount', text='Fat amount')
breakfast_table.heading('Carbohydrate amount', text='Carbohydrate amount')
breakfast_table.heading('Sodium amount', text='Sodium amount')
breakfast_table.configure(height=5)

lunch_label = ttk.Label(window, text="lunch")
lunch_label.grid(row=4, column=0, columnspan=1, sticky="n")

lunch_menu = ttk.Button(window, text="add lunch item",command=add_lunch_item_menu)
lunch_menu.grid(row=5, column=0, columnspan=3, sticky="ew")

# Create the Treeview widget
lunch_table = ttk.Treeview(window, columns=('Food item', 'Protein amount', 'Calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
lunch_table.heading('Food item', text='Food item')
lunch_table.heading('Protein amount', text='Protein amount')
lunch_table.heading('Calories amount', text='Calories amount')
lunch_table.heading('Fat amount', text='Fat amount')
lunch_table.heading('Carbohydrate amount', text='Carbohydrate amount')
lunch_table.heading('Sodium amount', text='Sodium amount')
lunch_table.configure(height=5)

dinner_label = ttk.Label(window, text="dinner")
dinner_label.grid(row=7, column=0, columnspan=1, sticky="n")

dinner_label = ttk.Button(window, text="add dinner item",command=add_dinner_item_menu)
dinner_label.grid(row=8, column=0, columnspan=3, sticky="ew")


# Create the Treeview widget
dinner_table = ttk.Treeview(window, columns=('Food item', 'Protein amount', 'Calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
dinner_table.heading('Food item', text='Food item')
dinner_table.heading('Protein amount', text='Protein amount')
dinner_table.heading('Calories amount', text='Calories amount')
dinner_table.heading('Fat amount', text='Fat amount')
dinner_table.heading('Carbohydrate amount', text='Carbohydrate amount')
dinner_table.heading('Sodium amount', text='Sodium amount')
dinner_table.configure(height=5)

#Total Table
total_table = ttk.Treeview(window, columns=('Food item', 'Protein amount', 'Calories amount', 'Fat amount', 'Carbohydrate amount', 'Sodium amount'), show='headings')
total_table.heading('Food item', text='Food item')
total_table.heading('Protein amount', text='Protein amount')
total_table.heading('Calories amount', text='Calories amount')
total_table.heading('Fat amount', text='Fat amount')
total_table.heading('Carbohydrate amount', text='Carbohydrate amount')
total_table.heading('Sodium amount', text='Sodium amount')
total_table.configure(height=1)

submit_button = ttk.Button(window, text="submit to diary",command=diary_total_window)
submit_button.grid(row=11, column=0, columnspan=3, sticky="ew")

##############################################################################################################################################################################
########################################################################        populate breakfast table        ###########################################################################
###################################################################################################################################################################################

def breakfast_main_menu():
    #populates the table
    for i in range(0, len(selected_breakfast_items)):
        # Insert a top-level item
        breakfast_table.insert(parent='', index=0, values=(selected_breakfast_items[i][0], selected_breakfast_items[i][1], selected_breakfast_items[i][2], selected_breakfast_items[i][3], selected_breakfast_items[i][4], selected_breakfast_items[i][5]))
            
    breakfast_table.grid(row = 3, column = 0, columnspan = 1, sticky="ew", pady=10)
    selected_breakfast_items.clear()
    
    #passes all the values from tables and sends them to total calculation function
    #breakfast_total_calculation(total_protein_amount, total_calories_amount, total_Fat_amount, total_Carbohydrates_amount, total_Sodium_amount)

breakfast_main_menu()
    
def delete_items(_):
    for i in breakfast_table.selection():
        #Find the index of the item selected
        index = breakfast_table.index(i)
        #Delete the item from the array based on the index given 
        #del breakfast_items[index]
        #delte the item from the table based on the index given 
        breakfast_table.delete(i)

        del total_items[index]

    total_main_menu()

#Calls item delete  function when row is selected in table
breakfast_table.bind('<Delete>', delete_items)
    
##############################################################################################################################################################################
########################################################################        populate lunch table        ###########################################################################
###################################################################################################################################################################################

def lunch_main_menu():
    for i in range(0, len(selected_lunch_items)):
        # Insert a top-level item
        lunch_table.insert(parent='', index=0, values=(selected_lunch_items[i][0], selected_lunch_items[i][1], selected_lunch_items[i][2], selected_lunch_items[i][3], selected_lunch_items[i][4], selected_lunch_items[i][5]))
    lunch_table.grid(row = 6, column = 0, columnspan = 1, sticky="ew", pady=10)
    selected_lunch_items.clear()
lunch_main_menu()

def delete_items_lunch(_):
    for i in lunch_table.selection():
        #Find the index of the item selected
        index = lunch_table.index(i)
        #Delte the item from the array based on the index given 
        #del lunch_items[index]
        #delte the item from the table based on the index given 
        lunch_table.delete(i)
        del total_items[index]

    total_main_menu()

#Calls item delete  function when row is selected in table
lunch_table.bind('<Delete>', delete_items_lunch)

##############################################################################################################################################################################
########################################################################        populate dinner table        ###########################################################################
###################################################################################################################################################################################

def dinner_main_menu():
    for i in range(0, len(selected_dinner_items)):
        # Insert a top-level item
        dinner_table.insert(parent='', index=0, values=(selected_dinner_items[i][0], selected_dinner_items[i][1], selected_dinner_items[i][2], selected_dinner_items[i][3], selected_dinner_items[i][4], selected_dinner_items[i][5]))
    dinner_table.grid(row = 9, column = 0, columnspan = 1, sticky="ew", pady=10)
    selected_dinner_items.clear()
dinner_main_menu()

def delete_items_dinner(_):    
    for i in dinner_table.selection():
        #Find the index of the item selected
        index = dinner_table.index(i)
        #Delte the item from the array based on the index given 
        #del dinner_items[index]
        #delte the item from the table based on the index given 
        dinner_table.delete(i)

        #total_items.remove(index)

        del total_items[index]

    total_main_menu()

#Calls item delete  function when row is selected in table
dinner_table.bind('<Delete>', delete_items_dinner)

##############################################################################################################################################################################
########################################################################        Total table        ###########################################################################
###################################################################################################################################################################################

def total_main_menu():
    global total_items

    protein_amount = 0
    calories_amount= 0
    fat_amount = 0
    carbohydrate_amount = 0
    sodium_amount = 0

    for i in range(0,len(total_items)):
        protein_amount += total_items[i][1]
        calories_amount += total_items[i][2]
        fat_amount += total_items[i][3]
        carbohydrate_amount += total_items[i][4]
        sodium_amount += total_items[i][5]

    # Insert a top-level item
    total_table.insert(parent='', index=0, values=("TOTAL", protein_amount, calories_amount, fat_amount, carbohydrate_amount, sodium_amount))
    total_table.grid(row = 10, column = 0, columnspan = 1, sticky="ew", pady=10)
total_main_menu()

##############################################################################################################################################################################
########################################################################    Store, Reset 24 hour        ###########################################################################
###################################################################################################################################################################################


window.mainloop()
