import sys
import os

# Se o script está sendo executado a partir do diretório src, adicione o diretório acima ao sys.path
if os.path.basename(os.getcwd()) == 'src':
    sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..')))

from data_pipeline.data_ingestion import *

# Função main do arquivo principal
def main():
    insert_areas_data()
    insert_habits_data()
    insert_journal_data()
    insert_moods_data()

    # Fechando a sessão
    session.close()

    print("Arquivo main.py executado com sucesso!")
    teste()

if __name__ == "__main__":
    main()
