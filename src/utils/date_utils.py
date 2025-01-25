from datetime import datetime, time
import pytz

# Fórmula para eu transformar a data para UTC-03:00 e sempre ás 20:59:59. 
# A chamada do endpoint apenas capturar hábitos até esse horário.
def to_iso8601_21():
    

    brazil_tz = pytz.timezone("America/Sao_Paulo")
    current_date = datetime.now(brazil_tz).date()

    # Combinar a data atual com o horário fixo 20:59:59
    fixed_time = time(20, 59, 59)
    result = datetime.combine(current_date, fixed_time)
    localized_result = brazil_tz.localize(result)
    # Formato ISO 8601
    iso_result = localized_result.isoformat()
    return iso_result




# Fórmula para eu transformar a data para UTC-03:00 e sempre ás 20:59:59. 
# A chamada do endpoint apenas capturar hábitos até esse horário.
def to_iso8601_23():

    brazil_tz = pytz.timezone("America/Sao_Paulo")
    current_date = datetime.now(brazil_tz).date()

    # Combinar a data atual com o horário fixo 22:59:59
    fixed_time = time(22, 59, 59)
    result = datetime.combine(current_date, fixed_time)
    localized_result = brazil_tz.localize(result)
    # Formato ISO 8601
    iso_result = localized_result.isoformat()
    return iso_result


#  Fórmula para transformar as datas do response in UTC-03:00 para já ser armazenado no banco em utc local.
def convert_to_brazil_time(utc_time_str):

    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    utc_time = utc_time.replace(tzinfo=pytz.UTC)

    brazil_tz = pytz.timezone("America/Sao_Paulo")
    brazil_time = utc_time.astimezone(brazil_tz)

    # Retorna a data/hora formatada
    return brazil_time.strftime('%Y-%m-%d %H:%M')