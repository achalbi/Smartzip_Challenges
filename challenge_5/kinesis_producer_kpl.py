from sqlalchemy import MetaData, Table, create_engine
from kinesis_producer import KinesisProducer


metadata = MetaData()

engine = create_engine('mysql://root@localhost/st5_dev')

connection = engine.connect()

statement = "select * from users"

result_proxy = connection.execute(statement)
result_set = result_proxy.fetchall()
records = result_set[:1]

config = dict(
    aws_region='us-east-1',
    buffer_size_limit=100000,
    buffer_time_limit=0.2,
    kinesis_concurrency=1,
    kinesis_max_retries=10,
    record_delimiter='\n',
    stream_name='smartzip-challenge-5',
    )

k = KinesisProducer(config=config)

for record in records:
    k.send(record)

k.close()
k.join()

