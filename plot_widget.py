import tkinter as tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class PlotWidget:
    def __init__(self, parent):
        self.parent = parent
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)

        # Create the canvas and pack it to fill the space
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Add the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.parent)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_graph(self, x_col, y_cols, title, df, x_title="", y_title="", legend=False, grid=False):
        self.ax.clear()

        if x_col and y_cols and df is not None:
            try:
                x = df[x_col].values

                for y_col in y_cols:
                    y = df[y_col].values
                    color = self.parent.line_colors.get(y_col, None)  # Fetch color if available
                    line, = self.ax.plot(x, y, label=y_col, linewidth=2,
                                         color=color or 'blue')  # Use default color if none is selected

                    # Add labels at the start and end points of each line
                    # self.ax.text(x[0], y[0], f'{y_col} Start', color=line.get_color(), ha='right', va='center')
                    # self.ax.text(x[-1], y[-1], y_col, color=line.get_color(), va='center')

                self.ax.set_xlabel(x_title)
                self.ax.set_ylabel(y_title)
                self.ax.set_title(title)

                if legend:
                    self.ax.legend()
                if grid:
                    self.ax.grid(True)

                self.canvas.draw()
                # self.parent.update_status_bar("Plot generated successfully")
            except Exception as e:
                message = f"Error: {str(e)}"
                # self.parent.update_status_bar(message)
                print(message)

