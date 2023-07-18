import tkinter as tk
from tkinter import ttk


class MainApp(tk.Frame):
    def __init__(self, master=None) -> None:
        master.title("Employee Management")
        super().__init__(master)
        self.table_frame = TableFrame(self)
        self.input_frame = InputFrame(self)


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
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.pack(fill=tk.BOTH, side=tk.TOP)
        self.tabbed_window = ttk.Notebook(self)
        self.tabbed_window.pack(expand=True, fill=tk.BOTH)
        self.show_ui()

    def show_ui(self):
        self.e_search_frame = EmployeeMainFrame(self.tabbed_window)
        self.e_search_frame.pack(fill=tk.BOTH, expand=True)

        self.tabbed_window.add(self.e_search_frame, text="Employee Management")


class EmployeeMainFrame(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        
        self.pack(fill=tk.BOTH)
        self.employee_id = tk.StringVar()
        self.employee_f_name = tk.StringVar()
        self.employee_l_name = tk.StringVar()
        self.employee_ph = tk.StringVar()
        self.employee_address = tk.StringVar()
        self.show_ui()

    def show_ui(self):
        ttk.Style(self).configure("TLabel", bg=self["background"])
        id_label = ttk.Label(self, text="Employee ID:")
        id_label.grid_configure(row=0, column=0, sticky="nswe", ipadx=5, ipady=3)
        id_entry = ttk.Entry(self, text="Enter ID", textvariable=self.employee_id)
        id_entry.grid_configure(row=0, column=1, sticky="nswe", ipadx=5, ipady=3)

        f_name_label = ttk.Label(self, text="First Name:")
        f_name_label.grid_configure(row=1, column=0, sticky="nswe", ipadx=5, ipady=3)
        f_name_entry = ttk.Entry(self, text="Enter First Name", textvariable=self.employee_f_name)
        f_name_entry.grid_configure(row=1, column=1, sticky="nswe", ipadx=5, ipady=3)

        l_name_label = ttk.Label(self, text="Last Name:")
        l_name_label.grid_configure(row=2, column=0, sticky="nswe", ipadx=5, ipady=3)
        l_name_entry = ttk.Entry(self, text="Enter Last Name", textvariable=self.employee_l_name)
        l_name_entry.grid_configure(row=2, column=1, sticky="nswe", ipadx=5, ipady=3)

        ph_label = ttk.Label(self, text="Ph no:")
        ph_label.grid_configure(row=0, column=2, sticky="nswe", ipadx=5, ipady=3)
        ph_entry = ttk.Entry(self, text="Enter phone number", textvariable=self.employee_ph)
        ph_entry.grid_configure(row=0, column=3, sticky="nswe", ipadx=5, ipady=3)

        address_label = ttk.Label(self, text="Address: ")
        address_label.grid_configure(row=1, column=2, sticky="nswe", ipadx=5, ipady=3)
        address_entry = ttk.Entry(self, text="Enter Address", textvariable=self.employee_address)
        address_entry.grid_configure(row=1, column=3, sticky="nswe", ipadx=5, ipady=3)

        search_button = ttk.Button(self, text="Search", width = 5)
        search_button.grid_configure(row=2, column=3, sticky="nse", ipadx=5, ipady=3)
        
        add_employee_button = ttk.Button(self, text="Add", width=5)
        add_employee_button.grid_configure(row=2, column=3, sticky="nsw", ipadx=5, ipady=3)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
