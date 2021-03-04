from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy import Index



Base = declarative_base()


class HecoScanConfig(Base):
    __tablename__ = 'heco_scan_config_table'
    hid = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(128), index=True, nullable=False)
    value = Column(String(128), nullable=False)


class HecoSwapReward(Base):
    __tablename__ = 'heco_swap_reward_table'
    hid = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(32), nullable=False)
    blockNum = Column(Integer)
    blockTime = Column(Integer, nullable=False)
    addr = Column(String(64), index=True, default="")
    reward = Column(String(64), default="0")
    sub = Column(String(64), index=True, default="")
    subLevel = Column(Integer, nullable=False)

    __table_args__ = (Index('ix_addr_symbol_block', 'symbol', 'addr', 'blockNum', unique=True),)


engine = create_engine(
            'sqlite:///invitation_reward.db',
            echo=True,
            poolclass=SingletonThreadPool,
            connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


if __name__ == '__main__':
    session = Session()
    session.add(HecoScanConfig(key="last_scan_block", value="200000"))
    session.add(HecoSwapReward(
        symbol='lead',
        blockNum=200000,
        blockTime="2020-02-01 11:22:33",
        addr="0x05b64039edb05b6eab570cffed256c7dbce699355",
        reward="100",
        sub="",
        subLevel=0))
    session.commit()
