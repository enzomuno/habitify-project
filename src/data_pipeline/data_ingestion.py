import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from datetime import datetime

import pandas as pd

from src.api import *
from src.data_pipeline import *


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Base para definir modelos
Base = declarative_base()


# Definição da Class 'Areas'
class Areas(Base):
    __tablename__ = 'tdim_areas'
    
    id_area = Column(String(255), primary_key=True)
    name_area = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


# Definição da Class 'Habits'
class Habits(Base):
    __tablename__ = 'tdim_habits'
    
    id_habit = Column(String(255), primary_key=True)
    name_habit = Column(String(255), nullable=False)
    goal_unit_type = Column(String(5), nullable=False)
    goal_value = Column(Integer, nullable=False)
    goal_periodicity = Column(String(7), nullable=False)
    id_area = Column(String(255), ForeignKey('tdim_areas.id_area'))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


# Definição da Class 'Journal'
class Journal(Base):
    __tablename__ = 'tfact_journal'
    
    id_habit = Column(String(255), ForeignKey('tdim_habits.id_habit'))
    status = Column(String(20), nullable=False)
    progress_current_value = Column(Integer, nullable=False)
    reference_date = Column(DateTime, nullable=False)  # Remova o primary_key=True aqui
    
    __table_args__ = (
        PrimaryKeyConstraint('id_habit', 'reference_date'),  # Defina a chave primária composta
    )

# Definição da Class 'Moods'
class Moods(Base):
    __tablename__ = 'tfact_moods'
    
    id_mood = Column(String(255), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    value_mood = Column(Integer, nullable=False)


# Criando a sessão no sqlalchemy
Session = sessionmaker(bind=engine)
session = Session()



# Função para inserir dados na tabela 'tdim_Areas'
def insert_areas_data():

    # Chama a função que retorna os df desse endpoint
    areas_data = process_areas_data(fetch_areas())

    if isinstance(areas_data, pd.DataFrame):
        
        for i, row in areas_data.iterrows():
            # Converti a linha do df para um dict
            area = row.to_dict()

            # Verifica se o id_area já existe na tabela
            existing_area = session.query(Areas).filter_by(id_area=area['id_area']).first()

            # Se não existir, adiciona o novo registro
            if not existing_area:
                new_area = Areas(
                    id_area=area['id_area'],  
                    name_area=area['name_area'],
                    created_at=area['created_at']
                )

                session.add(new_area)
            else:
                print(f"Área com id {area['id_area']} já existe. Ignorando inserção.")
        
        session.commit()
        print("Dados de áreas inseridos com sucesso.")
    else:
        print("Error: não retornado um DataFrame válido.")


# Função para inserir dados na tabela 'tdim_Areas'
def insert_habits_data():

    # Chama a função que retorna os df desse endpoint
    habits_data = process_habits_data(fetch_habits())

    if isinstance(habits_data, pd.DataFrame):
        
        for i, row in habits_data.iterrows():
            # Converti a linha do df para um dict
            habit = row.to_dict()

            # Verifica se o id_area já existe na tabela
            existing_habit = session.query(Habits).filter_by(id_habit=habit['id_habit']).first()

            # Se não existir, registra o novo registro
            if not existing_habit:
                new_habit = Habits(
                    id_habit=habit['id_habit']
                    ,name_habit=habit['name_habit']
                    ,goal_unit_type=habit['goal_unit_type']
                    ,goal_value=habit['goal_value']
                    ,goal_periodicity=habit['goal_periodicity']
                    ,id_area=habit['id_area']
                    ,created_at=habit['created_at']
                )

                session.add(new_habit)
            else:
                print(f"Habit com id {habit['id_area']} já existe. Ignorando inserção.")
        
        session.commit()
        print("Dados de hábitos inseridos com sucesso.")
    else:
        print("Error: não retornado um DataFrame válido.")


# Função para inserir dados na tabela 'tdim_Areas'
def insert_journal_data():

    # Chama a função que retorna os df desse endpoint
    journal_data = process_journal_data(fetch_journal())

    if isinstance(journal_data, pd.DataFrame):
        
        for i, row in journal_data.iterrows():
            # Converti a linha do df para um dict
            journal = row.to_dict()

            new_journal = Journal(
                id_habit=journal['id_habit']
                ,status=journal['status']
                ,progress_current_value=journal['progress_current_value']
                ,reference_date=journal['reference_Date']
            )

            session.add(new_journal)
        
        session.commit()
        print("Dados de journal inseridos com sucesso.")
    else:
        print("Error: não retornado um DataFrame válido.")



# Função para inserir dados na tabela 'tdim_Areas'
def insert_moods_data():

    # Chama a função que retorna os df desse endpoint
    moods_data = process_moods_data(fetch_moods())

    if isinstance(moods_data, pd.DataFrame):
        
        for i, row in moods_data.iterrows():
            # Converti a linha do df para um dict
            mood = row.to_dict()

            # Verifica se o id_area já existe na tabela
            existing_mood = session.query(Moods).filter_by(id_mood=mood['id_mood']).first()

            # Se não existir, registra o novo registro
            if not existing_mood:
                new_mood = Moods(
                    id_mood=mood['id_mood']
                    ,created_at=mood['created_at']
                    ,value_mood=mood['value_mood']
                )

                session.add(new_mood)
            else:
                print(f"Mood com id {mood['id_mood']} já existe. Ignorando inserção.")
        
        session.commit()
        print("Dados de moods inseridos com sucesso.")
    else:
        print("Error: não retornado um DataFrame válido.")










# Função main
if __name__ == "__main__":
    insert_areas_data()
    insert_habits_data()
    insert_journal_data()
    insert_moods_data()

    # Fechando a sessão
    session.close()
