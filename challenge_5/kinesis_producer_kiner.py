from sqlalchemy import MetaData, Table, create_engine
from kiner.producer import KinesisProducer

metadata = MetaData()

engine = create_engine('mysql://root@localhost/st5_dev')

connection = engine.connect()

statement = "select * from users"

result_proxy = connection.execute(statement)
result_set = result_proxy.fetchall()
record = result_set[0]

p = KinesisProducer('smartzip-challenge-5', batch_size=500, max_retries=5, threads=10)

p.put_record(record)

