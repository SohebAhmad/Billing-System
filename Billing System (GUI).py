from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700")
        self.root.title("Billing Software")
        self.bg_color = "#074463"
        title = Label(
            self.root,
            text="Billing Software",
            bd=5,
            relief=GROOVE,
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 20, "bold"),
            pady=2,
        ).pack(fill=X)

        # ==============Variables================

        # ==============Cosmetic=================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_oil = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        # ==============Grocery=================
        self.rice = IntVar()
        self.FoodOil = IntVar()
        self.Daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ==============Cold Drinks=================
        self.redbull = IntVar()
        self.Maza = IntVar()
        self.Coke = IntVar()
        self.appyfizz = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ===========Total product price & Tax Variable==========
        self.cosmetic_price = IntVar()
        self.grocery_price = IntVar()
        self.cold_drinks_price = IntVar()
        self.total_cosmetic_price = IntVar()
        self.total_grocery_price = IntVar()
        self.Total_bill = 0

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # ================Customer================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

    def find_bill(self):
        present="no"
        if os.path.exists("bills"):
            # print("Path Exists...")
            for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in f1:
                        self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill No.")
        else:
            # print("Path does not exists...")
            os.mkdir("bills")
            messagebox.showerror("Warning","Path does not exists")

    # -----------------------------------------------------
    # ------------customer Detail name frame---------------
    def main(self):
        F1 = LabelFrame(
            self.root,
            text="Customer Details",
            bd=10,
            relief=GROOVE,
            bg=self.bg_color,
            font=("times new roman", 15, "bold"),
            fg="lightgreen",
        )
        F1.place(x=0, y=45, relwidth=1)

        cname_label = Label(
            F1,
            text="Customer Name",
            fg="white",
            bg=self.bg_color,
            font=("times new roman", 18, "bold"),
        ).grid(row=0, column=0, padx=20, pady=5)
        cname_text = Entry(
            F1, width=15,bd=8, textvariable=self.c_name, font="arial,15,bd=7,relief=SUNKEN"
        ).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(
            F1,
            text="Customer Phn no.",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 18, "bold")).grid(
                row=0, column=2, padx=20, pady=10
        )
        cphn_lbl = Entry(
            F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN
        ).grid(row=0, column=3, pady=5, padx=10)

        bill_lbl = Label(
            F1,
            text="Bill No.",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        bill_lbl = Entry(
            F1,
            width=15,
            font="arial 15",
            textvariable=self.search_bill,
            bd=7,
            relief=SUNKEN,
        ).grid(row=0, column=5, pady=5, padx=10)


        #=====find bill from bill file==========

        bill_btn = Button(F1, text="search",command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(
            row=0, column=6, padx=10, pady=10
        )

        # ----------cosmetic Frame-----------
        F2 = LabelFrame(
            self.root,
            bd=10,
            relief=GROOVE,
            text="Cosmetic",
            font=("times new roman", 15, "bold"),
            fg="lightgreen",
            bg=self.bg_color,
        )
        F2.place(x=5, y=145, width=325, height=380)

        bath_lbl = Label(
            F2,
            text="Bath Soap",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_lbl = Entry(
            F2,
            width=10,
            textvariable=self.soap,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(
            F2,
            text="Face Cream",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_lbl = Entry(
            F2,
            width=10,
            textvariable=self.face_cream,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=1, column=1, padx=10, pady=10)

        face_w_lbl = Label(
            F2,
            text="Face Wash",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_lbl = Entry(
            F2,
            width=10,
            textvariable=self.face_wash,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=2, column=1, padx=10, pady=10)

        Hair_o_lbl = Label(
            F2,
            text="Hair Oil",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_o_lbl = Entry(
            F2,
            width=10,
            textvariable=self.hair_oil,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=3, column=1, padx=10, pady=10)

        body_lbl = Label(
            F2,
            text="body Loshan",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        body_lbl = Entry(
            F2,
            width=10,
            textvariable=self.loshan,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=4, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(
            F2,
            text="Hair spray",
            font=("times new roman", 16, "bold"),
            bd=5,
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Hair_s_lbl = Entry(
            F2,
            width=10,
            textvariable=self.spray,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=5, column=1, padx=10, pady=10)

        # ----------Grocery Frame-------
        F3 = LabelFrame(
            self.root,
            bd=10,
            relief=GROOVE,
            text="Grocery",
            font=("times new roman", 15, "bold"),
            fg="lightgreen",
            bg=self.bg_color,
        )
        F3.place(x=340, y=145, width=325, height=380)

        g1_lbl = Label(
            F3,
            text="rice",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=0, column=0, padx=10, pady=10)
        g1_txt = Entry(
            F3,
            width=10,
            textvariable=self.rice,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(
            F3,
            text="Food Oil",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=1, column=0, padx=10, pady=10)
        g2_txt = Entry(
            F3,
            width=10,
            textvariable=self.FoodOil,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(
            F3,
            text="Daal",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=2, column=0, padx=10, pady=10)
        g3_txt = Entry(
            F3,
            width=10,
            textvariable=self.Daal,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(
            F3,
            text="Wheat",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=3, column=0, padx=10, pady=10)
        g4_txt = Entry(
            F3,
            width=10,
            textvariable=self.wheat,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(
            F3,
            text="Sugar",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=4, column=0, padx=10, pady=10)
        g5_txt = Entry(
            F3,
            width=10,
            textvariable=self.sugar,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(
            F3,
            text="Tea",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=5, column=0, padx=10, pady=10)
        g6_txt = Entry(
            F3,
            width=10,
            textvariable=self.tea,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=5, column=1, padx=10, pady=10)

        # ---------------Cold Drinks-------------------
        F4 = LabelFrame(
            self.root,
            bd=10,
            relief=GROOVE,
            text="Cold Drinks",
            font=("times new roman", 15, "bold"),
            fg="lightgreen",
            bg=self.bg_color,
        )
        F4.place(x=670, y=145, width=325, height=380)

        c1_lbl = Label(
            F4,
            text="redbull",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=0, column=0, padx=10, pady=10)
        c1_txt = Entry(
            F4,
            width=10,
            textvariable=self.redbull,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(
            F4,
            text="Maza",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=1, column=0, padx=10, pady=10)
        c2_txt = Entry(
            F4,
            width=10,
            textvariable=self.Maza,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(
            F4,
            text="Coke",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=2, column=0, padx=10, pady=10)
        c3_txt = Entry(
            F4,
            width=10,
            textvariable=self.Coke,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(
            F4,
            text="Appyfizz",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=3, column=0, padx=10, pady=10)
        c4_txt = Entry(
            F4,
            width=10,
            textvariable=self.appyfizz,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(
            F4,
            text="limca",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=4, column=0, padx=10, pady=10)
        c5_txt = Entry(
            F4,
            width=10,
            textvariable=self.limca,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(
            F4,
            text="sprite",
            font=("times new roman", 16, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        ).grid(row=5, column=0, padx=10, pady=10)
        c6_txt = Entry(
            F4,
            width=10,
            textvariable=self.sprite,
            font=("times new roman", 16, "bold"),
            bd=5,
            relief=SUNKEN,
        ).grid(row=5, column=1, padx=10, pady=10)

        # ------------Bill Area ----------
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=145, width=350, height=380)

        bill_title = Label(
            F5, text="Bill Area", font=("arial 15 bold"), bd=7, relief=GROOVE
        ).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ------------Button Frame--------
        F6 = LabelFrame(
            self.root,
            bd=10,
            relief=GROOVE,
            text="Bill Menu",
            font=("times new roman", 15, "bold"),
            bg=self.bg_color,
            fg="lightgreen",
        )
        F6.place(x=0, y=525, relwidth=1, height=200)

        m1_lbl = Label(
            F6,
            text="Total Cosmetic Price",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 14, "bold")).grid(
                row=0, column=0, padx=20, pady=1, sticky="w"
            )
        m1_txt = Entry(
            F6,
            width=18,
            textvariable=self.cosmetic_price,
            font=("arial", 10, "bold"),
            bd=7,
            relief=SUNKEN,
        ).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(
            F6,
            text="Total Grocery Price",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 14, "bold")).grid(
                row=1, column=0, padx=20, pady=1, sticky="w"
            )
        m2_txt = Entry(
            F6,
            width=18,
            textvariable=self.grocery_price,
            font=("arial", 10, "bold"),
            bd=7,
            relief=SUNKEN,
        ).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(
            F6,
            text="Total Soft Drinks Price",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 14, "bold")).grid(
                row=2, column=0, padx=20, pady=1, sticky="w"
            )
        m3_txt = Entry(
            F6,
            width=18,
            textvariable=self.cold_drinks_price,
            font=("arial", 10, "bold"),
            bd=7,
            relief=SUNKEN,
        ).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(
            F6,
            text="Cosmetic Tax",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 14, "bold")).grid(
                row=0, column=2, padx=20, pady=1, sticky="w"
            )
        c1_txt = Entry(
            F6,
            width=18,
            font=("arial", 10, "bold"),
            textvariable=self.cosmetic_tax,
            bd=7,
            relief=SUNKEN,
        ).grid(row=0, column=3, padx=10, pady=10)

        c2_lbl = Label(
            F6,
            text="Grocery Tax",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 14, "bold")).grid(
                row=1, column=2, padx=20, pady=1, sticky="w"
            )
        c2_txt = Entry(
            F6,
            width=18,
            font=("arial", 10, "bold"),
            textvariable=self.grocery_tax,
            bd=7,
            relief=SUNKEN,
        ).grid(row=1, column=3, padx=10, pady=10)

        c3_lbl = Label(
            F6,
            text="Cold Drinks Tax",
            bg=self.bg_color,
            fg="white",
            font=("times new roman", 14, "bold")).grid(
                row=2, column=2, padx=20, pady=10, sticky="w"
            )
        c3_txt = Entry(
            F6,
            width=18,
            font=("arial", 10, "bold"),
            textvariable=self.cold_drinks_tax,
            bd=7,
            relief=SUNKEN,
        ).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(
            btn_F,
            command=self.total,
            text="Total",
            bg="blue",
            fg="white",
            bd=2,
            pady=3,
            width=7,
            font=("arial 15 bold")).grid(row=0, column=0, padx=5, pady=5)
        Gbill_btn = Button(
            btn_F,
            text="Generate Bill",
            command=self.bill_area,
            bg="blue",
            fg="white",
            bd=2,
            pady=3,
            width=10,
            font=("arial 15 bold")).grid(row=0, column=2, padx=5, pady=5)
        save_bill_btn = Button(
            btn_F,
            text="Save",
            command=self.save_bill,
            bg="blue",
            fg="white",
            bd=2,
            pady=3,
            width=7,
            font=("arial 15 bold")).grid(row=0, column=3, padx=5, pady=5)
        clear_btn = Button(
            btn_F,
            text="Clear",
            command=self.clear_data,
            bg="DarkOrange4",
            fg="white",
            bd=2,
            pady=3,
            width=7,
            font=("arial 15 bold")).grid(row=0, column=4, padx=5, pady=5)
        Exit_btn = Button(
            btn_F,
            text="Exit",
            command=self.Exit_app,
            bg="red",
            fg="white",
            bd=2,
            pady=3,
            width=7,
            font=("arial 15 bold")).grid(row=0, column=5, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()* 160
        self.c_fw_p=self.face_wash.get() * 95
        self.c_hs_p=self.spray.get() * 85
        self.c_hg_p=self.gell.get() * 78
        self.c_l_p=self.loshan.get() * 110

        self.total_cosmetic_price = float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_l_p 
                                    )
            
        self.cosmetic_price.set(self.total_cosmetic_price)
        self.c_tax=round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set(self.c_tax)
        
        
        self.g_r_p=self.rice.get() * 75
        self.g_fo_p=self.FoodOil.get() * 140
        self.g_d_p=self.Daal.get() * 85
        self.g_w_p=self.wheat.get() * 280
        self.g_s_p=self.sugar.get() * 42
        self.g_t_p=self.tea.get() * 55

        self.total_grocery_price = float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_t_p 
                                    )
            
        self.grocery_price.set(self.total_grocery_price)
        self.g_tax=round((self.total_grocery_price * 0.07),2)
        self.grocery_tax.set(self.g_tax)
        
        self.d_stg_p=self.redbull.get() * 40
        self.d_m_p=self.Maza.get() * 100
        self.d_c_p=self.Coke.get() * 95
        self.d_af_p=self.appyfizz.get() * 65
        self.d_l_p=self.limca.get() * 85
        self.d_s_p=self.sprite.get() * 90

        self.total_cold_drinks_price = float(
                                    self.d_stg_p+
                                    self.d_m_p+
                                    self.d_c_p+
                                    self.d_af_p+
                                    self.d_l_p+
                                    self.d_s_p 
                                    )

        # self.cold_drinks_price.set("Rs. " + str(self.total_cold_drinks_price))
        # self.d_tax=round((self.total_cold_drinks_price * 0.05),2)
        # self.cold_drinks_tax.set("Rs. "+str(self.d_tax))
        self.cold_drinks_price.set(self.total_cold_drinks_price)
        self.d_tax=round((self.total_cold_drinks_price * 0.05),2)
        self.cold_drinks_tax.set(self.d_tax)

    def welcome_bill(self):  
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, f" Welcome to faruki kirana store \n")
        self.txtarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n =====================================")
        self.txtarea.insert(END,f"\n products\t\tQTY\t\tprice")   
        self.txtarea.insert(END, f"\n =====================================")

        # self.Total_bill=float(self.total_cosmetic_price+
        #                        self.total_grocery_price+
        #                        self.total_drinks_price+
        #                        self.c_tax+
        #                        self.g_tax+
        #                        self.d_tax

        #                     )

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","customer details are must")
        elif self.cosmetic_price.get()==0 and self.grocery_price.get()==0 and self.cold_drinks_price.get()==0:
            messagebox.showerror("Error","no product purchased")
        else:
            self.welcome_bill()
    #=============cosmetics=============
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n bath soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_oil.get()!=0:
                self.txtarea.insert(END,f"\n hair oil\t\t{self.hair_oil.get()}\t\t{self.c_hs_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n spray\t\t{self.loshan.get()}\t\t{self.c_l_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n gell\t\t{self.spray.get()}\t\t{self.c_hs_p}")
    #=============grocery=============
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.FoodOil.get()!=0:
                self.txtarea.insert(END,f"\n food oil\t\t{self.FoodOil.get()}\t\t{self.g_fo_p}")
            if self.Daal.get()!=0:
                self.txtarea.insert(END,f"\n daal\t\t{self.Daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
    #=============cold Drinks=============
            if self.redbull.get()!=0:
                self.txtarea.insert(END,f"\n redbull\t\t{self.redbull.get()}\t\t{self.d_stg_p}")
            if self.Maza.get()!=0:
                self.txtarea.insert(END,f"\n maza\t\t{self.Maza.get()}\t\t{self.d_m_p}")
            if self.Coke.get()!=0:
                self.txtarea.insert(END,f"\n coke\t\t{self.Coke.get()}\t\t{self.d_c_p}")
            if self.appyfizz.get()!=0:
                self.txtarea.insert(END,f"\n appyfizz\t\t{self.appyfizz.get()}\t\t{self.d_af_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, f"\n------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n cosmatic tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n grocery tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n cold drinks tax\t\t\t{self.cold_drinks_tax.get()}")
            
            self.Total_bill=float(self.total_cosmetic_price+
                               self.total_grocery_price+
                               self.total_cold_drinks_price+
                               self.c_tax+
                               self.g_tax+
                               self.d_tax
                            )
            self.txtarea.insert(END, f"\n------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {str(self.Total_bill)}" )

        #   self.txtarea.insert(END, f"\n------------------------")
    def save_bill(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","customer details are must")
        elif self.cosmetic_price.get()==0 and self.grocery_price.get()==0 and self.cold_drinks_price.get()==0:
            messagebox.showerror("Error","no product purchased")
        else:
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
            if op>0:
                my_path = f"{os.getcwd()}\\bills\\"
                # os.mkdir(path)
                if os.path.exists(my_path):
                    self.bill_data=self.txtarea.get('1.0', END)
                    f1=open(my_path+str(self.bill_no.get())+".txt","w")
                    f1.write(self.bill_data)
                    f1.close
                    messagebox.showinfo("Saved",f"Bill_no. : {self.bill_no.get()} saved successfully")
                else:
                    os.mkdir(my_path)
                    self.bill_data=self.txtarea.get('1.0', END)
                    f1=open(my_path+str(self.bill_no.get())+".txt","w")
                    f1.write(self.bill_data)
                    f1.close
                    messagebox.showinfo("Saved",f"Bill_no. : {self.bill_no.get()} saved successfully")
            else:
                return

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:
        # ==============Cosmetic=================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_oil.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

            # ==============Grocery=================
            self.rice.set(0)
            self.FoodOil.set(0)
            self.Daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ==============Cold Drinks=================
            self.redbull.set(0)
            self.Maza.set(0)
            self.Coke.set(0)
            self.appyfizz.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ===========Total product price & Tax Variable==========
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            # ================Customer================
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit")
        if op>0:
            self.root.destroy()
root = Tk()
obj = Bill_App(root)
obj.main()
root.mainloop()
