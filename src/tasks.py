from src.item_adpm import ItemADPM
import src.actions as act

def fill_form(item: ItemADPM) -> bool:

#    if act.locate_blank_item:
#        act.fill_in_desc(item.codigo_ed)
        
    if act.incluir_cadastro(item.desc_plus_ed,item.get_unit_code):
        print('FUCK YEAH!')
    return False  