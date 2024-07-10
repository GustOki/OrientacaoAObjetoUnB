import pickle


class M22:
    """Representation of a 2x2 matrix"""


    def __init__(self, value11, value12=None, value21=None, value22=None):
        if value12==None and valuer21==None and valuer22==None:
            self.value11 = value11
            self.value12 = value11
            self.value21 = value11
            self.value22 = value11
        else:
            self.value11 = value11
            self.value12 = value12
            self.value21 = value21
            self.value22 = value22


    @classmethod
    def new(cls, matlab_format):
        # Assuming matlab_format is a string like "[a, b; c, d]"
        values = [float(val) for val in matlab_format[1:-1].replace(',', ' ').replace(';', ' ').split()]
        if len(values) == 4:
            value11, value12, value21, value22 = values
            return cls(value11, value12, value21, value22)
        else:
            raise ValueError("Invalid input format for M22.new")


    @staticmethod
    def eh_simetrica(m):
        """ Verifica se a matriz fornecida é simétrica """
        if m.value12 == m.value21:
            return "Verdadeiro"
        else:
            return "Falso"


    def __add__(self, m22):
        val11 = self.value11 + m22.value11
        val12 = self.value12 + m22.value12
        val21 = self.value21 + m22.value21
        val22 = self.value22 + m22.value22
        return M22(val11, val12, val21, val22)

    def __str__(self):
        return f"[{self.value11}, {self.value12}; {self.value21}, {self.value22}]"



