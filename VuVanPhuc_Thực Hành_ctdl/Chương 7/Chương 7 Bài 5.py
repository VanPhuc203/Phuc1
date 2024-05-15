class DoThi:
    def __init__(self):
        self.do_thi = {}

    def them_dinh(self, v):
        if v not in self.do_thi:
            self.do_thi[v] = []

    def them_canh(self, u, v):
        if u in self.do_thi and v in self.do_thi:
            self.do_thi[u].append(v)
            self.do_thi[v].append(u)

    def BacDinh(self, v):
        if v in self.do_thi:
            return len(self.do_thi[v])
        else:
            return None
