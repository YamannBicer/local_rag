import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_ollama import ChatOllama
from langchain_community.agent_toolkits import create_sql_agent


df = pd.read_csv("csv_data/titanic.csv")


engine = create_engine("sqlite:///titanic.db")
df.to_sql("titanic", engine, index=False, if_exists='replace')

db = SQLDatabase(engine=engine)
# print(db.dialect)
print(db.get_usable_table_names())
print(db.run("SELECT AVG(age) as average_age FROM titanic WHERE survived = 1;"))


llm = ChatOllama(model="llama3.1", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="tool-calling", verbose=True)

agent_executor.invoke({"input": "what's the average age of survivors"})
# agent_executor.invoke({"input": "how many male and females were there on the titanic"})

