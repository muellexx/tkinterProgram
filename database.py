from tkinter import *
from tkinter import filedialog, ttk
import os, sqlite3

def rotate(l, n):
    return l[n:] + l[:n]

class database_app:

    def __init__(self, root):
        self.root = root
        self.show_start()

    def remove_widgets(self):
        if hasattr(self,'btn_start_screen'):
            self.btn_start_screen.grid_remove()
        if hasattr(self, 'tv_frame'):
            self.tv_frame.grid_remove()

    def show_start(self):
        self.remove_widgets()
        if not hasattr(self, 'start_frame'):
            self.start_frame = LabelFrame(self.root, text="Choose Database")
            self.btn_new_database = Button(self.start_frame, text="Create New Address Database", command=lambda: self.create_database(False))
            self.btn_new_database.grid(padx=5, pady=5)
            self.btn_open_database = Button(self.start_frame, text="Open Existing Address Database", command=self.open_database)
            self.btn_open_database.grid(padx=5, pady=5)
            self.btn_test_database = Button(self.start_frame, text="Create Test Database", command=lambda: self.create_database(True))
            self.btn_test_database.grid(padx=5, pady=5)
        self.start_frame.grid(sticky=N+S+E+W)
        
    def create_database(self, dummy):
        self.db_path = filedialog.asksaveasfilename(title = "Create Database", filetypes = (("Database File","*.db"),("all files","*.*")))
        if not self.db_path:
            return
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            country text
            )""")

        conn.commit()
        conn.close()
        if dummy:
            self.create_test_database()
        self.show_database_app()

    def open_database(self):
        self.db_path = filedialog.askopenfilename(title = "Open Database", filetypes = (("Database File","*.db"),("all files","*")))
        if not self.db_path:
            return
        self.show_database_app()
    
    def show_database_app(self):
        self.start_frame.grid_remove()
        # self.btn_new_database.grid_remove()
        # self.btn_open_database.grid_remove()
        
        self.btn_start_screen = Button(self.root, text="Back to Start", command=self.show_start)
        self.btn_start_screen.grid(padx=5, pady=5)
        
        self.query()
        return

    def query(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()

        self.tv_frame = LabelFrame(self.root, text='Address List')

        self.treeview = ttk.Treeview(self.tv_frame, height=15)
        # headings = rotate([description[0] for description in c.description], -1)
        headings = ['ID', 'First Name', 'Last Name', 'Address', 'City', 'State', 'Zipcode']
        widths = [40, 100, 100, 160, 100, 100, 60]
        self.treeview["columns"] = headings
        self.treeview["show"] = "headings"
        for i in range(len(headings)):
            self.treeview.column(headings[i], width=widths[i], stretch=YES)
            self.treeview.heading(headings[i], text=headings[i])
        
        for i in range(len(records)):
            self.treeview.insert("", i, i, values=rotate(records[i], -1))

        self.treeview.grid(row=0, column=0, padx=5, pady=5)
        # self.treeview.pack(fill='y', expand=1)

        vsb = ttk.Scrollbar(self.tv_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky="ns")
        self.tv_frame.grid(sticky=E+W+N+S, padx=5, pady=5)

        self.btn_frame = Frame(self.tv_frame)
        self.btn_frame.grid()
        self.add_btn = Button(self.btn_frame, text="Add New Record", command=self.add_entry)
        self.add_btn.grid(row=0, column=0, padx=5, pady=5)
        self.btn_edit = Button(self.btn_frame, text="Edit Record", command=self.edit_entry)
        self.btn_edit.grid(row=0, column=1, padx=5, pady=5)
        self.delete_btn = Button(self.btn_frame, text="Delete Record", command=self.delete)
        self.delete_btn.grid(row=0, column=2, padx=5, pady=5)
        
        conn.commit()
        conn.close()

    def add_entry(self):
        self.add_window = Toplevel()
        self.add_window.title('Add A New Record')
        self.add_window.minsize(300,300)

        self.db_form = address_form(self.add_window)

        save_btn = Button(self.add_window, text="Save Record", command=self.submit)
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)
    
    def submit(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': self.db_form.f_name.get(),
                'l_name': self.db_form.l_name.get(),
                'address': self.db_form.address.get(),
                'city': self.db_form.city.get(),
                'state': self.db_form.state.get(),
                'zipcode': self.db_form.country.get()
            })

        conn.commit()
        conn.close()

        self.update_treeview()

        self.add_window.destroy()

    def edit_entry(self):
        curItem = self.treeview.focus()
        try:
            self.record_id = self.treeview.item(curItem)['values'][0]

            self.editor = Toplevel()
            self.editor.title('Update A Record')
            self.editor.minsize(300,300)

            self.address_form_edit = address_form(self.editor)

            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()

            c.execute("SELECT * FROM addresses WHERE oid = " + str(self.record_id))

            records = c.fetchall()
            for record in records:
                self.address_form_edit.f_name.insert(0, record[0])
                self.address_form_edit.l_name.insert(0, record[1])
                self.address_form_edit.address.insert(0, record[2])
                self.address_form_edit.city.insert(0, record[3])
                self.address_form_edit.state.insert(0, record[4])
                self.address_form_edit.country.insert(0, record[5])
            
            conn.commit()
            conn.close()

            save_btn = Button(self.editor, text="Save Record", command=self.update)
            save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)
            

        except IndexError:
            self.warning_label = Label(self.btn_frame, text="Please choose a record to edit!", fg="red")
            self.warning_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def update(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            country = :country

            WHERE oid = :oid""",
            {'first': self.address_form_edit.f_name.get(),
            'last': self.address_form_edit.l_name.get(),
            'address': self.address_form_edit.address.get(),
            'city': self.address_form_edit.city.get(),
            'state': self.address_form_edit.state.get(),
            'country': self.address_form_edit.country.get(),
            
            'oid': self.record_id
            }
        )

        conn.commit()
        conn.close()

        self.update_treeview()

        self.editor.destroy()

    def delete(self):
        curItem = self.treeview.focus()
        # messagebox.askyesno("Delete", "Hello World!")
        try:
            self.record_id = self.treeview.item(curItem)['values'][0]
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()

            c.execute("SELECT * FROM addresses WHERE oid = " + str(self.record_id))

            records = c.fetchall()
            record = records[0][0] + " " + records[0][1]

            title = "Delete " + record
            question = "Are you sure you want to delete " + record + "? This cannot be undone."

            confirmation = messagebox.askyesno(title, question)
            print(confirmation)
            if confirmation:
                c.execute("DELETE from addresses WHERE oid = " + str(self.record_id))

            conn.commit()
            conn.close()

            if confirmation:
                self.update_treeview()

        except IndexError:
            self.warning_label = Label(self.btn_frame, text="Please choose a record to delete!", fg="red")
            self.warning_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def update_treeview(self):
        if hasattr(self, "warning_label"):
            self.warning_label.destroy()
        items = self.treeview.get_children()
        for item in items:
            self.treeview.delete(item)

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        for i in range(len(records)):
            self.treeview.insert("", i, i, values=rotate(records[i], -1))
        
        conn.commit()
        conn.close()
        
    def create_test_database(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        dummy_list = example_entries()

        for entry in dummy_list:
            c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    'f_name': entry[0],
                    'l_name': entry[1],
                    'address': entry[2],
                    'city': entry[3],
                    'state': entry[4],
                    'zipcode': entry[5]
                })

        conn.commit()
        conn.close()


class address_form:

    def __init__(self, root):
        self.f_name = Entry(root, width=30)
        self.f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.l_name = Entry(root, width=30)
        self.l_name.grid(row=1, column=1, padx=20)
        self.address = Entry(root, width=30)
        self.address.grid(row=2, column=1, padx=20)
        self.city = Entry(root, width=30)
        self.city.grid(row=3, column=1, padx=20)
        self.state = Entry(root, width=30)
        self.state.grid(row=4, column=1, padx=20)
        self.country = Entry(root, width=30)
        self.country.grid(row=5, column=1, padx=20)

        self.f_name_label = Label(root, text="First Name")
        self.f_name_label.grid(row=0, column=0, pady=(10, 0))
        self.l_name_label = Label(root, text="Last Name")
        self.l_name_label.grid(row=1, column=0)
        self.address_label = Label(root, text="Address")
        self.address_label.grid(row=2, column=0)
        self.city_label = Label(root, text="City")
        self.city_label.grid(row=3, column=0)
        self.state_label = Label(root, text="State")
        self.state_label.grid(row=4, column=0)
        self.country_label = Label(root, text="Country")
        self.country_label.grid(row=5, column=0)


def example_entries():
    entry_list = []
    entry_list.append(['Albert', 'Einstein', '112 Mercer Street', 'Princeton', 'New Jersey','USA'])
    entry_list.append(['Isaac', 'Newton', 'Woolsthorpe Manor', 'Colsterworth', 'Lincolnshire','England'])
    entry_list.append(['Galileo', 'Galilei', 'Via del Pian dei Giullari, 42', 'Florence', 'Florence','Italy'])
    entry_list.append(['Stephen', 'Hawking', '12-26 Lexington Street', 'London', 'London','England'])
    entry_list.append(['Nikola', 'Tesla', 'The New Yorker Hotel', 'New York', 'New Yorker','USA'])
    entry_list.append(['Marie', 'Curie', 'Unknown', 'Warsaw', 'Warsaw','Poland'])
    entry_list.append(['Elon', 'Musk', 'Musk Street', 'Arcadia Planitia', 'Tharsis','Mars'])
    entry_list.append(['Thomas', 'Edison', 'Unknown', 'West Orange', 'New Jersey','USA'])
    entry_list.append(['Charles', 'Darwin', 'Down House', 'Downe', 'Downe','UK'])
    entry_list.append(['Steve', 'Jobs', 'Palo Alto', 'San Jose', 'California','USA'])
    entry_list.append(['Albert', 'Einstein', '112 Mercer Street', 'Princeton', 'New Jersey','USA'])
    entry_list.append(['Isaac', 'Newton', 'Woolsthorpe Manor', 'Colsterworth', 'Lincolnshire','England'])
    entry_list.append(['Galileo', 'Galilei', 'Via del Pian dei Giullari, 42', 'Florence', 'Florence','Italy'])
    entry_list.append(['Stephen', 'Hawking', '12-26 Lexington Street', 'London', 'London','England'])
    entry_list.append(['Nikola', 'Tesla', 'The New Yorker Hotel', 'New York', 'New Yorker','USA'])
    entry_list.append(['Marie', 'Curie', 'Unknown', 'Warsaw', 'Warsaw','Poland'])
    entry_list.append(['Elon', 'Musk', 'Musk Street', 'Arcadia Planitia', 'Tharsis','Mars'])
    entry_list.append(['Thomas', 'Edison', 'Unknown', 'West Orange', 'New Jersey','USA'])
    entry_list.append(['Charles', 'Darwin', 'Down House', 'Downe', 'Downe','UK'])
    entry_list.append(['Steve', 'Jobs', 'Palo Alto', 'San Jose', 'California','USA'])
    entry_list.append(['Albert', 'Einstein', '112 Mercer Street', 'Princeton', 'New Jersey','USA'])
    entry_list.append(['Isaac', 'Newton', 'Woolsthorpe Manor', 'Colsterworth', 'Lincolnshire','England'])
    entry_list.append(['Galileo', 'Galilei', 'Via del Pian dei Giullari, 42', 'Florence', 'Florence','Italy'])
    entry_list.append(['Stephen', 'Hawking', '12-26 Lexington Street', 'London', 'London','England'])
    entry_list.append(['Nikola', 'Tesla', 'The New Yorker Hotel', 'New York', 'New Yorker','USA'])
    entry_list.append(['Marie', 'Curie', 'Unknown', 'Warsaw', 'Warsaw','Poland'])
    entry_list.append(['Elon', 'Musk', 'Musk Street', 'Arcadia Planitia', 'Tharsis','Mars'])
    entry_list.append(['Thomas', 'Edison', 'Unknown', 'West Orange', 'New Jersey','USA'])
    entry_list.append(['Charles', 'Darwin', 'Down House', 'Downe', 'Downe','UK'])
    entry_list.append(['Steve', 'Jobs', 'Palo Alto', 'San Jose', 'California','USA'])
    return entry_list
