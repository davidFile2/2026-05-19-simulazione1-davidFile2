from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllArtist():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from chinook.artist a """

        cursor.execute(query)

        for row in cursor:
            result.append(row["ArtistId"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.Name 
                    from chinook.genre g """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(g, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.ArtistId 
                from chinook.track t , chinook.album a, chinook.genre g 
                where g.Name = %s and t.GenreId = g.GenreId and a.AlbumId  = t.AlbumId """

        cursor.execute(query, (g,))

        for row in cursor:
            result.append(idMap[row["ArtistId"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ """

        cursor.execute(query)

        for row in cursor:
            result.append(idMap[row])

        cursor.close()
        conn.close()
        return result

