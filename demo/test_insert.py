# INSERT
# 参照 3. sqlalchemy.coreを使う
# https://qiita.com/yukiB/items/d6a70da802cb5731dc01#3-sqlalchemycore%E3%82%92%E4%BD%BF%E3%81%86

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

import os

from dotenv import load_dotenv
load_dotenv(override=True)

metadata = MetaData()

uri = sqlalchemy.engine.url.URL(
    drivername='mysql+pymysql',
    username=os.environ['GCP_USER'],
    password=os.environ['GCP_PASS'],
    database='demo',
    host=os.environ['GCP_HOST'],
    query=dict({"unix_socket": f"/cloudsql/{format(os.environ['GCP_CONNECTION'])}"})
)

engine = create_engine(uri, encoding='utf-8', pool_recycle=3600)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=True,
        expire_on_commit=False,
        bind=_engine
    )
)

metadata.create_all(bind=_engine)

data_list = [
    ['tanaka', 20],
    ['sato', 25],
    ['abe', 50],
]

users = [{'name' : d[0], 'age' : d[1]} for d in data_list]

session.execute(User.__table__.insert(), users)
session.commit()