import tkinter as tk
from tkinter import messagebox
from mysql.connector import connect
from tkinter import ttk


class MainApp(tk.Frame):
    def __init__(self, master=None, db=None) -> None:
        master.title("Employee Management")
        super().__init__(master)
        self.table_frame = TableFrame(self)
        self.input_frame = InputFrame(master=self, db=db, table=self.table_frame)
        self.db = db


class TableFrame(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        self.table = ttk.Treeview(self)
        self.table.pack(fill=tk.BOTH, expand=True)

    def show_results(self, keys, values):
        self.table.delete(*self.table.get_children())
        self.table["columns"] = keys

        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.heading("#0", text="", anchor=tk.CENTER)

        for key in keys:
            self.table.column(key, anchor=tk.CENTER, stretch=True)
            self.table.heading(key, text=key.capitalize().replace("_", ","), anchor="center")

        for value in values:
            self.table.insert(parent="", index="end", values=value)


class InputFrame(tk.Frame):
    def __init__(self, db=None, master=None, table=None) -> None:
        super().__init__(master)
        self.pack(fill=tk.BOTH, side=tk.TOP)
        self.table_frame = table
        self.tabbed_window = ttk.Notebook(self)
        self.tabbed_window.pack(expand=True, fill=tk.BOTH)
        self.db = db
        self.show_ui()

    def show_ui(self):
        self.e_search_frame = EmployeeMainFrame(master=self.tabbed_window, db=self.db, table=self.table_frame)
        self.e_search_frame.pack(fill=tk.BOTH, expand=True)

        self.tabbed_window.add(self.e_search_frame, text="Employee Management")


class EmployeeMainFrame(tk.Frame):
    def __init__(self, db, master=None, table=None) -> None:
        super().__init__(master)

        self.db = db
        self.table_frame = table
        self.pack(fill=tk.BOTH)
        self.employee_id = tk.StringVar()
        self.employee_f_name = tk.StringVar()
        self.employee_l_name = tk.StringVar()
        self.employee_ph = tk.StringVar()
        self.employee_address = tk.StringVar()
        self.show_ui()

    def show_ui(self):
        style = {"sticky": "nswe", "ipadx": 5, "ipady": 3}
        ttk.Label(self, text="Employee ID:").grid_configure(row=0, column=0, **style)
        ttk.Entry(self, text="Enter ID", textvariable=self.employee_id).grid_configure(row=0, column=1, **style)

        ttk.Label(self, text="First Name:").grid_configure(row=1, column=0, **style)
        ttk.Entry(self, text="Enter First Name", textvariable=self.employee_f_name).grid_configure(
            row=1, column=1, **style
        )

        ttk.Label(self, text="Last Name:").grid_configure(row=2, column=0, **style)
        ttk.Entry(self, text="Enter Last Name", textvariable=self.employee_l_name).grid_configure(
            row=2, column=1, **style
        )

        ttk.Label(self, text="Ph no:").grid_configure(row=0, column=2, **style)
        ttk.Entry(self, text="Enter phone number", textvariable=self.employee_ph).grid_configure(
            row=0, column=3, **style
        )

        ttk.Label(self, text="Address: ").grid_configure(row=1, column=2, **style)
        ttk.Entry(self, text="Enter Address", textvariable=self.employee_address).grid_configure(
            row=1, column=3, **style
        )

        ttk.Button(self, text="Search", width=5, command=self.search_employee).grid_configure(
            row=2, column=3, sticky="nse", ipadx=5, ipady=3
        )

        ttk.Button(self, text="Add", width=5, command=self.add_employee).grid_configure(row=2, column=3, sticky="nsw", ipadx=5, ipady=3)

    def get_params(self):
        return {
            "f_name": self.employee_f_name.get(),
            "l_name": self.employee_l_name.get(),
            "ph_no": self.employee_ph.get(),
            "address": self.employee_address.get(),
            "id": self.employee_id.get(),
        }

    def search_employee(self):
        params = self.get_params()
        # filter out empty keys
        params = {key: val for key, val in params.items() if val != ""}
        results = self.db.search_employee(**params)
        self.table_frame.show_results(("ID", "First Name", "Last Name", "Adress", "Phone no"), results)

    def add_employee(self):
        params = self.get_params()

        for key, val in params.items():
            if val == "" and key != "id":
                messagebox.showwarning(title="Missing Information", message="Please fill all details")
                return
            if key == "id" and val != "":
                messagebox.showwarning(title="Invalid", message="Employee ID is auto generated!")
                return
        params.pop("id")
        self.db.add_employee(**params)
        messagebox.showinfo(title="Success", message="Information Added")


class DBManager:
    def __init__(self, conn) -> None:
        self.conn = conn

    def search_employee(self, **kwargs):
        cur = self.conn.cursor()

        params = " AND ".join([f"{e}=%s" for e in kwargs.keys()])
        sql = f"SELECT * FROM employee_register WHERE {params};"
        cur.execute(sql, [a for a in kwargs.values()])
        results = cur.fetchall()
        return results

    def add_employee(self, **kwargs):
        cur = self.conn.cursor()

        params = ",".join(["%s" for e in kwargs.values()])
        columns = ','.join(kwargs.keys())
        sql = f"INSERT INTO employee_register({columns}) VALUES({params});"
        print(sql)
        cur.execute(sql, [a for a in kwargs.values()])


if __name__ == "__main__":
    root = tk.Tk()
    db = DBManager(connect(host="localhost", user="root", password="", database="employees"))
    app = MainApp(root, db=db)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
