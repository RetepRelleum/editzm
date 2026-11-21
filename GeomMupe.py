from qgis.core import QgsPointXY, QgsGeometry
from .EditZM_Series import EditZM_Series


class GeomMupe():
    def __init__(self, geom_as_txt, rasterlayer):
        self.raster = rasterlayer
        self.type = geom_as_txt[:geom_as_txt.find('(')]
        self.geom_as_txt = geom_as_txt
        self.array = [[[[]]]]
        self.buildArray(geom_as_txt)

    def buildArray(self, geom_as_txt):
        pol = self.geom_as_txt[geom_as_txt.find('('):]

        pol = pol.replace('))),(((', 'A')
        pol = pol.replace(')),((', 'B')
        pol = pol.replace('),(', 'C')
        pol = pol.replace(', ', 'D')
        pol = pol.replace('(', '')
        pol = pol.replace(')', '')
        a = pol.split('A')

        for ai, b in enumerate(a):
            b = b.split('B')
            for bi, c in enumerate(b):
                c = c.split('C')
                for ci, d in enumerate(c):
                    d = d.split('D')
                    for di, e in enumerate(d):
                        print(e)
                        e = list(map(float, e.split(' ')))
                        if self.type.find('ZM') >= 0:
                            pass
                        elif self.type.find('Z') >= 0 or self.type.find('M') >= 0:
                            e.append(0.0)
                            e[3] = e[2]
                        self.array[ai][bi][ci].append(e)
                    if ci < (len(c)-1):
                        self.array[ai][bi].append([])
                if bi < (len(b)-1):
                    self.array[ai].append([])
                    self.array[ai][bi+1].append([])

    def setZall(self, z: float):
        for multi in self.array:
            for poly in multi:
                for line in poly:
                    for point in line:
                        point[2] = z

    def setMall(self, m: float):
        for multi in self.array:
            for poly in multi:
                for line in poly:
                    for point in line:
                        point[3] = m

    def setValZ(self, a: int, b: int, c: int, d: int, val: float):
        if d < len(self.array[a][b][c]):
            self.array[a][b][c][d][2] = val

    def setValM(self, a: int, b: int, c: int, d: int, val: float):
        if d < len(self.array[a][b][c]):
            self.array[a][b][c][d][3] = val

    def getValZ(self, a: int, b: int, c: int, d: int):
        if d < len(self.array[a][b][c]):
            return self.array[a][b][c][d][2]
        else:
            return 0

    def getValX(self, a: int, b: int, c: int, d: int):
        if d < len(self.array[a][b][c]):
            return self.array[a][b][c][d][0]
        else:
            return 0

    def getValY(self, a: int, b: int, c: int, d: int):
        if d < len(self.array[a][b][c]):
            return self.array[a][b][c][d][1]
        else:
            return 0

    def getValM(self, a: int, b: int, c: int, d: int):
        if d < len(self.array[a][b][c]):
            return self.array[a][b][c][d][3]
        else:
            return 0

    def getMum(self, x, y):
        val, res = self.raster[0].dataProvider().sample(QgsPointXY(x, y), 1)
        return val

    def setMueMZ(self):
        for multi in self.array:
            for poly in multi:
                for line in poly:
                    for point in line:
                        val, res = self.raster[0].dataProvider().sample(
                            QgsPointXY(point[0], point[1]), 1)
                        if not res:
                            val = 0
                        point[2] = val

    def setMueMM(self):
        for multi in self.array:
            for poly in multi:
                for line in poly:
                    for point in line:
                        val, res = self.raster[0].dataProvider().sample(
                            QgsPointXY(point[0], point[1]), 1)
                        if not res:
                            val = 0
                        point[3] = val

    def getQseries(self):
        self.ret = []
        pos = 0
        for ai, a in enumerate(self.array):
            for bi, b in enumerate(a):
                for ci, c in enumerate(b):
                    x = []
                    y = []
                    z = []
                    m = []
                    for di, d in enumerate(c):
                        x.append(d[0])
                        y.append(d[1])
                        z.append(d[2])
                        m.append(d[3])
                    editZM_Series = EditZM_Series(
                        x, y, z, m, ai, bi, ci, di, pos)
                    pos = pos+1
                    self.ret.append(editZM_Series)
        return self.ret

    def getGeom(self):
        ret = self.type
        if self.type.find('Multi') >= 0:
            ret = ret+'('
        if self.type.find('Polygon') >= 0:
            ret = ret+'('
        for ai, a in enumerate(self.array):
            if ai == 0:
                pass
            else:
                ret = ret+'('
            for bi, b in enumerate(a):
                if bi > 0:
                    ret = ret+'('
                for ci, c in enumerate(b):
                    if ci >= 0:
                        ret = ret+'('
                    for di, d in enumerate(c):
                        ret = ret + str(d[0])+' '+str(d[1])
                        if self.type.find('ZM') >= 0:
                            ret = ret + ' ' + str(d[2]) + ' '+str(d[3])
                        elif self.type.find('Z') >= 0:
                            ret = ret + ' ' + str(d[2])
                        else:
                            ret = ret + ' ' + str(d[3])
                        if di < len(c)-1:
                            ret = ret+', '
                    if ci >= 0:
                        ret = ret+')'
                    if ci < len(b)-1:
                        ret = ret+','
                if bi >= 0:
                    ret = ret+')'
                if bi < len(a)-1:
                    ret = ret+','

        if self.type.find('Multi') >= 0:
            ret = ret+')'
        if self.type.find('Polygon') >= 0:
            ret = ret+')'
        return ret

    def getGeometry(self):
        return QgsGeometry.fromWkt(self.getGeom())

    def test(self):
        self.setZall(4)
        print(self.array, 'Z4')
        self.setMall(5)
        print(self.array, 'M5')
        self.setMueMZ()
        print(self.array, 'zMüm')
        self.setMueMM()
        print(self.array, 'MMüm')
        print(self.getGeom())
