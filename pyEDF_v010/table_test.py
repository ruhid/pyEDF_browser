import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return QVariant()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a pandas dataframe
    df = pd.DataFrame({'Name': ['John', 'Alice', 'Bob'],
                       'Age': [25, 30, 35]})

    # Create a PyQt model from the pandas dataframe
    model = PandasModel(df)

    # Create a QTableView widget and set the model
    view = QTableView()
    view.setModel(model)

    # Show the view
    view.show()

    sys.exit(app.exec_())
