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
        self.tabbed_window.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
        self.show_ui()

    def show_ui(self):
        self.e_search_frame = EmployeeSearchFrame(self.tabbed_window)
        self.e_search_frame.pack(fill=tk.BOTH, expand=True)

        self.tabbed_window.add(self.e_search_frame, text="Employee Search")


class EmployeeSearchFrame(tk.Frame):
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
        ttk.Style(self).configure("S.TLabel.grid", sticky="NSWE")
        ttk.Style(self).configure(
            "S.TEntry",
            border=(3, 3, 3, 3),
            sticky="NSWE",
            justify=tk.LEFT,
        )

        id_label = ttk.Label(self, text="Employee ID:", style="S.TLabel").grid(row=0, column=0)
        id_entry = ttk.Entry(self, style="S.TEntry", text="Enter ID", textvariable=self.employee_id).grid(
            row=0, column=1
        )

        f_name_label = ttk.Label(self, text="First Name:", style="S.TLabel").grid(row=1, column=0)
        f_name_entry = ttk.Entry(
            self, style="S.TEntry", text="Enter First Name", textvariable=self.employee_f_name
        ).grid(row=1, column=1)

        l_name_label = ttk.Label(self, text="Last Name:", style="S.TLabel").grid(row=2, column=0)
        l_name_entry = ttk.Entry(
            self, style="S.TEntry", text="Enter Last Name", textvariable=self.employee_l_name
        ).grid(row=2, column=1)

        ph_label = ttk.Label(self, text="Ph no:", style="S.TLabel").grid(row=0, column=2, sticky="NSWE")
        ph_entry = ttk.Entry(self, style="S.TEntry", text="Enter phone number", textvariable=self.employee_ph).grid(
            row=0, column=3
        )

        address_label = ttk.Label(self, text="Address: ", style="S.TLabel").grid(row=1, column=2)
        address_entry = ttk.Entry(
            self, style="S.TEntry", text="Enter Address", textvariable=self.employee_address
        ).grid(row=1, column=3)

        search_button = ttk.Button(self, text="search").grid(row=2, column=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
