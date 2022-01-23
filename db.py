from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+pymysql://onlyupuz_fastapi:onlyupuz_fastapi@localhost:3306/onlyupuz_fastapi")
conn = engine.connect()
Base = declarative_base()
meta = Base.metadata