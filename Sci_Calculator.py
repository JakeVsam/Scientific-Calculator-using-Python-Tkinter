#RUN calculator.py

from tkinter import *
import math
from calculator import Calculator

is_on = True
num = 1


class ScientificCalculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("350x565")
        self.resizable(0, 0)
        self.config(bg="lavender")

        self.main_frame = Frame(width=350, height=565, bg="lavender")
        self.main_frame.pack()

        self.input_frame = Frame(master=self.main_frame, width=330, height=235, bg="lavender")
        self.input_frame.pack(side=TOP)
        self.input_frame.pack_propagate(0)

        self.input_text = StringVar()
        self.input_text.set("0")
        self.memory_text = StringVar()
        self.memory_text.set("0")
        self.memory_stored = StringVar()

        self.input_entry = Entry(master=self.input_frame, font=('arial', 20, 'bold'), textvariable=self.input_text,
                                 disabledbackground="ghost white", bd=0, disabledforeground="gray11",
                                 fg="red", justify=RIGHT, state=DISABLED)
        self.input_entry.insert(0, '0')
        self.input_entry.grid(row=0, column=0, columnspan=4, pady=1)
        self.input_entry.place(x=12, y=50, width=300, height=145)

# switch calculator
        self.switch = Button(self.input_frame, text="≡ Scientific", width=6, height=1, relief=RAISED,
                             font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                             command=lambda: switch_calc())
        self.switch.pack()
        self.switch.place(x=10, y=10, width=100, height=30)

        self.memory_frame_main = Frame(self.input_frame, width=310, height=100, bd=0, bg="lavender",
                                       highlightcolor="gray11",
                                       highlightthickness=0)
        self.memory_frame_main.pack(side=BOTTOM)

        self.memory_frame = Frame(self.memory_frame_main, width=310, height=50, bd=0, highlightbackground="lavender",
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

        self.btn_frame_main = Frame(self.main_frame, width=430, height=370, bg="lavender")
        self.btn_frame_main.pack(side=BOTTOM)

        self.btn_frame_center = Frame(self.btn_frame_main, width=430, height=370, bg="lavender")
        self.btn_frame_center.pack()

        self.btn_frame = Frame(self.btn_frame_center, width=430, height=370, bg="lavender")
        self.btn_frame.pack(side=BOTTOM)

        self.btn_frame_hide = Frame(self.btn_frame_center, width=430, height=70, bg="lavender")
        self.btn_frame_hide.pack(side=TOP)

        self.btn_frame_reveal = Frame(self.btn_frame_center, width=430, height=70, bg="lavender")
        self.btn_frame_reveal.pack_forget()

# memory show frame
        self.memory_show_frame = Frame(self.btn_frame_main, width=430, height=370, bg="lavender")
        self.memory_show_frame.pack_forget()
        self.memory_show_frame.pack_propagate(0)

# memory entry
        self.memory_entry = Entry(self.memory_show_frame, font=('arial', 28, 'bold'), textvariable=self.memory_text,
                                  disabledbackground="ghost white", bd=0, disabledforeground="black", justify=RIGHT,
                                  state=DISABLED)
        self.memory_entry.insert(0, '0')
        self.memory_entry.grid(row=1, column=0, columnspan=4, pady=1)
        self.memory_entry.place(x=25, y=175, width=300, height=150)

# memory storing entry
        self.storem_entry = Entry(self.memory_show_frame, font=('arial', 28, 'bold'), textvariable=self.memory_stored,
                                  disabledbackground="ghost white", bd=0, disabledforeground="black", justify=RIGHT,
                                  state=DISABLED)
        self.storem_entry.insert(0, '0')
        self.storem_entry.grid(row=1, column=0, columnspan=4, pady=1)
        self.storem_entry.place(x=25, y=15, width=300, height=160)
# ----------------------------------------------------------------------------------------------------------------------
        self.advanced_frame = Frame(self.memory_frame_main, width=330, height=50, bd=0, bg="lavender",
                                    highlightthickness=0)
        self.advanced_frame.pack(side=TOP)

        self.deg = Button(self.advanced_frame, text="DEG", width=4, height=1, relief=RAISED,
                          font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                          command=lambda: triple_switch())
        self.deg.grid(row=0, column=0)

        self.rad = Button(self.advanced_frame, text="RAD", width=4, height=1, relief=RAISED,
                          font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                          command=lambda: triple_switch())
        self.rad.grid_forget()

        self.grad = Button(self.advanced_frame, text="GRAD", width=4, height=1, relief=RAISED,
                           font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                           command=lambda: triple_switch())
        self.grad.grid_forget()

        self.hyp = Button(self.advanced_frame, text="HYP", width=4, height=1, relief=RAISED,
                          font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                          command=lambda: func_hyp())
        self.hyp.grid(row=0, column=1)

        self.fe = Button(self.advanced_frame, text="F- E", width=4, height=1, relief=RAISED,
                         font=('arial', 13, "bold"), fg="gray11", bg="lavender", cursor="hand2",
                         command=lambda: fe())
        self.fe.grid(row=0, column=2)
# ----------------------------------------------------------------------------------------------------------------------
    # arithmetic operators:~
    # Basic
        self.plus = Button(self.btn_frame, text="+", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure3", cursor="hand2", command=lambda: plus_click())
        self.plus.grid(row=5, column=4, padx=1, pady=1)

        self.minus = Button(self.btn_frame, text="-", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="azure3", cursor="hand2", command=lambda: minus_click())
        self.minus.grid(row=4, column=4, padx=1, pady=1)

        self.multiply = Button(self.btn_frame, text="x", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                               fg="gray11", bg="azure3", cursor="hand2", command=lambda: multi_click())
        self.multiply.grid(row=3, column=4, padx=1, pady=1)

        self.divide = Button(self.btn_frame, text="÷", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                             fg="gray11", bg="azure3", cursor="hand2", command=lambda: div_click())
        self.divide.grid(row=2, column=4, padx=1, pady=1)

        self.point = Button(self.btn_frame, text=".", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="azure3", cursor="hand2", command=lambda: period_click())
        self.point.grid(row=6, column=3, padx=1, pady=1)

        self.equal = Button(self.btn_frame, text="=", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="azure3", cursor="hand2", command=lambda: bt_equal())
        self.equal.grid(row=6, column=4, padx=1, pady=1)

        self.equal_2 = Button(self.btn_frame, text="=", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                              fg="gray11", bg="azure3", cursor="hand2", command=lambda: y_root_x())
        self.equal_2.grid(row=6, column=4, padx=1, pady=1)
        self.equal_2.grid_forget()

        self.equal_3 = Button(self.btn_frame, text="=", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                              fg="gray11", bg="azure3", cursor="hand2", command=lambda: exp_func())
        self.equal_3.grid(row=6, column=4, padx=1, pady=1)
        self.equal_3.grid_forget()
# --------------------------------------------------------------------------------------------------------------------
# Delete Buttons
        self.clear = Button(self.btn_frame, text="C", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                            fg="gray11", bg="gray99", cursor="hand2", command=lambda: bt_clear())
        self.clear.grid(row=2, column=2, padx=1, pady=1)

        self.clear_entry = Button(self.btn_frame, text="CE", width=4, height=1, relief=RAISED,
                                  font=('arial', 15, "bold"), fg="gray11", bg="gray99", cursor="hand2",
                                  command=lambda: entry_clear())
        self.clear_entry.grid(row=2, column=1, padx=1, pady=1)

        self.backspace = Button(self.btn_frame, text="⌫", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                                fg="gray11", bg="gray99", cursor="hand2", command=lambda: func_backspace())
        self.backspace.grid(row=2, column=3, padx=1, pady=1)
# ---------------------------------------------------------------------------------------------------------------------
# Additional math:~
# Brackets:
        self.rbl = Button(self.btn_frame, text="(", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: btn_click("("))
        self.rbl.grid(row=6, column=0, padx=1, pady=1)

        self.rbr = Button(self.btn_frame, text=")", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: btn_click(")"))
        self.rbr.grid(row=6, column=1, padx=1, pady=1)

# ----------------------------------------------------------------------------------------------------------------------
        # Advanced:
        self.exp = Button(self.btn_frame_hide, text="Exp", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: func_exp())
        self.exp.grid(row=1, column=3, padx=1, pady=1)

        self.mod = Button(self.btn_frame_hide, text="Mod", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: btn_click("%"))
        self.mod.grid(row=1, column=4, padx=1, pady=1)

        self.log = Button(self.btn_frame_hide, text="log", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: numb_log())
        self.log.grid(row=1, column=2, padx=1, pady=1)

        self.pi = Button(self.btn_frame, text="π", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                         fg="gray11", bg="azure3", cursor="hand2", command=lambda: numb_pi())
        self.pi.grid(row=3, column=0, padx=1, pady=1)

        self.sin = Button(self.btn_frame_hide, text="sin", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: numb_sin_deg())
        self.sin.grid(row=0, column=2, padx=1, pady=1)

        self.cos = Button(self.btn_frame_hide, text="cos", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: numb_cos_deg())
        self.cos.grid(row=0, column=3, padx=1, pady=1)

        self.tan = Button(self.btn_frame_hide, text="tan", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: numb_tan_deg())
        self.tan.grid(row=0, column=4, padx=1, pady=1)

        self.sq_root = Button(self.btn_frame_hide, text="√", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: func_sqrt())
        self.sq_root.grid(row=1, column=0, padx=1, pady=1)

        self.sq = Button(self.btn_frame_hide, text="x²", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                         fg="gray11", bg="azure3", cursor="hand2", command=lambda: func_sq())
        self.sq.grid(row=0, column=0, padx=1, pady=1)

        self.power = Button(self.btn_frame_hide, text="xʸ", width=4, height=1, relief=RAISED,
                            font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                            command=lambda: btn_click("**"))
        self.power.grid(row=0, column=1, padx=1, pady=1)

        self.up_arrow = Button(self.btn_frame, text="↑", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                               fg="gray11", bg="azure3", cursor="hand2", command=lambda: switch())
        self.up_arrow.grid(row=2, column=0, padx=1, pady=1)

        self.plus_minus = Button(self.btn_frame, text="±", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                                 fg="gray11", bg="azure3", cursor="hand2", command=lambda: p_m())
        self.plus_minus.grid(row=5, column=0, padx=1, pady=1)

        self.ten = Button(self.btn_frame_hide, text="10ˣ", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                          fg="gray11", bg="azure3", cursor="hand2", command=lambda: ten_power())
        self.ten.grid(row=1, column=1, padx=1, pady=1)

        self.fact = Button(self.btn_frame, text="n!", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure3", cursor="hand2", command=lambda: func_fact())
        self.fact.grid(row=4, column=0, padx=1, pady=1)

# --------------------------------------------list 2------------------------------------------------------------------
        self.e = Button(self.btn_frame_reveal, text="eˣ", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                        fg="gray11", bg="azure3", cursor="hand2", command=lambda: e_power())
        self.e.grid(row=1, column=1, padx=1, pady=1)

        self.cube = Button(self.btn_frame_reveal, text="x³", width=4, height=1, relief=RAISED,
                           font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                           command=lambda: func_cube())
        self.cube.grid(row=0, column=0, padx=1, pady=1)

        self.y_x = Button(self.btn_frame_reveal, text="ʸ√x", width=4, height=1, relief=RAISED,
                          font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                          command=lambda: get_y())
        self.y_x.grid(row=0, column=1, padx=1, pady=1)

        self.one_x = Button(self.btn_frame_reveal, text="¹/x", width=4, height=1, relief=RAISED,
                            font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                            command=lambda: one_by_x())
        self.one_x.grid(row=1, column=0, padx=1, pady=1)

        self.ln = Button(self.btn_frame_reveal, text="ln", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                         fg="gray11", bg="azure3", cursor="hand2", command=lambda: numb_ln())
        self.ln.grid(row=1, column=2, padx=1, pady=1)

        self.dms = Button(self.btn_frame_reveal, text="dms", width=4, height=1, relief=RAISED,
                          font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                          command=lambda: func_dms())
        self.dms.grid(row=1, column=3, padx=1, pady=1)

        self.deg = Button(self.btn_frame_reveal, text="deg", width=4, height=1, relief=RAISED,
                          font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                          command=lambda: func_dd())
        self.deg.grid(row=1, column=4, padx=1, pady=1)

        self.sin_inv = Button(self.btn_frame_reveal, text="sin⁻¹", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: numb_sin_inv_deg())
        self.sin_inv.grid(row=0, column=2, padx=1, pady=1)

        self.cos_inv = Button(self.btn_frame_reveal, text="cos⁻¹", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: numb_cos_inv_deg())
        self.cos_inv.grid(row=0, column=3, padx=1, pady=1)

        self.tan_inv = Button(self.btn_frame_reveal, text="tan⁻¹", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: numb_tan_inv_deg())
        self.tan_inv.grid(row=0, column=4, padx=1, pady=1)
# ----------------------------------------------------------------------------------------------------------------------
# Hyp buttons:~
        self.sin_h = Button(self.btn_frame_hide, text="sinh", width=4, height=1, relief=RAISED,
                            font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                            command=lambda: numb_sin_h())
        self.sin_h.grid_forget()

        self.cos_h = Button(self.btn_frame_hide, text="cosh", width=4, height=1, relief=RAISED,
                            font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                            command=lambda: numb_cos_h())
        self.cos_h.grid_forget()

        self.tan_h = Button(self.btn_frame_hide, text="tanh", width=4, height=1, relief=RAISED,
                            font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                            command=lambda: numb_tan_h())
        self.tan_h.grid_forget()

        self.sin_h_inv = Button(self.btn_frame_reveal, text="sinh⁻¹", width=4, height=1, relief=RAISED,
                                font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                command=lambda: numb_sin_h_inv())
        self.sin_h_inv.grid_forget()

        self.cos_h_inv = Button(self.btn_frame_reveal, text="cosh⁻¹", width=4, height=1, relief=RAISED,
                                font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                command=lambda: numb_cos_h_inv())
        self.cos_h_inv.grid_forget()

        self.tan_h_inv = Button(self.btn_frame_reveal, text="tanh⁻¹", width=4, height=1, relief=RAISED,
                                font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                command=lambda: numb_tan_h_inv())
        self.tan_h_inv.grid_forget()
# ----------------------------------------------------------------------------------------------------------------------
# rad variants trigonometry
        self.sin_rad = Button(self.btn_frame_hide, text="sin", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: numb_sin_rad())
        self.sin_rad.grid_forget()

        self.cos_rad = Button(self.btn_frame_hide, text="cos", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: numb_cos_rad())
        self.cos_rad.grid_forget()

        self.tan_rad = Button(self.btn_frame_hide, text="tan", width=4, height=1, relief=RAISED,
                              font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                              command=lambda: numb_tan_rad())
        self.tan_rad.grid_forget()

        self.sin_inv_rad = Button(self.btn_frame_reveal, text="sin⁻¹", width=4, height=1, relief=RAISED,
                                  font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                  command=lambda: numb_sin_inv_rad())
        self.sin_inv_rad.grid_forget()

        self.cos_inv_rad = Button(self.btn_frame_reveal, text="cos⁻¹", width=4, height=1, relief=RAISED,
                                  font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                  command=lambda: numb_cos_inv_rad())
        self.cos_inv_rad.grid_forget()

        self.tan_inv_rad = Button(self.btn_frame_reveal, text="tan⁻¹", width=4, height=1, relief=RAISED,
                                  font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                  command=lambda: numb_tan_inv_rad())
        self.tan_inv_rad.grid_forget()

# ----------------------------------------------------------------------------------------------------------------------
# grad variants trigonometry
        self.sin_grad = Button(self.btn_frame_hide, text="sin", width=4, height=1, relief=RAISED,
                               font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                               command=lambda: numb_sin_rad())
        self.sin_grad.grid_forget()

        self.cos_grad = Button(self.btn_frame_hide, text="cos", width=4, height=1, relief=RAISED,
                               font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                               command=lambda: numb_cos_grad())
        self.cos_grad.grid_forget()

        self.tan_grad = Button(self.btn_frame_hide, text="tan", width=4, height=1, relief=RAISED,
                               font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                               command=lambda: numb_tan_rad())
        self.tan_grad.grid_forget()

        self.sin_inv_grad = Button(self.btn_frame_reveal, text="sin⁻¹", width=4, height=1, relief=RAISED,
                                   font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                   command=lambda: numb_sin_inv_rad())
        self.sin_inv_grad.grid_forget()

        self.cos_inv_grad = Button(self.btn_frame_reveal, text="cos⁻¹", width=4, height=1, relief=RAISED,
                                   font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                   command=lambda: numb_cos_inv_rad())
        self.cos_inv_grad.grid_forget()

        self.tan_inv_grad = Button(self.btn_frame_reveal, text="tan⁻¹", width=4, height=1, relief=RAISED,
                                   font=('arial', 15, "bold"), fg="gray11", bg="azure3", cursor="hand2",
                                   command=lambda: numb_tan_inv_rad())
        self.tan_inv_grad.grid_forget()

# ----------------------------------------------------------------------------------------------------------------------
# number buttons

        self.num7 = Button(self.btn_frame, text="7", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: seven_click())
        self.num7.grid(row=3, column=1, padx=1, pady=1)

        self.num8 = Button(self.btn_frame, text="8", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: eight_click())
        self.num8.grid(row=3, column=2, padx=1, pady=1)

        self.num9 = Button(self.btn_frame, text="9", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: nine_click())
        self.num9.grid(row=3, column=3, padx=1, pady=1)

        self.num4 = Button(self.btn_frame, text="4", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: four_click())
        self.num4.grid(row=4, column=1, padx=1, pady=1)

        self.num5 = Button(self.btn_frame, text="5", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: five_click())
        self.num5.grid(row=4, column=2, padx=1, pady=1)

        self.num6 = Button(self.btn_frame, text="6", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: six_click())
        self.num6.grid(row=4, column=3, padx=1, pady=1)

        self.num1 = Button(self.btn_frame, text="1", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: one_click())
        self.num1.grid(row=5, column=1, padx=1, pady=1)

        self.num2 = Button(self.btn_frame, text="2", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: two_click())
        self.num2.grid(row=5, column=2, padx=1, pady=1)

        self.num3 = Button(self.btn_frame, text="3", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: three_click())
        self.num3.grid(row=5, column=3, padx=1, pady=1)

        self.num0 = Button(self.btn_frame, text="0", width=4, height=1, relief=RAISED, font=('arial', 15, "bold"),
                           fg="gray11", bg="azure", cursor="hand2", command=lambda: zero_click())
        self.num0.grid(row=6, column=2, padx=1, pady=1)

# ====================================================================================================================

        def get_y():
            btn_click("√")
            self.equal.grid_forget()
            self.equal_2.grid(row=6, column=4, padx=1, pady=1)

        def y_root_x():
            global expression

            got = self.input_text.get()
            index_root = got.index("√")
            num_1 = got[:index_root]
            num_2 = got[index_root + 1:]

            y = int(num_1)
            x = int(num_2)

            root = y ** (1 / x)

            expression = str(root)
            self.input_text.set(expression)

            self.equal_2.grid_forget()
            self.equal.grid(row=6, column=4, padx=1, pady=1)

# ----------------------------------------------------------------------------------------------------------------------
# Toggle Function

        def switch():
            global is_on

            if is_on:
                self.up_arrow.config(bg="turquoise", fg="gray11")
                self.btn_frame_hide.pack_forget()
                self.btn_frame_reveal.pack(side=TOP)
                is_on = False

            else:
                self.up_arrow.config(bg="azure3", fg="gray11")
                self.btn_frame_reveal.pack_forget()
                self.btn_frame_hide.pack(side=TOP)
                is_on = True

# ----------------------------------------------------------------------------------------------------------------------
        # text size edit function
#        def font_change():
#            global expression
#            expression = self.input_text.get()
#            if len(expression) > 9:
#                self.input_field.config(font=('arial', 16, 'bold'))

# ----------------------------------------------------------------------------------------------------------------------
# Operation Functions
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
            self.input_text.set("0")
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
        def bt_equal():
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
        def numb_pi():
            num_pi = str(math.pi)
            global expression
            expression = expression + num_pi[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def func_dms():
            global expression
            if len(expression) > 4 and '.' in expression:
                dd = float(expression)
                mnt, sec = divmod(dd * 3600, 60)
                degree, mnt = divmod(mnt, 60)
                ans = f'{degree}° {mnt}\' {sec}\"'
                #    tup = (degree, mnt, sec)
                self.input_text.set(ans)
                expression = ""

            else:
                self.input_text.set("invalid input")
                expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def func_dd():  # dd = degrees + (min/60) + (sec/3600) # Ex: 77.3453 = 77deg + 20' + 43.0799"
            global expression

            got = self.input_text.get()
            deg_index = got.index("°")
            mnt_index = got.index("'")
            sec_index = got.index('"')

            if '°' in got:
                degree = got[:deg_index]
                if "'" in got:
                    mnt = got[deg_index + 1:mnt_index]
                    if '"' in got:
                        sec = got[mnt_index + 1:sec_index]

                        num_deg = float(degree)
                        num_mnt = float(mnt)
                        num_sec = float(sec)

                        ans = num_deg + (num_mnt / 60) + (num_sec / 3600)
                        expression = str(ans)
                        self.input_text.set(expression)
            else:
                self.input_text.set("Invalid Input")

# ----------------------------------------------------------------------------------------------------------------------
        def numb_ln():
            global expression
            flt_exp = float(expression)
            num_log = math.log(flt_exp)
            str_log = str(num_log)
            expression = str_log[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_log():
            global expression
            flt_exp = float(expression)
            num_log = math.log(flt_exp, 10)
            str_log = str(num_log)
            expression = str_log[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def func_fact():
            global expression
            int_fact = int(expression)
            fac = math.factorial(int_fact)
            expression = str(fac)
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_rad():
            global expression
            int_cos = int(expression)
            num_cos = math.cos(int_cos)
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_deg():
            global expression
            int_cos = int(expression)
            num_cos = math.cos(math.radians(int_cos))
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_grad():
            global expression
            int_cos = int(expression)
            num_cos = math.cos(math.radians(int_cos))
            num_cos = num_cos * 1.111111
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_h():
            global expression
            int_cos = int(expression)
            num_cos = math.cosh(int_cos)
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_inv_rad():
            global expression
            int_cos = int(expression)
            num_cos = math.acos(int_cos)
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_inv_deg():
            global expression
            int_cos = int(expression)
            num_cos = math.acos(math.radians(int_cos))
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_cos_h_inv():
            global expression
            int_cos = int(expression)
            num_cos = math.acosh(int_cos)
            str_cos = str(num_cos)
            expression = str_cos[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_sin_rad():
            global expression
            int_sin = int(expression)
            num_sin = math.sin(int_sin)
            str_sin = str(num_sin)
            expression = str_sin[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_sin_deg():
            global expression
            int_sin = int(expression)
            num_sin = math.sin(math.radians(int_sin))
            str_sin = str(num_sin)
            expression = str_sin[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_sin_h():
            global expression
            int_sin = int(expression)
            num_sin = math.sinh(int_sin)
            str_sin = str(num_sin)
            expression = str_sin[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_sin_inv_rad():
            global expression
            int_sin = int(expression)
            num_sin = math.asin(int_sin)
            str_sin = str(num_sin)
            expression = str_sin[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_sin_inv_deg():
            global expression
            int_sin = int(expression)
            num_sin = math.asin(math.radians(int_sin))
            str_sin = str(num_sin)
            expression = str_sin[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_sin_h_inv():
            global expression
            int_sin = int(expression)
            num_sin = math.asinh(int_sin)
            str_sin = str(num_sin)
            expression = str_sin[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_tan_rad():
            global expression
            int_tan = int(expression)
            num_tan = math.tan(int_tan)
            str_tan = str(num_tan)
            expression = str_tan[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_tan_deg():
            global expression
            int_tan = int(expression)
            num_tan = math.tan(math.radians(int_tan))
            str_tan = str(num_tan)
            expression = str_tan[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_tan_h():
            global expression
            int_tan = int(expression)
            num_tan = math.tanh(int_tan)
            str_tan = str(num_tan)
            expression = expression + str_tan[:8]
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def numb_tan_inv_rad():
            global expression
            int_tan = int(expression)
            num_tan = math.atan(int_tan)
            str_tan = str(num_tan)
            expression = str_tan[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_tan_inv_deg():
            global expression
            int_tan = int(expression)
            num_tan = math.atan(math.radians(int_tan))
            str_tan = str(num_tan)
            expression = str_tan[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def numb_tan_h_inv():
            global expression
            int_tan = int(expression)
            num_tan = math.atanh(int_tan)
            str_tan = str(num_tan)
            expression = str_tan[:8]
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def func_sq():
            global expression
            num_sq = int(expression)
            expression = str(num_sq ** 2)
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def func_cube():
            global expression
            num_cube = int(expression)
            expression = str(num_cube ** 3)
            self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------------------------------------------
        def func_exp():
            global expression

            numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            got = self.input_text.get()
            expression = f'{got}.e+'

            self.equal.grid_forget()
            self.equal_3.grid(row=6, column=4, padx=1, pady=1)
            if got in numbs:
                self.input_text.set(expression)

# ----------------------------------------------------------------------------------------------------------------------
        def exp_func():
            global expression
            got = self.input_text.get()
            num_1 = got[0]
            last_num = got[-1]
            num_l = int(last_num)
            mid_num = got[2:-3]

            if len(mid_num) < num_l:
                extra = num_l - len(mid_num)
                for zero in range(extra):
                    mid_num = mid_num + "0"
                    self.input_text.set(f'{num_1}{mid_num}')

            self.equal_3.grid_forget()
            self.equal.grid(row=6, column=4, padx=1, pady=1)

            expression = ''

# ----------------------------------------------------------------------------------------------------------------------
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
        def ten_power():
            global expression
            got = self.input_text.get()
            int_got = int(got)
            ans = 10 ** int_got
            expression = str(ans)
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------
        def e_power():
            global expression
            num_e = 2.718281828459045
            got = self.input_text.get()
            int_e = int(got)

            ans = num_e ** int_e
            expression = str(ans)
            self.input_text.set(expression)
            expression = ""

# ----------------------------------------------------------------------------------------------------------------------

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Memory Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        def fe():
            global is_on
            got = self.input_text.get()

            if is_on:
                self.fe.config(fg="turquoise")
                num_1 = got[0]
                num_last = len(got) - 1
                mid_num = got[1:]
                while "0" in mid_num[-1]:
                    mid_num = mid_num.rstrip(mid_num[-1])
                    self.input_text.set(f"{num_1}.{mid_num}e+{num_last}")
                    if mid_num == "":
                        break
                else:
                    self.input_text.set(f"{num_1}.{mid_num}e+{num_last}")

                is_on = False

            else:
                self.fe.config(fg="gray11")
                num_1 = got[0]
                last_num = got[-1]
                num_l = int(last_num)
                mid_num = got[2:-3]

                if len(mid_num) < num_l:
                    extra = num_l - len(mid_num)
                    for zero in range(extra):
                        mid_num = mid_num + "0"

                        self.input_text.set(f'{num_1}{mid_num}')

                elif len(mid_num) == num_l:
                    self.input_text.set(f'{num_1}{mid_num}')

                is_on = True

# ----------------------------------------------------------------------------------------------------------------------
        def func_hyp():
            global is_on

            if is_on:
                self.hyp.config(fg="turquoise")
                self.sin.grid_forget()
                self.sin_h.grid(row=0, column=2, padx=1, pady=1)
                self.cos.grid_forget()
                self.cos_h.grid(row=0, column=3, padx=1, pady=1)
                self.tan.grid_forget()
                self.tan_h.grid(row=0, column=4, padx=1, pady=1)
                self.sin_inv.grid_forget()
                self.sin_h_inv.grid(row=0, column=2, padx=1, pady=1)
                self.cos_inv.grid_forget()
                self.cos_h_inv.grid(row=0, column=3, padx=1, pady=1)
                self.tan_inv.grid_forget()
                self.tan_h_inv.grid(row=0, column=4, padx=1, pady=1)
                is_on = False
            else:
                self.hyp.config(fg="gray11")
                self.sin_h.grid_forget()
                self.sin.grid(row=0, column=2, padx=1, pady=1)
                self.cos_h.grid_forget()
                self.cos.grid(row=0, column=3, padx=1, pady=1)
                self.tan_h.grid_forget()
                self.tan.grid(row=0, column=4, padx=1, pady=1)
                self.sin_h_inv.grid_forget()
                self.sin_inv.grid(row=0, column=2, padx=1, pady=1)
                self.cos_h_inv.grid_forget()
                self.cos_inv.grid(row=0, column=3, padx=1, pady=1)
                self.tan_h_inv.grid_forget()
                self.tan_inv.grid(row=0, column=4, padx=1, pady=1)
                is_on = True

# ----------------------------------------------------------------------------------------------------------------------
        def triple_switch():
            global num

            if num == 1:
                self.deg.grid_forget()
                self.rad.grid(row=0, column=0)

                self.sin.grid_forget()
                self.sin_rad.grid(row=0, column=2, padx=1, pady=1)
                self.cos.grid_forget()
                self.cos_rad.grid(row=0, column=3, padx=1, pady=1)
                self.tan.grid_forget()
                self.tan_rad.grid(row=0, column=4, padx=1, pady=1)
                self.sin_inv.grid_forget()
                self.sin_inv_rad.grid(row=0, column=2, padx=1, pady=1)
                self.cos_inv.grid_forget()
                self.cos_inv_rad.grid(row=0, column=3, padx=1, pady=1)
                self.tan_inv.grid_forget()
                self.tan_inv_rad.grid(row=0, column=4, padx=1, pady=1)
                num = 2
            elif num == 2:
                self.rad.grid_forget()
                self.grad.grid(row=0, column=0)

                self.sin_rad.grid_forget()
                self.sin_grad.grid(row=0, column=2, padx=1, pady=1)
                self.cos_rad.grid_forget()
                self.cos_grad.grid(row=0, column=3, padx=1, pady=1)
                self.tan_rad.grid_forget()
                self.tan_grad.grid(row=0, column=4, padx=1, pady=1)
                self.sin_inv_rad.grid_forget()
                self.sin_inv_grad.grid(row=0, column=2, padx=1, pady=1)
                self.cos_inv_rad.grid_forget()
                self.cos_inv_grad.grid(row=0, column=3, padx=1, pady=1)
                self.tan_inv_rad.grid_forget()
                self.tan_inv_grad.grid(row=0, column=4, padx=1, pady=1)
                num = 3
            else:
                self.grad.grid_forget()
                self.deg.grid(row=0, column=0)

                self.sin_grad.grid_forget()
                self.sin.grid(row=0, column=2, padx=1, pady=1)
                self.cos_grad.grid_forget()
                self.cos.grid(row=0, column=3, padx=1, pady=1)
                self.tan_grad.grid_forget()
                self.tan.grid(row=0, column=4, padx=1, pady=1)
                self.sin_inv_grad.grid_forget()
                self.sin_inv.grid(row=0, column=2, padx=1, pady=1)
                self.cos_inv_grad.grid_forget()
                self.cos_inv.grid(row=0, column=3, padx=1, pady=1)
                self.tan_inv_grad.grid_forget()
                self.tan_inv.grid(row=0, column=4, padx=1, pady=1)
                num = 1

# ----------------------------------------------------------------------------------------------------------------------
        def switch_calc():
            ScientificCalculator.destroy(self)
            Calculator()
# ----------------------------------------------------------------------------------------------------------------------
# Bindings:~

        self.bind('<Key-1>', lambda event: one_click())
        self.bind('<Key-2>', lambda event: two_click())
        self.bind('<Key-3>', lambda event: three_click())
        self.bind('<Key-4>', lambda event: four_click())
        self.bind('<Key-5>', lambda event: five_click())
        self.bind('<Key-6>', lambda event: six_click())
        self.bind('<Key-7>', lambda event: seven_click())
        self.bind('<Key-8>', lambda event: eight_click())
        self.bind('<Key-9>', lambda event: nine_click())
        self.bind('<Key-0>', lambda event: zero_click())

        self.bind('+', lambda event: plus_click())
        self.bind('-', lambda event: minus_click())
        self.bind('*', lambda event: multi_click())
        self.bind('/', lambda event: div_click())
        self.bind('.', lambda event: period_click())
        self.bind('<Return>', lambda event: bt_equal())

        self.bind('<BackSpace>', lambda event: func_backspace())
        self.bind('<Delete>', lambda event: bt_clear())

# ----------------------------------------------------------------------------------------------------------------------


expression = ""
memory = ""
# **********************************************************************************************************************
#                                             Mainloop
# **********************************************************************************************************************
if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
