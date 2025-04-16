import pandas as pd
from sqlalchemy import create_engine, exc
from typing import Union, Dict, Optional, Iterator
import logging

db_config = {
    "host": "localhost",    # 主机地址
    "port": 3306,          # 端口号
    "user": "root",        # 用户名
    "password": "123456",  # 密码
    "database": "pythonml"  # 数据库名
}


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def readFromDB(sql:str,batchsize:Optional[int])->  Union[pd.DataFrame, Iterator[pd.DataFrame]]:
    try:
        engine = create_engine(
            f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}?charset=utf8mb4"
        )
        with engine.connect() as conn:
            return pd.read_sql(sql,conn,chunksize=batchsize)

    except exc.SQLAlchemyError as e:
        logger.error(f"exception DB Exception:{str(e)}")
        raise

    except Exception as e:
        logger.error(f"read from DB Exception:{str(e)}")
        raise

def write2DB(df: pd.DataFrame,tableName: str,batchsize:Optional[int]) -> None:
    try:
        engine = create_engine(
            f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}?charset=utf8mb4"
        )
        with engine.begin() as conn:
            logger.info(f"正在写入{tableName} ing...")
            df.to_sql(
                name=tableName,
                con=conn,
                index=False,
                if_exists='append',
                chunksize=batchsize,
                method='multi'
            )

            logger.info(f"正在写入{tableName} 成功.")

    except exc.IntegrityError as e:
        logger.error(f"数据完整性错误: {str(e)}，建议检查主键或唯一约束")
        raise
    except exc.SQLAlchemyError as e:
        logger.error(f"exception DB Exception:{str(e)}")
        raise

    except Exception as e:
        logger.error(f"read from DB Exception:{str(e)}")
        raise

new_data = pd.DataFrame({
        'id': [101, 102],
        'title': ['Alice', 'Bob'],
        'content': ['alice@example.com', 'bob@example.com']
})

write2DB(
            df=new_data,
            tableName="article",
            batchsize=100
)