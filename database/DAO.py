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
        query = """select distinct g.Name from genre g order by g.Name"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(self, g):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.ArtistId, a.Name 
                    from artist a, genre g, album a2, track t 
                    where t.GenreId = g.GenreId and g.Name = %s
                    and t.AlbumId = a2.AlbumId and a2.ArtistId = a.ArtistId """

        cursor.execute(query, [g])

        for row in cursor:
            result.append(row["Name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCustomerArt(a, g):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = f"""select i.CustomerId, a2.Name, count(*) as ntracks
                    from invoice i, invoiceline i2, track t, album a, genre g, artist a2 
                    where i.InvoiceId = i2.InvoiceId and i2.TrackId = t.TrackId 
                    and t.AlbumId = a.AlbumId and t.GenreId = g.GenreId and g.Name = %s
                    and a.ArtistId = a2.ArtistId
                    group by i.CustomerId, a2.ArtistId 
                """
        cursor.execute(query, [g])

        for row in cursor:
            result.append((row["CustomerId"], row["Name"], row["ntracks"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV2(a, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = f"""
                    """

        cursor.execute(query)

        for row in cursor:
            result.append((idMap[row["CustomerId"]],
                            idMap[row["ArtistId"]]))

        cursor.close()
        conn.close()
        return result

