import pyautogui as gui
from src.paths import get_path
import pyperclip

def alert_when_found(picture: str):
    if see(picture):
        gui.alert('OK', 'OK', 'OK')
    
def see(picture: str, timeout=60, confidence=0.9) -> bool:
    try:
        match = gui.locateOnScreen(get_path(picture),timeout, confidence=confidence)
        return match is not None
    except Exception as e:
        return False

def locate_blank_item() -> bool:
 return see(get_path('blank_item'))

def fill_in_desc(codigo_ed: str) -> bool:
    location = gui.locateOnScreen(get_path('descricao_edit.png'), 60, confidence= 0.9)
    gui.click(location)
    gui.typewrite(codigo_ed)
    gui.press('tab')
    return True

def insert_service(desc_ed, codigo_uf: str) -> bool:
    
    if not gui.confirm('desseja incluir registro de serviço?') == 'OK':
        return False

    gui.hotkey('alt','i')
    if see('servico_screen.png',10,0.8):
      gui.hotkey('Alt', 'n')

      if see('new_servico_screen.png'):
        gui.press('F3')
        gui.press('F3')
        pyperclip.copy(desc_ed)
        gui.hotkey('ctrl','v')
        gui.press('tab', presses= 2)
        gui.press('4')
        gui.press('tab', presses= 5)
        gui.press('right', presses= 2)

        if see('unidade_screen.png'):
                gui.press('tab')
                gui.typewrite(codigo_uf)
                gui.press('tab')
                #if gui.confirm('Deseja inserir o Item?') == 'OK':
                gui.hotkey('alt','f')
                gui.hotkey('alt','s')

    return True

def find_desc() -> str:
    while True:
        if see('descricao_n_cadastrada.png',1,confidence= 0.7):
            return '0'
        if see('pesquisa_screen.png',1, confidence=0.7):
            return 'more'
        if see('unidade_blank.png',1, confidence=0.7):
            return '1'


def see_blank_registro_back() -> bool:
    return see('blank_registro_screen.png',60,0.8)

def finish(quantidade:str) -> bool:
    if not see('blank_qtt.png',10,0.8):
        return False

    gui.press('f4')
    gui.press('tab', presses= 1)
    gui.hotkey('ctrl','a')
    gui.press('backspace')
    gui.typewrite(quantidade)
    gui.press('tab')
    #if gui.confirm('Deseja Inserir o Item?') == 'OK':

    incluir_button = gui.locateOnScreen(get_path('selected_incluir_pedido_button.png'),10,confidence= 0.8)
    gui.click(incluir_button)
    #already_registered = gui.locateOnScreen(get_path('nao_reinserir.png'),5,confidence= 0.8)
    #if already_registered is not None:
    #    gui.click(already_registered)
    #return True
