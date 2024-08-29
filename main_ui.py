# main_ui.py
import tkinter as tk
from tkinter import ttk, filedialog, Listbox, StringVar
from plot_widget import PlotWidget

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DataVisualisation Tool")
        # self.geometry("1200x580") #Set Window Size

        # Create and configure main widgets
        self.create_widgets()

    def create_widgets(self):
        # Central Widget
        self.centralwidget = tk.Frame(self)
        self.centralwidget.pack(fill="both", expand=True)

        # File selection layout
        self.file_name_var = StringVar(value="No File Selected")
        file_frame = tk.Frame(self.centralwidget)
        file_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.file_name = tk.Entry(file_frame, textvariable=self.file_name_var, state="readonly", width=60)
        self.file_name.pack(side="left", fill="x", expand=True)
        self.add_file_button = tk.Button(file_frame, text="Add File")
        self.add_file_button.pack(side="left", padx=5)

        # X-Axis Label
        self.x_axis_label = tk.Label(self.centralwidget, text="Y-Axis Data", anchor="center")
        self.x_axis_label.grid(row=1, column=0, pady=5)

        # List selection layout
        list_frame = tk.Frame(self.centralwidget)
        list_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        list_frame.columnconfigure(1, weight=1)

        self.list_columns = Listbox(list_frame, selectmode="single")
        self.list_columns.grid(row=0, column=0, sticky="nsew")

        button_frame = tk.Frame(list_frame)
        button_frame.grid(row=0, column=1, padx=5)
        self.add_button = tk.Button(button_frame, text="Add")
        self.add_button.pack(fill="x")
        self.remove_button = tk.Button(button_frame, text="Remove")
        self.remove_button.pack(fill="x")
        self.clear_button = tk.Button(button_frame, text="Clear")
        self.clear_button.pack(fill="x")

        self.list_columns_2 = Listbox(list_frame, selectmode="single")
        self.list_columns_2.grid(row=0, column=2, sticky="nsew")

        # X-Axis dropdown
        x_axis_frame = tk.Frame(self.centralwidget)
        x_axis_frame.grid(row=3, column=0, pady=5, padx=10)
        tk.Label(x_axis_frame, text="X-Axis Data").pack(anchor="w")
        self.dropdown_x_axis = ttk.Combobox(x_axis_frame, state="readonly")
        self.dropdown_x_axis.pack(fill="x")

        # X-Axis Title
        x_title_frame = tk.Frame(self.centralwidget)
        x_title_frame.grid(row=4, column=0, pady=5, padx=10)
        tk.Label(x_title_frame, text="X-Axis Title").pack(anchor="w")
        self.line_x_title = tk.Entry(x_title_frame)
        self.line_x_title.pack(fill="x")

        # Y-Axis Title
        y_title_frame = tk.Frame(self.centralwidget)
        y_title_frame.grid(row=5, column=0, pady=5, padx=10)
        tk.Label(y_title_frame, text="Y-Axis Title").pack(anchor="w")
        self.line_y_title = tk.Entry(y_title_frame)
        self.line_y_title.pack(fill="x")

        # Display options
        display_group = tk.LabelFrame(self.centralwidget, text="Display")
        display_group.grid(row=6, column=0, pady=5, padx=10, sticky="ew")

        # Initialize variables for the checkboxes
        self.legend_var = tk.BooleanVar()
        self.grid_var = tk.BooleanVar()

        self.legend_check = tk.Checkbutton(display_group, text="Legend", variable=self.legend_var)
        self.legend_check.grid(row=0, column=0, sticky="w")
        self.grid_check = tk.Checkbutton(display_group, text="Grid", variable=self.grid_var)
        self.grid_check.grid(row=0, column=1, sticky="w")

        # Plot title and button
        self.plot_title = tk.Entry(self.centralwidget, justify="center")
        self.plot_title.insert(0, "Plot Title")
        self.plot_title.grid(row=7, column=0, pady=5, padx=10, sticky="ew")
        self.plot_button = tk.Button(self.centralwidget, text="PLOT!")
        self.plot_button.grid(row=8, column=0, pady=5, padx=10)

        # Status bar setup
        self.status_bar_var = tk.StringVar()
        self.status_bar = tk.Label(self, textvariable=self.status_bar_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Set initial status bar text
        self.status_bar_var.set("Ready")

    # def update_status_bar(self, message):
    #     self.status_bar_var.set(message)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()