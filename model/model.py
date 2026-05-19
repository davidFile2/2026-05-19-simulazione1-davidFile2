import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artist = DAO.getAllArtist()
        self._idMapArtist = {}
        for a in self._artist:
            self._idMapArtist[a] = a


    def getGeneri(self):
        return DAO.getGeneri()

    def creaGrafo(self, g):
        nodes = DAO.getAllNodes(g, self._idMapArtist)
        self._graph.add_nodes_from(nodes)
        #print(f"N nodi: {len(self._graph.nodes)}, n archi: {len(self._graph.edges)}")
        self.addEdges()

    def addEdges(self):
        tratti = DAO.getAllEdges(self._idMapArtist)