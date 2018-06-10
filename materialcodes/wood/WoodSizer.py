from materialcodes.wood.wooddataparser import ur


class SawnLumberDimensions():
    def __init__(self, size = '2x4'):
        #super(sawnlumberdimensions, self).__init__(size)
        r1 = size.split('x')
        ind = int(0)
        for i in r1:
            i = int(i)
            if i < 8:
                i = i - .5
                #print(i)
            else:
                i = i - .75
                if self.iscolumn == True:
                    i = i + .25  #columns only take .5 reduction
                #print(i)
            r1[ind] = i
            ind += 1

        self.b = r1[0] * ur.inch
        self.d = r1[1] * ur.inch

    @property
    def area(self):
        area = self.d * self.b
        assert area.dimensionality == '[length]**2'
        return self.area

    @area.setter
    def area(self, area):
        self.

    @property
    def mom_x(self):
        return (self.b * self.d**3)/12

    @property
    def mom_y(self):
        return (self.b**3 * self.d)/12

    @property
    def r_x(self):
        return (self.d)/(12**.5)

    @property
    def r_y(self):
        return (self.b)/(12**.5)

    @property
    def s_x(self):
        return (self.b * self.d**2)/(6)

    @property
    def s_y(self):
        return (self.b**2 * self.d)/(6)

    def __repr__(self):
        return f'sawlumberdimensions({size})'


class SawnColumnDimensions():
    def __init__(self, size = '2x4'):
        #super(sawnlumberdimensions, self).__init__(size)
        r1 = size.split('x')
        ind = 0
        for i in r1:
            i = int(i)
        i = i - .5
        r1[ind] = i
        ind += 1

        self.b = r1[0] * ur.inch
        self.d = r1[1] * ur.inch

    @property
    def area(self):
        area = self.d * self.b
        assert area.dimensionality == '[length]**2'
        return area

    @property
    def mom_x(self):
        return (self.b * self.d**3)/12

    @property
    def mom_y(self):
        return (self.b**3 * self.d)/12

    @property
    def r_x(self):
        return (self.d)/(12**.5)

    @property
    def r_y(self):
        return (self.b)/(12**.5)

    @property
    def s_x(self):
        return (self.b * self.d**2)/(6)

    @property
    def s_y(self):
        return (self.b**2 * self.d)/(6)

    def __repr__(self):
        return f'sawbeamdimensions({size})'

class GlulamBeamSizer():
    pass