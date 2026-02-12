import pandas as pd
from src.item_adpm import ItemADPM

def load_items(file_path:str) -> list[ItemADPM]:
    df = pd.read_excel(file_path).fillna("")

    items = []
    for _, row in df.iterrows():
        item = ItemADPM(
            codigo_ed=str(row['codigo_ed']),
            descricao=str(row['descricao']),
            unit_fornecimento=str(row['unidade']),
            valor_unit=str(row['valor_unit'])
        )
        items.append(item)
    return items