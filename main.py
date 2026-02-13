from src.paths import get_path
from src.tasks import fill_form, test_quantidade, price_quotation
from src.data_loader import load_items
import pyautogui

def main():
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1.0

    try:
        excel_path = get_path("data_source.xlsx")
        dataset = load_items(excel_path)
        
        for item in dataset:
            try:
                #if not fill_form(item):
                if not price_quotation(item):
                #if not test_quantidade(item):
                    raise ValueError('ERRO')
            except Exception as e:
                print(f"Failed to process item {item.codigo_ed}: {e}")
            continue
    
    except Exception as e:
        print(f"Error{e}")
    finally:
        print("Automation Terminated")

if __name__ == "__main__":
    main()