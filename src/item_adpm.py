from dataclasses import dataclass
from typing import Optional

@dataclass
class ItemADPM:
    codigo_ed: str
    descricao: str
    unit_fornecimento: str
    #valor_unit : str
    quantidade: str

    UNIDADE_MAPPING = {
        "M²": '134',
        "KG": '120',
        "M": '132',
        "UND": '204',
        "M³": '133'
        #"MÊS": ''
    }

    @property
    def desc_plus_ed(self) -> str:
        return f"{self.descricao} {self.codigo_ed}"

    @property 
    def get_unit_code(self) -> str:
        code = self.UNIDADE_MAPPING.get(self.unit_fornecimento.upper().strip())

        if code is None:
            raise ValueError(f"Unidade desconhecida: {self.unit_fornecimento}")
        
        return code