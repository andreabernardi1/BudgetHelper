from tkinter import *
from tkinter import ttk

#=========Main window============    
    
window_root = Tk()
window_root.geometry("1100x700+600+100")
window_root.title("BudgetHelper")

#=======Classes========

class myEntry(Entry):
    def __init__(self, root = window_root, sample = "sample_text", color = "grey"):
        super().__init__(root)

        self.sample = sample
        self.sample_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_sample()

    def put_sample(self):
        self.insert(0, self.sample)
        self["fg"] = self.sample_color

    def foc_in(self, *args):
        if self["fg"] == self.sample_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_sample()
      
#=========functions=====

def sum_restaurant():
    base_value = 0
    a, b = float(restaurant_food.get()), float(restaurant_drinks.get())
    base_value = a + b
    tot_restaurant_value_label["text"] = str(base_value)
            
def sum_travel():
    base_value = 0
    a, b, c = float(travel_bus.get()), float(travel_plane.get()), float(travel_metro.get())
    base_value = a + b + c
    tot_travel_value_label["text"] = str(base_value)

def sum_groceries():
    base_value = 0
    a = float(groceries_all.get())
    base_value = a
    tot_groceries_value_label["text"] = str(base_value)
    
def sum_salary():
    base_value = 0
    a = float(salary_all.get())
    base_value = a
    tot_salary_value_label["text"] = str(base_value)

def sum_assets():
    base_value = 0
    a, b = float(assets_stocks.get()), float(assets_bonds.get())
    base_value = a + b
    tot_assets_value_label["text"] = str(base_value)

def sum_others():
    base_value = 0
    a = float(others_all.get())
    base_value = a
    tot_others_value_label["text"] = str(base_value)

def register_restaurant():
    a = tot_restaurant_value_label.cget("text")
    b = restaurant_food.get()
    c = restaurant_drinks.get()
    restaurant_list.append(a)
    restaurant_food_list.append(b)
    restaurant_drinks_list.append(c)
    
    restaurant_food.delete(0, END)
    restaurant_drinks.delete(0, END)
    
def register_travel():
    a = tot_travel_value_label.cget("text")
    b = travel_bus.get()
    c = travel_metro.get()
    d = travel_plane.get()
    
    travel_list.append(a)
    travel_bus_list.append(b)
    travel_metro_list.append(c)
    travel_plane_list.append(d)
       
    travel_bus.delete(0, END)
    travel_metro.delete(0, END)
    travel_plane.delete(0, END)
    
def register_groceries():
    a = tot_groceries_value_label.cget("text")
    groceries_list.append(a)
    
    groceries_all.delete(0, END)
    

def register_salary():
    a = tot_salary_value_label.cget("text")
    salary_list.append(a)
    
    salary_all.delete(0, END)
    
def register_assets():
    a = tot_assets_value_label.cget("text")
    b = assets_stocks.get()
    c = assets_bonds.get()
    
    assets_list.append(a)
    assets_stocks_list.append(b)
    assets_bonds_list.append(c)
    
    assets_stocks.delete(0, END)
    assets_bonds.delete(0, END)
    
def register_others():
    a = tot_others_value_label.cget("text")
    others_list.append(a)
    
    others_all.delete(0, END)

def show_exp_rest():
    a = [float(i) for i in restaurant_list]
    b = sum(a)
    c = [float(i) for i in restaurant_food_list]
    d = sum(c)
    e = [float(i) for i in restaurant_drinks_list]
    f = sum(e)
    tot_exp_rest_label["text"] = b
    tot_rest_food_label["text"] = d
    tot_rest_drinks_label["text"] = f
    
def show_exp_travel():
    a = [float(i) for i in travel_list]
    b = sum(a)
    c = [float(i) for i in travel_bus_list]
    d = sum(c)
    e = [float(i) for i in travel_metro_list]
    f = sum(e)
    g = [float(i) for i in travel_plane_list]
    h = sum(g)
    tot_exp_travel_label["text"] = b
    tot_travel_bus_label["text"] = d
    tot_travel_metro_label["text"] = f
    tot_travel_plane_label["text"] = h
    
def show_exp_groc():
    a = [float(i) for i in groceries_list]
    b = sum(a)
    tot_exp_groc_label["text"] = b
    
def show_rev_sal():
    a = [float(i) for i in salary_list]
    b = sum(a)
    tot_rev_sal_label["text"] = b

def show_rev_assets():
    a = [float(i) for i in assets_list]
    b = sum(a)
    c = [float(i) for i in assets_stocks_list]
    d = sum(c)
    e = [float(i) for i in assets_bonds_list]
    f = sum(e)
    tot_rev_assets_label["text"] = b
    tot_assets_stocks_label["text"] = d
    tot_assets_bonds_label["text"] = f
    
def show_rev_others():
    a = [float(i) for i in others_list]
    b = sum(a)
    tot_rev_others_label["text"] = b

def total():
    a = [float(i) for i in restaurant_list]
    b = [float(i) for i in travel_list]
    c = [float(i) for i in groceries_list]
    d = [float(i) for i in salary_list]
    e = [float(i) for i in assets_list]
    f = [float(i) for i in others_list]
    budget = sum(d) + sum(e) + sum(f) - (sum(a) + sum(b) + sum(c))
    budget_label["text"] = budget    

#creates clear and exit application in menu app
def reset():
    del restaurant_list[0:]
    del travel_list[0:]
    del groceries_list[0:]

    del salary_list[0:]
    del assets_list[0:]
    del others_list[0:]
    

#colors
EXP = "#f9e3d1"
REV = "#d1f9d5"
RES = "#e2e2e2"
BUT = "#ffa3a3"

#fonts
TNR16 = ("Times New Roman", (16))
TNR12 = ("Times New Roman", (12))
H12 = ("Helvetica", (12))

menu = Menu(window_root)
window_root.config(menu = menu)
file = Menu(menu)
file.add_command(label = "Clear", command = reset)
menu.add_cascade(label = "File", menu = file)
file.add_cascade(label = "Quit", command = window_root.destroy)

#===================DEFINES FRAMES===================================

frame1 = Frame(window_root, bg = EXP)      
frame1.place(relwidth = 0.5, relheight = 0.79)      

frame2 = Frame(window_root, bg = REV)
frame2.place(relwidth = 0.5, relheight = 0.79, relx = 0.5)

frame3 = Frame(window_root, bg = RES)
frame3.place(relwidth = 1, relheight = 0.21, rely = 0.79)

#global lists to store values

restaurant_list  = []
restaurant_food_list = []
restaurant_drinks_list = []

travel_list = []
travel_bus_list = []
travel_plane_list = []
travel_metro_list = []

groceries_list = []


salary_list = []

assets_list = []
assets_stocks_list = []
assets_bonds_list = []

others_list = []

#headers
Label(frame1, text = "Expenditure:", font = TNR16,
      bg = EXP ).grid(row = 0, column = 0, sticky = W)
Label(frame2, text = "Revenue:", font = TNR16,
      bg = REV).grid(row = 0, column = 0, sticky = W)

#choices/inputs
#==========restaurant===========

restaurant_label = Label(frame1, text = "Restaurant: ", 
                         font = H12, bg = EXP).grid(row = 1, column = 0, pady = 10, sticky = W)

restaurant_food_label = Label(frame1, text = "food:", font = TNR12,
                              bg = EXP, pady = 5).grid(row = 1, column = 1)
restaurant_food = myEntry(frame1, "0")
restaurant_food.grid(row = 1, column = 2, pady = 5, padx = 5)

restaurant_drinks_label = Label(frame1, text = "drinks:", font = TNR12,
                                bg = EXP, pady = 5).grid(row = 2, column = 1)
restaurant_drinks = myEntry(frame1, "0")
restaurant_drinks.grid(row = 2, column = 2, pady = 5, padx = 5)

Enter_restaurant = ttk.Button(frame1, text = "Confirm",
                              command = sum_restaurant).grid(row = 2, column = 3, padx = 10)

tot_restaurant_label = Label(frame1, text = "Total restaurant expenditure: ", bg = EXP, font = H12,
                             pady = 30).grid(row = 3, column = 0, sticky = W)
tot_restaurant_value_label = Label(frame1, text = "0", bg = EXP)
tot_restaurant_value_label.grid(row = 3, column = 2)

Register_restaurant = ttk.Button(frame1, text = "Register", 
                                command = register_restaurant).grid(row = 3, column = 3)

#=========travel============

travel_label = Label(frame1, text = "Travelling: ", font = H12,
                     bg = EXP).grid(row = 4, column = 0, pady = 5, sticky = W)

travel_bus_label = Label(frame1, text = "bus:", font = TNR12,
                         bg = EXP, pady = 5).grid(row = 4, column = 1)
travel_bus = myEntry(frame1, "0")
travel_bus.grid(row = 4, column = 2, pady = 5, padx = 5)

travel_metro_label = Label(frame1, text = "metro:", font = TNR12,
                           bg = EXP, pady = 5).grid(row = 5, column = 1)
travel_metro = myEntry(frame1, "0")
travel_metro.grid(row = 5, column = 2, pady = 5, padx = 5)

travel_plane_label = Label(frame1, text = "plane:", font = TNR12,
                           bg = EXP, pady = 5).grid(row = 6, column = 1)
travel_plane = myEntry(frame1, "0")
travel_plane.grid(row = 6, column = 2, pady = 5, padx = 5)

Enter_travel = ttk.Button(frame1, text = "Confirm",
                          command = sum_travel).grid(row = 6, column = 3, padx = 10)

tot_travel_label = Label(frame1, text = "Total travel expenditure: ", bg = EXP,
                         font = H12, pady = 30).grid(row = 7, column = 0, sticky = W)
tot_travel_value_label = Label(frame1, text = "0", bg = EXP)
tot_travel_value_label.grid(row = 7, column = 2)

Register_travel = ttk.Button(frame1, text = "Register", 
                                command = register_travel).grid(row = 7, column = 3)


#===========groceries==========

groceries_label = Label(frame1, text = "Groceries: ", font = H12,
                     bg = EXP).grid(row = 8, column = 0, pady = 5, sticky = W)

groceries_all_label = Label(frame1, text = "all:", font = TNR12,
                            bg = EXP, pady = 5).grid(row = 8, column = 1)
groceries_all = myEntry(frame1, "0")
groceries_all.grid(row = 8, column = 2)

Enter_groceries = ttk.Button(frame1, text = "Confirm", 
                             command = sum_groceries).grid(row = 8, column = 3, padx = 10)

tot_groceries_label = Label(frame1, text = "Total groceries expenditure: ", bg = EXP,
                         font = H12, pady = 30).grid(row = 9, column = 0, sticky = W)
tot_groceries_value_label = Label(frame1, text = "0", bg = EXP)
tot_groceries_value_label.grid(row = 9, column = 2)

Register_groceries = ttk.Button(frame1, text = "Register", 
                                command = register_groceries).grid(row = 9, column = 3)

#===============revenues===============
#salary

salary_label = Label(frame2, text = "Salary: ", font = H12,
                     bg = REV).grid(row = 1, column = 0, pady = 5, sticky = W)

salary_all_label = Label(frame2, text = "all:", font = TNR12,
                         bg = REV, pady = 5, padx = 5).grid(row = 1, column = 1)
salary_all = myEntry(frame2, "0")
salary_all.grid(row = 1, column = 2)

Enter_salary = ttk.Button(frame2, text = "Confirm", 
                          command = sum_salary).grid(row = 1, column = 3, padx = 10)

tot_salary_label = Label(frame2, text = "Total salary revenue: ", bg = REV,
                         font = H12, pady = 30).grid(row = 2, column = 0, sticky = W)
tot_salary_value_label = Label(frame2, text = "0", bg = REV)
tot_salary_value_label.grid(row = 2, column = 2)

Register_salary = ttk.Button(frame2, text = "Register", 
                                command = register_salary).grid(row = 2, column = 3)



#==========assets================

assets_label = Label(frame2, text = "Assets:", font = H12,
                     bg = REV).grid(row = 3, column = 0, pady = 5, padx = 5, sticky = W)

assets_stocks_label = Label(frame2, text = "stocks:", font = TNR12,
                            bg = REV, pady = 5, padx = 5).grid(row = 3, column = 1)
assets_stocks = myEntry(frame2, "0")
assets_stocks.grid(row = 3, column = 2)

assets_bonds_label = Label(frame2, text = "bonds:", font = TNR12,
                           bg = REV, pady = 5, padx = 5).grid(row = 4, column = 1)
assets_bonds = myEntry(frame2, "0")
assets_bonds.grid(row = 4, column = 2)

Enter_assets = ttk.Button(frame2, text = "Confirm", 
                          command = sum_assets).grid(row = 4, column = 3, padx = 10)

tot_assets_label = Label(frame2, text = "Total assets revenue: ", bg = REV,
                         font = H12, pady = 30).grid(row = 5, column = 0, sticky = W)
tot_assets_value_label = Label(frame2, text = "0", bg = REV)
tot_assets_value_label.grid(row = 5, column = 2)

Register_assets = ttk.Button(frame2, text = "Register", 
                                command = register_assets).grid(row = 5, column = 3)


#===========Other====================

others_label = Label(frame2, text = "Others:", bg = REV,
                    font = H12).grid(row = 6, column = 0, pady = 5, padx = 5, sticky = W)

others_all_label = Label(frame2, text = "all:", font = TNR12,
                        bg = REV, pady = 5, padx = 5).grid(row = 6, column = 1)
others_all = myEntry(frame2, "0")
others_all.grid(row = 6, column = 2)

Enter_others = ttk.Button(frame2, text = "Confirm",
                         command = sum_others).grid(row = 6, column = 3)

tot_others_label = Label(frame2, text = "Total others: ", bg = REV,
                              font = H12, pady = 30).grid(row = 7, column = 0, sticky = W)
tot_others_value_label = Label(frame2, text = "0", bg = REV)
tot_others_value_label.grid(row = 7, column = 2)

Register_others = ttk.Button(frame2, text = "Register", 
                                command = register_others).grid(row = 7, column = 3)

#========bottom frame==================

tot_exp_rest = Button(frame3, text = "Restaurant expenses", width = 15, height = 2,
                      fg = "black", font = TNR12, bg = "#ffa3a3", relief = FLAT,
                      command = show_exp_rest).grid(row = 0, column = 0, sticky = N)
tot_exp_rest_label = Label(frame3, text = "0", bg = RES)
tot_exp_rest_label.grid(row = 4, column = 0, pady = 5)


tot_exp_travel = Button(frame3, text = "Travel expenses", width = 15, height = 2,
                      fg = "black", font = TNR12, bg = "#ffa3a3", relief = FLAT,
                      command = show_exp_travel).grid(row = 0, column = 1, padx = 1, sticky = N)
tot_exp_travel_label = Label(frame3, text = "0", bg = RES)
tot_exp_travel_label.grid(row = 4, column = 1, pady = 5)

tot_exp_groc = Button(frame3, text = "Groceries expenses", width = 15, height = 2,
                      fg = "black", font = TNR12, bg = "#ffa3a3", relief = FLAT,
                      command = show_exp_groc).grid(row = 0, column = 2, padx = 1, sticky = N)
tot_exp_groc_label = Label(frame3, text = "0", bg = RES)
tot_exp_groc_label.grid(row = 4, column = 2, pady = 5)

tot_rev_sal =  Button(frame3, text = "Salary revenue", width = 15, height = 2,
                      fg = "black", font = TNR12, bg = "#b0f79e", relief = FLAT,
                      command = show_rev_sal).grid(row = 0, column = 3, padx = 1, sticky = N)
tot_rev_sal_label = Label(frame3, text = "0", bg = RES)
tot_rev_sal_label.grid(row = 4, column = 3, pady = 5)

tot_rev_assets =  Button(frame3, text = "Assets revenue", width = 15, height = 2,
                      fg = "black", font = TNR12, bg = "#b0f79e", relief = FLAT,
                      command = show_rev_assets).grid(row = 0, column = 4, padx = 1, sticky = N)
tot_rev_assets_label = Label(frame3, text = "0", bg = RES)
tot_rev_assets_label.grid(row = 4, column = 4)

tot_rev_others =  Button(frame3, text = "Other revenue", width = 15, height = 2,
                      fg = "black", font = TNR12, bg = "#b0f79e", relief = FLAT,
                      command = show_rev_others).grid(row = 0, column = 5, padx = 1, sticky = N)
tot_rev_others_label = Label(frame3, text = "0", bg = RES)
tot_rev_others_label.grid(row = 4, column = 5)

Budget = Button(frame3, text = "Budget", width = 24, height = 2,
                      fg = "black", font = TNR12, bg = "#8cb0ff", relief = FLAT,
                      command = total).grid(row = 0, column = 6, padx = 1, sticky = N)
budget_label = Label(frame3, text = "0", bg = RES)
budget_label.grid(row = 4, column = 6)

tot_rest_food_label = Label(frame3, text = "0", bg = RES)
tot_rest_food_label.grid(row = 1, column = 0)

tot_rest_drinks_label = Label(frame3, text = "0", bg = RES)
tot_rest_drinks_label.grid(row = 2, column = 0)

tot_travel_bus_label = Label(frame3, text = "0", bg = RES)
tot_travel_bus_label.grid(row = 1, column = 1)

tot_travel_metro_label = Label(frame3, text = "0", bg = RES)
tot_travel_metro_label.grid(row = 2, column = 1)

tot_travel_plane_label = Label(frame3, text = "0", bg = RES)
tot_travel_plane_label.grid(row = 3, column = 1)

tot_assets_stocks_label = Label(frame3, text = "0", bg = RES)
tot_assets_stocks_label.grid(row = 1, column = 4)

tot_assets_bonds_label = Label(frame3, text = "0", bg = RES)
tot_assets_bonds_label.grid(row = 2, column = 4)


if __name__=="__main__":
    window_root.mainloop()