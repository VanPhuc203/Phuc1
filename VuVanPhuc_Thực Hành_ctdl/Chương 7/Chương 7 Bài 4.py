class DoThi:
    def __init__(self):
        self.do_thi = {}

    def them_dinh(self, v):
        if v not in self.do_thi:
            self.do_thi[v] = []

    def ChuaDinh(self, v):
        return v in self.do_thi
