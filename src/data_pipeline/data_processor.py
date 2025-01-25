from src.api import *
from src.utils import convert_to_brazil_time
import pandas as pd



def process_moods_data(raw_data):
    if not raw_data:
        print("Nenhum dado de humores para processar")
        return None

    try:
        data = []
        
        for i in raw_data:
            if not all(key in i for key in ['id', 'created_at', 'value']):
                print(f"Dado inválido encontrado e ignorado: {i}")
                continue
            
            created_at = convert_to_brazil_time(i["created_at"])
            data.append({'id_mood': i["id"], 'created_at': created_at, 'value_mood': i["value"]})

        if not data:
            print("Nenhum dado válido foi encontrado para processar")
            return None

        df = pd.DataFrame(data, columns=['id_mood', 'created_at', 'value_mood'])
        return df
        
    except Exception as e:
        print(f"Erro ao processar dados de humores: {e}")
        return None

def process_areas_data(raw_data):

    if not raw_data:
        print("Nenhum dado de humores para processar")
        return None

    try:
        data = []
        
        for i in raw_data:
            if not all(key in i for key in ['id', 'name', 'createdAt', 'priority', 'color']):
                print(f"Dado inválido encontrado e ignorado: {i}")
                continue
            
            created_at = convert_to_brazil_time(i["createdAt"])
            data.append({'id_area': i["id"], 'name_area': i["name"], 'created_at': created_at, 'priority': i["priority"], 'color': i["color"]})

        if not data:
            print("Nenhum dado válido foi encontrado para processar")
            return None

        df = pd.DataFrame(data, columns=['id_area', 'name_area', 'created_at', 'priority', 'color'])
        return df
        
    except Exception as e:
        print(f"Erro ao processar dados de areas: {e}")
        return None



def process_habits_data(raw_data):

    # Condicional para verificar se algum dado foi encontrado no fetch.
    if not raw_data:
        print("Nenhum dado de hábitos para processar")
        return None


    # Processamento dos dados.
    try:
        data = []
        
        # Aqui eu verifico se todas os campos que api retorna, foram encontrados.
        for i in raw_data:
            if not all(key in i for key in ['id', 'name', 'is_archived', 'start_date', 'time_of_day', 'goal', 'goal_history_items', 'log_method', 'recurrence', 'remind', 'area', 'created_date', 'priority']):
                print(f"Dado inválido encontrado e ignorado: {i}")
                continue
            
            # Tratativa dos dados.
            created_at = convert_to_brazil_time(i["created_date"])
            started_at = convert_to_brazil_time(i["start_date"])

            data.append({
                'id_habit': i.get("id", None),
                'name_habit': i.get("name", None),
                'goal_unit_type':i.get("goal", {}).get("unit_type", None),
                'goal_value': i.get("goal", {}).get("value", None),
                'goal_periodicity': i.get("goal", {}).get("periodicity", None),
                'id_area': i.get("area", {}).get("id", None) if i.get("area", None) is not None else None,
                'created_at': created_at
            })

        if not data:
            print("Nenhum dado válido foi encontrado para processar")
            return None

        # Criação do df para dar return
        df = pd.DataFrame(data= data)
        return df
        
    except Exception as e:
        print(f"Erro ao processar dados de hábitos: {e}")
        return None


def process_journal_data(raw_data):

    # Condicional para verificar se algum dado foi encontrado no fetch.
    if not raw_data:
        print("Nenhum dado de journal para processar")
        return None


    # Processamento dos dados.
    try:
        data = []
        
        # Aqui eu verifico se todas os campos que api retorna, foram encontrados.
        for i in raw_data:
            if not all(key in i for key in ['id', 'status', 'progress']):
                print(f"Dado inválido encontrado e ignorado: {i}")
                continue
            
            # Tratativa dos dados.
            reference_date = convert_to_brazil_time(i['progress']['reference_date'])

            data.append({
                'id_habit': i.get("id", None),
                'status': i.get("status", None),
                'progress_current_value':i.get("progress", {}).get("current_value", None),
                'reference_Date': reference_date
            })

        if not data:
            print("Nenhum dado válido foi encontrado para processar")
            return None

        # Criação do df para dar return
        df = pd.DataFrame(data= data)
        return df
        
    except Exception as e:
        print(f"Erro ao processar dados de journal: {e}")
        return None
