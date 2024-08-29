# main_app.py
import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import os
import data_handler
from main_ui import MainWindow
from plot_widget import PlotWidget

class MainApp(MainWindow):
    def __init__(self,):
        super().__init__()
        self.df = None
        self.plot_window = None
        self.plot_widget = None  # Reference to PlotWidget instance
        self.bind_buttons()

    def bind_buttons(self):
        self.add_file_button.config(command=self.add_file)
        self.add_button.config(command=self.add_item)
        self.remove_button.config(command=self.remove_item)
        self.clear_button.config(command=self.clear_items)
        self.plot_button.config(command=self.open_plot_window)

    def add_file(self):
        # File dialog to select Excel or CSV files
        file_path = filedialog.askopenfilename(
            filetypes=[("Data files", "*.xlsx;*.xls;*.csv"), ("All files", "*")],
            title="Select a Data File"
        )
        if file_path:
            filename = os.path.basename(file_path)
            self.file_name_var.set(filename)
            self.load_data(file_path)
        else:
            messagebox.showwarning("File Selection", "No file selected or unsupported file type.")

    def update_status_bar(self, message):
        # Update the status bar with the given message
        self.status_bar_var.set(message)
    #
    def load_data(self, file_path):
        self.df, error = data_handler.load_excel(file_path)
        if self.df is not None:
            self.update_list_view()
            self.update_dropdowns()
            self.update_status_bar("File loaded successfully")
        else:
            self.update_status_bar(f"Error: {error}")

    def update_dropdowns(self):
        # Clear existing items in the Combobox
        self.dropdown_x_axis['values'] = []

        # Get column names from the DataFrame using the data_handler
        column_names = data_handler.get_column_names(self.df)

        # Add new items to the Combobox
        if column_names:
            self.dropdown_x_axis['values'] = column_names

        # Optionally, set the first item as the current selection
        if column_names:
            self.dropdown_x_axis.set(column_names[0])

        self.update_status_bar("Dropdown updated with column names.")
    #
    def update_list_view(self):
        # Clear existing items in the listbox
        self.list_columns.delete(0, tk.END)

        # Get column names from the DataFrame using the data_handler
        column_names = data_handler.get_column_names(self.df)

        # Add new items to the listbox
        if column_names:
            for col in column_names:
                self.list_columns.insert(tk.END, col)

        self.update_status_bar("List updated with column names.")

    def add_item(self):
        selected_indices = self.list_columns.curselection()
        existing_items = self.list_columns_2.get(0, tk.END)

        if not existing_items:
            existing_items = []

        for index in reversed(selected_indices):  # Reversed to handle deletion while iterating
            column_name = self.list_columns.get(index)

            # Add to list_columns_2 if not already present
            if column_name not in existing_items:
                self.list_columns_2.insert(tk.END, column_name)

            # Remove the item from list_columns
            self.list_columns.delete(index)

        self.update_dropdowns()  # Update dropdowns after adding columns

        # Update status bar
        self.update_status_bar("Item(s) added to second list and removed from first list.")

    def remove_item(self):
        selected_indices = self.list_columns_2.curselection()

        # Collect the selected items to add back later
        items_to_add = []

        for index in reversed(selected_indices):  # Reversed to handle deletion while iterating
            column_name = self.list_columns_2.get(index)
            items_to_add.append(column_name)

            # Remove the item from list_columns_2
            self.list_columns_2.delete(index)

        # Add removed items back to list_columns
        for item in items_to_add:
            if item not in self.list_columns.get(0, tk.END):
                self.list_columns.insert(tk.END, item)

        self.update_dropdowns()  # Update dropdowns after removing columns

        # Update status bar
        self.update_status_bar("Item(s) removed from second list and added back to first list.")

    def clear_items(self):
        # Clear all items from list_columns_2
        self.list_columns_2.delete(0, tk.END)

        # Update the list view and dropdowns
        self.update_list_view()
        self.update_dropdowns()  # Refresh dropdowns

        # Update status bar
        self.update_status_bar("All items cleared from the second list.")

    def open_plot_window(self):
        if self.plot_window is None or not self.plot_window.winfo_exists():
            # Create a new Toplevel window for the plot
            self.plot_window = tk.Toplevel(self)
            self.plot_window.title("Plot")
            self.plot_window.geometry("800x600")  # Set the size of the plot window

            # Initialize PlotWidget in the new Toplevel window
            self.plot_widget = PlotWidget(self.plot_window)
        else:
            # If the plot window already exists, bring it to the front
            self.plot_window.lift()

        # Get the required data from the main window
        x_col = self.dropdown_x_axis.get()
        y_cols = [self.list_columns_2.get(i) for i in range(self.list_columns_2.size())]
        title = self.plot_title.get()
        x_title = self.line_x_title.get()
        y_title = self.line_y_title.get()
        legend = self.legend_var.get()
        grid = self.grid_var.get()

        if self.plot_widget is not None:
            self.plot_widget.plot_graph(x_col, y_cols, title, self.df, x_title, y_title, legend, grid)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()