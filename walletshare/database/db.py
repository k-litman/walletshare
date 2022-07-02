from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

from walletshare.exceptions import EnvironmentVariableError

if environ.get('DATABASE_TYPE') == 'sqlite':
    engine = create_engine('sqlite:///walletshare.db', connect_args={'check_same_thread': False})
elif environ.get('DATABASE_TYPE') == 'postgres':
    if not (environ.get('POSTGRES_USER') and environ.get('POSTGRES_PASSWORD') and environ.get('POSTGRES_HOST')
            and environ.get('POSTGRES_PORT') and environ.get('POSTGRES_DB')):
        raise EnvironmentVariableError('PostgreSQL database environment variables not set')

    engine = create_engine(
        f'postgresql://{environ.get("POSTGRES_USER")}:{environ.get("POSTGRES_PASSWORD")}@'
        f'{environ.get("POSTGRES_HOST")}:{environ.get("POSTGRES_PORT")}/{environ.get("POSTGRES_DB")}')
else:
    raise EnvironmentVariableError('DATABASE_TYPE not set or invalid')

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
