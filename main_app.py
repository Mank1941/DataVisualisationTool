# main_app.py

import sys
import os
import matplotlib.pyplot as plt
from PyQt5 import QtGui, QtWidgets
from main_ui import Ui_MainWindow
import data_handler  # Import the data handler module

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.addFileButton.clicked.connect(self.load_file)
        self.plotButton.clicked.connect(self.plot_graph)
        self.addButton.clicked.connect(self.add_column)
        self.removeButton.clicked.connect(self.remove_column)
        self.clearButton.clicked.connect(self.clear_columns)
        self.df = None

        # Initialize models
        self.listColumns.setModel(QtGui.QStandardItemModel())
        self.listColumns_2.setModel(QtGui.QStandardItemModel())

    def update_statusbar(self, text):
        self.statusBar.showMessage(text, 5000)

    def load_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_path:
            filename = os.path.basename(file_path)
            self.fileName.setText(filename)
            self.load_data(file_path)

    def load_data(self, file_path):
        self.df, error = data_handler.load_excel(file_path)
        if self.df is not None:
            self.update_list_view()
            self.update_dropdowns()
            self.update_statusbar("File loaded successfully")
        else:
            self.update_statusbar(f"Error: {error}")

    def update_dropdowns(self):
        self.dropdownXAxis.clear()
        column_names = data_handler.get_column_names(self.df)
        if column_names:
            for col in column_names:
                self.dropdownXAxis.addItem(col)

    def update_list_view(self):
        model = QtGui.QStandardItemModel()
        column_names = data_handler.get_column_names(self.df)
        if column_names:
            for col in column_names:
                item = QtGui.QStandardItem(col)
                model.appendRow(item)
        self.listColumns.setModel(model)

    def add_column(self):
        selected_items = self.listColumns.selectedIndexes()
        list_columns_model = self.listColumns.model()
        list_columns_2_model = self.listColumns_2.model()

        if list_columns_2_model is None:
            list_columns_2_model = QtGui.QStandardItemModel()
            self.listColumns_2.setModel(list_columns_2_model)

        if list_columns_model:
            for item in selected_items:
                column_name = item.data()
                # Add to listColumns_2 if not already present
                existing_items = [list_columns_2_model.item(i).text() for i in range(list_columns_2_model.rowCount())]
                if column_name not in existing_items:
                    list_columns_2_model.appendRow(QtGui.QStandardItem(column_name))

                # Remove the item from listColumns
                list_columns_model.removeRow(item.row())

        self.update_dropdowns()  # Update dropdowns after adding columns

    def remove_column(self):
        selected_items = self.listColumns_2.selectedIndexes()
        list_columns_model = self.listColumns.model()
        list_columns_2_model = self.listColumns_2.model()

        if list_columns_model and list_columns_2_model:
            for index in selected_items:
                column_name = index.data()
                list_columns_2_model.removeRow(index.row())

                # Add the removed item back to listColumns
                item = QtGui.QStandardItem(column_name)
                item.setSelectable(True)  # Ensure items are selectable
                list_columns_model.appendRow(item)

        self.update_dropdowns()  # Update dropdowns after removing columns

    def clear_columns(self):
        list_columns_2_model = self.listColumns_2.model()
        if list_columns_2_model:
            list_columns_2_model.removeRows(0, list_columns_2_model.rowCount())
        self.update_list_view()
        self.update_dropdowns()  # Refresh dropdowns

    def plot_graph(self):
        x_col = self.dropdownXAxis.currentText()
        y_cols = [self.listColumns_2.model().item(row).text() for row in range(self.listColumns_2.model().rowCount())]

        if x_col and y_cols and self.df is not None:
            try:
                plt.figure(figsize=(10, 6))
                for y_col in y_cols:
                    y = self.df[y_col]
                    plt.plot(self.df[x_col], y, label=y_col)

                plt.xlabel(self.lineXTitle.text())
                plt.ylabel(self.lineYTitle.text())
                plt.title(f'{x_col} vs Selected Columns')

                if self.legendCheck.isChecked():
                    plt.legend()

                if self.gridCheck.isChecked():
                    plt.grid(True)

                plt.show()
                self.update_statusbar("Plot generated successfully")
            except Exception as e:
                self.update_statusbar(f"Error: {str(e)}")
        else:
            self.update_statusbar("Please select valid columns for X and Y axes.")
