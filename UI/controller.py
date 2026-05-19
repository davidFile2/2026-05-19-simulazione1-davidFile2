import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getGeneri()
        for g in generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(g))


    def handleCreaGrafo(self, e):
        gen = self._view._ddGenre.value
        self._model.creaGrafo(gen)



    def handleCammino(self,e):
        pass

    def filldropdown(self, nodes):
        pass