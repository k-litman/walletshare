from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

if environ.get('DATABASE_TYPE') == 'sqlite':
    engine = create_engine('sqlite:///walletshare.db', connect_args={'check_same_thread': False})
elif environ.get('DATABASE_TYPE') == 'postgres':
    engine = create_engine(
        f'postgresql://{environ.get("POSTGRES_USER")}:{environ.get("POSTGRES_PASSWORD")}@'
        f'{environ.get("POSTGRES_HOST")}:{environ.get("POSTGRES_PORT")}/{environ.get("POSTGRES_DB")}')
else:
    raise Exception('DATABASE_TYPE not set or invalid')

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
