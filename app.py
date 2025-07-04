from dotenv import load_dotenv
import warnings

warnings.filterwarnings('ignore')
load_dotenv()

from app.menu import main_menu

if __name__ == "__main__":
    print("\n")
    main_menu()
