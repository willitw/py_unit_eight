# just like importing turtle, you must import tkinter for this interface
import tkinter as tk

# this code sets up the window for us and gives it a title
root = tk.Tk()
root.title("Tip Calculator")

# here is the function that performs the calculations and sets the values
def calculate_tip():
    # price * % tip + price / people
    total_with_tip = (float(cost.get()) * float(tip_percent.get()/100)) + float(cost.get())
    per_person = total_with_tip / people.get()
    total.set("$" + str(per_person))

# this set up the default cost of zero when the interface opens
cost = tk.StringVar()
cost.set(0)

# this sets a default tip percentage when the interface opens
tip_percent = tk.IntVar()
tip_percent.set(15)

people = tk.IntVar()

# this set up the default total cost of the meal (to zero) when the interface opens
total = tk.StringVar()
total.set("$0")

# this creates a label at the top of the screen
word = tk.Label(root, text="Tip Calculator")
word.grid(row=1, column=1, columnspan=2)

# this next set of code sets up the user interface with various labels and entry boxes

meal_cost_label = tk.Label(root, text="Meal cost:")
meal_cost_label.grid(row=2, column=1, sticky="E")

meal_cost_entry = tk.Entry(root, textvariable=cost)
meal_cost_entry.grid(row=2, column=2, sticky="W")

tip_label = tk.Label(root, text="Tip percent:")
tip_label.grid(row=3, column=1, sticky="E")

tip_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=tip_percent)
tip_slider.grid(row=3, column=2, sticky="W")

diners_label = tk.Label(root, text="Number of diners:")
diners_label.grid(row=4, column=1, columnspan=2, pady=15)

button_frame = tk.Frame(root)
button_frame.grid(row=5, column=1, columnspan=2, pady=15)

# this code sets up the buttons that allow the user to designate how many diners are splitting the tip
num_diners1 = tk.Radiobutton(button_frame, text="1", value=1, variable=people)
num_diners1.grid(row=5, column=1, padx=10)
num_diners2 = tk.Radiobutton(button_frame, text="2", value=2, variable=people)
num_diners2.grid(row=5, column=2, padx=10)
num_diners3 = tk.Radiobutton(button_frame, text="3", value=3, variable=people)
num_diners3.grid(row=5, column=3, padx=10)
num_diners4 = tk.Radiobutton(button_frame, text="4", value=4, variable=people)
num_diners4.grid(row=5, column=4, padx=10)
num_diners5 = tk.Radiobutton(button_frame, text="5", value=5, variable=people)
num_diners5.grid(row=5, column=5, padx=10)

# next we set up a label and then the total cost per person to display
total_label = tk.Label(root, text="")
total_label.grid(row=6, column=1)

total_display = tk.Label(root, textvariable=total)
total_display.grid(row=6, column=2)

# this "calls" the function so that it will run, based on the amounts entered
calculate = tk.Button(root, text="Calculate total per person", command=calculate_tip)
calculate.grid(row=7, column=1, columnspan=2)


def calculate_ONLYtip():
    # price * % tip + price / people
    total_tip = (float(cost.get()) * float(tip_percent.get()/100))

    total.set("$" + str(total_tip))


total_label = tk.Label(root, text="")
total_label.grid(row=8, column=1)

calculate = tk.Button(root, text="Calculate total tip", command=calculate_ONLYtip)
calculate.grid(row=9, column=1, columnspan=2)

root.mainloop()

