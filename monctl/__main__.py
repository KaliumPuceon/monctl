import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] == 'gui':
            from qtpy import QtWidgets
            from .monctl import MyWindow

            app = QtWidgets.QApplication([])

            widget = MyWindow()
            widget.show()

            sys.exit(app.exec_())
        else:
            from .moncli import Moncli
            moncli = Moncli()
            moncli.app(sys.argv[2:])

    except IndexError:
        print("Provide an argument (cli/gui)")

        
