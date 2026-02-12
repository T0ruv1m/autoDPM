from src.item_adpm import ItemADPM
import src.actions as act
import pyautogui as gui

def fill_form(item: ItemADPM) -> bool:
    
    if act.fill_in_desc(item.codigo_ed):
        desc_found = act.find_desc()

    match desc_found:
        case '0':
            if act.insert_service(item.desc_plus_ed,item.get_unit_code):
                print('YES!')
        case 'more':
            if act.see_blank_registro_back:
                print('serviço registrado')
                act.see_blank_registro_back
        case '1':
            print('serviço registrado.')      
    
    if act.finish(item.quantidade):
        print('cadastro finalizado!')
    return False  

def test_quantidade(item: ItemADPM) -> bool:
    gui.typewrite(item.quantidade)
    return True