import pyqtgraph as pg
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QApplication

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()