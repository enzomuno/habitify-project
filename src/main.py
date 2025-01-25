from src.data_pipeline.data_ingestion import *


# Função main do arquivo principal
def main():
    insert_areas_data()
    insert_habits_data()
    insert_journal_data()
    insert_moods_data()

    # Fechando a sessão
    session.close()

if __name__ == "__main__":
    main()
