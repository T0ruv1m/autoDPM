import pyautogui as gui
from src.paths import get_path

def alert_when_found(picture: str):
    if found(picture):
        gui.alert('OK', 'OK', 'OK')
    
def found(picture: str) -> bool:
   return gui.locateOnScreen(get_path(picture), 20, confidence= 0.9)

def locate_blank_item() -> bool:
 return found(get_path('blank_item'))

def fill_in_desc(codigo_ed: str) -> bool:
    location = gui.locateOnScreen(get_path('descricao_edit.png'), 20, confidence= 0.9)
    gui.click(location)
    gui.typewrite(codigo_ed)
    return True

def incluir_cadastro(desc_ed, codigo_uf: str) -> bool:
    if found(get_path('servico_screen.png')):
      gui.hotkey('Alt', 'n')
      gui.press('F3')
      gui.press('F3')
      gui.typewrite(desc_ed)
      gui.press('tab', presses= 2)
      gui.press('4')
      gui.press('tab', presses= 5)
      gui.press('right', presses= 2)
      gui.press('tab')
      gui.typewrite(codigo_uf)

    return True