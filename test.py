from src.data_loader import load_items
items = load_items('assets/data_source.xlsx')
for item in items[:3]:
    print(f"Descricao: {repr(item.descricao)}")
