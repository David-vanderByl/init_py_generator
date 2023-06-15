# This code was automatically generated from a text file.

from model import Model
from view import View
from controller import Controller

if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()
