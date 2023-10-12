import sys

def monctl():
        from qtpy import QtWidgets
        from .monctl import MyWindow

        app = QtWidgets.QApplication([])

        widget = MyWindow()
        widget.show()

        sys.exit(app.exec_())
def moncli():
        from .moncli import Moncli
        moncli = Moncli()
        moncli.app(sys.argv)


