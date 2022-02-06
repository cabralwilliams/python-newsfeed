from curses import echo
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

print('Trying to connect')
print(getenv('DB_URL'))
# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
print(str(engine))
Session = sessionmaker(bind=engine)
Base = declarative_base()

