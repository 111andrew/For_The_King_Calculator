import tkinter as tk
import math
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class for_the_king_gui:
    def __init__(self, master):
        
        self.master = master
        master.configure(background="blue")
        master.title("For the King Calculator")
        master.geometry("1200x800")

        label_1 = tk.Label(master, text="# of Slot: ")
        label_1.grid(row=1, column=1)
        label_2 = tk.Label(master, text="Slot Acc: ")
        label_2.grid(row=2, column=1)
        label_3 = tk.Label(master, text="Total Dmg: ")
        label_3.grid(row=3, column=1)

        slot_num_var = tk.IntVar()

        slot_num_box = tk.Entry(master, textvariable=slot_num_var)
        slot_num_box.grid(row=1, column=2, columnspan=1, ipadx=0.5)

        slot_acc_var = tk.DoubleVar()

        slot_acc_box = tk.Entry(master, textvariable=slot_acc_var)
        slot_acc_box.grid(row=2, column=2, columnspan=1, ipadx=1)

        slot_dmg_var = tk.IntVar()

        slot_dmg_box = tk.Entry(master, textvariable=slot_dmg_var)
        slot_dmg_box.grid(row=3, column=2, columnspan=1, ipadx=1)

        button1 = tk.Button(master, text='Calculate', fg='black', bg='red',
                            command=lambda: self.calculate_probability(slot_num_var.get(), slot_acc_var.get(),
                                                                  slot_dmg_var.get()),
                            height=1, width=8)
        button1.grid(row=4, column=2)

    def plot(self, x, y):
        x = np.array(x)
        y = np.array(y)

        fig = Figure(figsize=(6, 6))
        a = fig.add_subplot(111)

        # a.scatter(x, y, color='red')
        width = 0.2
        a.bar(x, y, width)

        a.set_title("Damage Estimator", fontsize=16)
        a.set_ylabel("Probability", fontsize=14)
        a.set_xlabel("Damage", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().grid(row=5, column=5)
        canvas.draw()

    def calculate_probability(self, slot_num, slot_acc, total_dmg):
        try:
            slot_num = int(slot_num)
            slot_acc = float(slot_acc)
            total_dmg = int(total_dmg)

            dmg_list = []
            prob_list = []

            i = 0
            while i < slot_num + 1:
                probability = (slot_acc ** i) * ((1-slot_acc) ** (slot_num - i)) \
                              * math.factorial(slot_num) / (math.factorial(i) * math.factorial(slot_num-i))
                print("Damage " + str(i*total_dmg / slot_num) + " probability is :" + str(probability))
                dmg_list.append(i*total_dmg / slot_num)
                prob_list.append(probability)
                i += 1

            self.plot(dmg_list, prob_list)
        except TypeError:
            print("Please input integers")

        except ZeroDivisionError:
            print("Please input numbers greater than 0")

        return


if __name__ == '__main__':
    root = tk.Tk()
    gui = for_the_king_gui(root)
    root.mainloop()