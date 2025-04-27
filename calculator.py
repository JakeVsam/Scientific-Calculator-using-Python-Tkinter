from tkinter import *
import math
import Sci_Calculator

is_on = True


# main window
class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(0, 0)
        self.geometry("335x500")
        self.configure(bg='lavender')

        self.main_frame = Frame(width=335, height=565, bg="lavender")
        self.main_frame.pack()

# Output Field
        self.input_text = StringVar()
        self.input_text.set("0")
        self.memory_text = StringVar()
        self.memory_text.set("0")
        self.memory_stored = StringVar()

        self.input_frame = Frame(master=self.main_frame, width=330, height=230, bg="lavender")
        self.input_frame.pack(side=TOP)
        self.input_frame.pack_propagate(0)

# input field
        self.input_entry = Entry(master=self.input_frame, font=('arial', 20, 'bold'), textvariable=self.input_text,
                                 disabledbackground="ghost white", bd=0, disabledforeground="gray11",
                                 fg="red", justify=RIGHT, state=DISABLED)
        self.input_entry.insert(0, '0')
        self.input_entry.grid(row=0, column=0, columnspan=4, pady=1)
        self.input_entry.place(x=12, y=50, width=300, height=130)

# switch calculator
        self.switch = Button(self.input_frame, text="≡ Standard", width=6, height=1, relief=RAISED,
                             font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                             command=lambda: switch_calc())
        self.switch.pack()
        self.switch.place(x=10, y=10, width=100, height=30)

# Memory
        self.memory_frame_main = Frame(self.input_frame, width=310, height=30, bd=0, bg="lavender",
                                       highlightcolor="gray11",
                                       highlightthickness=0)
        self.memory_frame_main.pack(side=BOTTOM)

        self.memory_frame = Frame(self.memory_frame_main, width=310, height=20, bd=0, highlightbackground="lavender",
                                  highlightcolor="gray11",
                                  highlightthickness=0)
        self.memory_frame.pack(side=BOTTOM)

        self.memory_clear = Button(self.memory_frame, text="MC", width=4, height=1, relief=RAISED,
                                   font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                                   command=lambda: mem_clear(), state=DISABLED)
        self.memory_clear.grid(row=1, column=0, padx=1)

        self.memory_re = Button(self.memory_frame, text="MR", width=4, height=1, relief=RAISED,
                                font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                                command=lambda: mem_recall(), state=DISABLED)
        self.memory_re.grid(row=1, column=1, padx=1)

        self.memory_add = Button(self.memory_frame, text="M+", width=4, height=1, relief=RAISED,
                                 font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                                 command=lambda: mem_add())
        self.memory_add.grid(row=1, column=2, padx=1)

        self.memory_sub = Button(self.memory_frame, text="M-", width=4, height=1, relief=RAISED,
                                 font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                                 command=lambda: mem_sub())
        self.memory_sub.grid(row=1, column=3, padx=1)

        self.memory_store = Button(self.memory_frame, text="MS", width=4, height=1, relief=RAISED,
                                   font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                                   command=lambda: memory_store())
        self.memory_store.grid(row=1, column=4, padx=1)

        self.memory_show = Button(self.memory_frame, text="M↓", width=4, height=1, relief=RAISED,
                                  font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                                  command=lambda: mem_show())
        self.memory_show.grid(row=1, column=5, padx=1)

# Button frame

        self.btn_frame_main = Frame(self.main_frame, width=350, height=405, bg="lavender")
        self.btn_frame_main.pack(side=BOTTOM)

        self.btn_frame_center = Frame(self.btn_frame_main, width=350, height=405, bg="lavender")
        self.btn_frame_center.pack()

        self.btn_frame = Frame(self.btn_frame_center, width=350, height=405, bg="lavender")
        self.btn_frame.pack(side=BOTTOM)

# memory show frame
        self.memory_show_frame = Frame(self.btn_frame_main, width=350, height=370, bg="lavender")
        self.memory_show_frame.pack_forget()
        self.memory_show_frame.pack_propagate(0)

# memory entry
        self.memory_entry = Entry(self.memory_show_frame, font=('arial', 28, 'bold'), textvariable=self.memory_text,
                                  disabledbackground="ghost white", bd=0, disabledforeground="black", justify=RIGHT,
                                  state=DISABLED)
        self.memory_entry.insert(0, '0')
        self.memory_entry.grid(row=1, column=0, columnspan=4, pady=1)
        self.memory_entry.place(x=25, y=175, width=300, height=250)

# memory storing entry
        self.storem_entry = Entry(self.memory_show_frame, font=('arial', 28, 'bold'), textvariable=self.memory_stored,
                                  disabledbackground="ghost white", bd=0, disabledforeground="black", justify=RIGHT,
                                  state=DISABLED)
        self.storem_entry.insert(0, '0')
        self.storem_entry.grid(row=1, column=0, columnspan=4, pady=1)
        self.storem_entry.place(x=25, y=15, width=300, height=260)

# ----------------------------------------------------------------------------------------------------------------------
# arithmetic operators:~
# Basic
        self.plus = Button(self.btn_frame, text="+", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure3", cursor="hand2", command=lambda: plus_click())
        self.plus.grid(row=4, column=3, padx=1, pady=1)

        self.minus = Button(self.btn_frame, text="-", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="azure3", cursor="hand2", command=lambda: minus_click())
        self.minus.grid(row=3, column=3, padx=1, pady=1)

        self.multiply = Button(self.btn_frame, text="x", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                               fg="gray11", bg="azure3", cursor="hand2", command=lambda: multi_click())
        self.multiply.grid(row=2, column=3, padx=1, pady=1)

        self.divide = Button(self.btn_frame, text="÷", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                             fg="gray11", bg="azure3", cursor="hand2", command=lambda: div_click())
        self.divide.grid(row=1, column=3, padx=1, pady=1)

        self.point = Button(self.btn_frame, text=".", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="azure3", cursor="hand2", command=lambda: period_click())
        self.point.grid(row=5, column=2, padx=1, pady=1)

        self.equal = Button(self.btn_frame, text="=", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="azure3", cursor="hand2", command=lambda: equal_bt())
        self.equal.grid(row=5, column=3, padx=1, pady=1)

        self.mod = Button(self.btn_frame, text="%", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: btn_click("%"))
        self.mod.grid(row=0, column=0, padx=1, pady=1)

        self.sq_root = Button(self.btn_frame, text="√", width=5, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: func_sqrt())
        self.sq_root.grid(row=0, column=1, padx=1, pady=1)

        self.sq = Button(self.btn_frame, text="x²", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                         fg="gray11", bg="azure3", cursor="hand2", command=lambda: func_sq())
        self.sq.grid(row=0, column=2, padx=1, pady=1)

        self.plus_minus = Button(self.btn_frame, text="±", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                                 fg="gray11", bg="azure3", cursor="hand2", command=lambda: p_m())
        self.plus_minus.grid(row=5, column=0, padx=1, pady=1)

        self.one_x = Button(self.btn_frame, text="¹/x", width=5, height=1, relief=RAISED,
                            font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                            command=lambda: one_by_x())
        self.one_x.grid(row=0, column=3, padx=1, pady=1)
# ----------------------------------------------------------------------------------------------------------------------
        # Delete Buttons
        self.clear = Button(self.btn_frame, text="C", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="gray99", cursor="hand2", command=lambda: bt_clear())
        self.clear.grid(row=1, column=1, padx=1, pady=1)

        self.clear_entry = Button(self.btn_frame, text="CE", width=5, height=1, relief=RAISED,
                                  font=('arial', 15, "bold"), fg="gray11", bg="gray99", cursor="hand2",
                                  command=lambda: entry_clear())
        self.clear_entry.grid(row=1, column=0, padx=1, pady=1)

        self.backspace = Button(self.btn_frame, text="⌫", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                                fg="gray11", bg="gray99", cursor="hand2", command=lambda: func_backspace())
        self.backspace.grid(row=1, column=2, padx=1, pady=1)
# ---------------------------------------------------------------------------------------------------------------------
# number buttons

        self.num7 = Button(self.btn_frame, text="7", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: seven_click())
        self.num7.grid(row=2, column=0, padx=1, pady=1)

        self.num8 = Button(self.btn_frame, text="8", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: eight_click())
        self.num8.grid(row=2, column=1, padx=1, pady=1)

        self.num9 = Button(self.btn_frame, text="9", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: nine_click())
        self.num9.grid(row=2, column=2, padx=1, pady=1)

        self.num4 = Button(self.btn_frame, text="4", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: four_click())
        self.num4.grid(row=3, column=0, padx=1, pady=1)

        self.num5 = Button(self.btn_frame, text="5", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: five_click())
        self.num5.grid(row=3, column=1, padx=1, pady=1)

        self.num6 = Button(self.btn_frame, text="6", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: six_click())
        self.num6.grid(row=3, column=2, padx=1, pady=1)

        self.num1 = Button(self.btn_frame, text="1", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: one_click())
        self.num1.grid(row=4, column=0, padx=1, pady=1)

        self.num2 = Button(self.btn_frame, text="2", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: two_click())
        self.num2.grid(row=4, column=1, padx=1, pady=1)

        self.num3 = Button(self.btn_frame, text="3", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: three_click())
        self.num3.grid(row=4, column=2, padx=1, pady=1)

        self.num0 = Button(self.btn_frame, text="0", width=5, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: zero_click())
        self.num0.grid(row=5, column=1, padx=1, pady=1)

# ----------------------------------------------------------------------------------------------------------------------
# Functions
        def btn_click(item):
            global expression
            expression = expression + str(item)
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def one_click():
            global expression
            expression = expression + "1"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def two_click():
            global expression
            expression = expression + "2"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def three_click():
            global expression
            expression = expression + "3"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def four_click():
            global expression
            expression = expression + "4"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def five_click():
            global expression
            expression = expression + "5"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def six_click():
            global expression
            expression = expression + "6"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def seven_click():
            global expression
            expression = expression + "7"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def eight_click():
            global expression
            expression = expression + "8"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def nine_click():
            global expression
            expression = expression + "9"
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def zero_click():
            global expression
            expression = expression + "0"
            self.input_text.set(expression)

# ---------------------------------------------------------------------------------------------------------------------
        def plus_click():
            global expression
            expression = expression + "+"
            self.input_text.set(expression)

# ---------------------------------------------------------------------------------------------------------------------
        def minus_click():
            global expression
            expression = expression + "-"
            self.input_text.set(expression)

# ---------------------------------------------------------------------------------------------------------------------
        def multi_click():
            global expression
            expression = expression + "x"
            self.input_text.set(expression)

# ---------------------------------------------------------------------------------------------------------------------
        def div_click():
            global expression
            expression = expression + "÷"
            self.input_text.set(expression)

# ---------------------------------------------------------------------------------------------------------------------
        def period_click():
            global expression
            expression = expression + "."
            self.input_text.set(expression)

# ---------------------------------------------------------------------------------------------------------------------

        def bt_clear():
            global expression
            expression = ""
            self.input_text.set("")

# ----------------------------------------------------------------------------------------------------------------------
#        def bt_equal():
#            global expression
#            result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
#            self.input_text.set(result)
#            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def equal_bt():
            global expression
            got = self.input_text.get()

            if "x" in got:
                expression = got.replace("x", "*")
                if "÷" in got:
                    expression = expression.replace("÷", "/")

            if "÷" in got:
                expression = got.replace("÷", "/")
                if "x" in got:
                    expression = expression.replace("x", "*")

            result = str(eval(expression))
            self.input_text.set(result)

            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def entry_clear():
            global expression
            for i, c in enumerate(expression[::-1]):  # reverse string
                if c in ['+', '-', '/', '*', '%', '**', '.e+']:  # find first operator
                    expression = expression[:-i - 1]  # truncate string
                    break
            else:
                expression = ""  # no operator found
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def func_backspace():
            global expression
            expression = expression[:-1]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def mem_add():
            self.memory_clear.config(state=NORMAL)
            self.memory_re.config(state=NORMAL)
            global memory
            mem1 = self.input_text.get()
            mem2 = self.memory_text.get()
            num1 = int(mem1)
            num2 = int(mem2)
            add = num1 + num2
            ans = str(add)
            self.memory_text.set(ans)

        def mem_sub():
            self.memory_clear.config(state=NORMAL)
            self.memory_re.config(state=NORMAL)
            global memory
            mem1 = self.input_text.get()
            mem2 = self.memory_text.get()
            num1 = int(mem1)
            num2 = int(mem2)
            sub = num2 - num1
            ans = str(sub)
            self.memory_text.set(ans)

        def mem_clear():
            self.memory_text.set("0")
            self.memory_stored.set("")

        def mem_recall():
            global memory
            memory = self.memory_text.get()
            self.input_text.set(memory)

        def mem_show():
            global is_on

            if is_on:
                self.btn_frame_center.pack_forget()
                self.memory_show_frame.pack()
                self.memory_add.config(state=DISABLED)
                self.memory_sub.config(state=DISABLED)
                self.memory_re.config(state=DISABLED)
                self.memory_clear.config(state=DISABLED)
                self.input_text.set(memory)
                is_on = False

            else:
                self.memory_show_frame.pack_forget()
                self.btn_frame_center.pack()
                bt_clear()
                self.memory_add.config(state=NORMAL)
                self.memory_sub.config(state=NORMAL)
                self.memory_re.config(state=NORMAL)
                self.memory_clear.config(state=NORMAL)
                is_on = True

        def memory_store():
            stored_mem = self.input_text.get()
            self.memory_stored.set(stored_mem)

# ----------------------------------------------------------------------------------------------------------------------
        def func_sq():
            global expression
            got = self.input_text.get()
            num_sq = int(got)
            expression = str(num_sq ** 2)
            self.input_text.set(expression)

# --------------------------------------------------------------------------------------------------------------------
        def func_sqrt():
            global expression
            int_rt = int(expression)
            str_rt = math.sqrt(int_rt)
            expression = str(str_rt)
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def one_by_x():
            global expression
            x = int(expression)
            int_x = 1 / x
            expression = str(int_x)
            self.input_text.set(expression)

# --------------------------------------------------------------------------------------------------------------------
        def p_m():
            global expression
            global is_on
            int_num = int(expression)

            if is_on:
                pos = abs(int_num)
                expression = str(pos)
                self.input_text.set(expression)
                is_on = False

            else:
                neg = -abs(int_num)
                expression = str(neg)
                self.input_text.set(expression)
                is_on = True

# ----------------------------------------------------------------------------------------------------------------------
        def switch_calc():
            Calculator.destroy(self)
            Sci_Calculator.ScientificCalculator()

# ----------------------------------------------------------------------------------------------------------------------


expression = ""
memory = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
