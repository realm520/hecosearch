import logging
from heco_api import HecoApi
from models import HecoScanConfig, HecoSwapReward, Session


def get_token(addr):
    if addr is None:
        return ""
    daoAddr = {
        "lead": '0x8527224946E775FE93F16834b94A446c87f45217',
        "beer": '0x0A8a9929f0826aad857aa020f8278036A46763b8'
    }
    for k, v in daoAddr.items():
        if v.lower() == addr.lower():
            return k
    return ""

def scan_token(start):
    tokenAddr = {
        "lead": "0x2866a32f364b67437c442f5a15fdc992be83cd6f",
        "beer": "0x3870c14F5a2Da7b67353831C33477E889C6e841D",
    }
    heco = HecoApi("http://192.168.1.123:16909/")
    block_number = heco.get_block_number()
    if block_number <= 0:
        return
    session = Session()
    for i in range(start, block_number+1):
        block = heco.get_block(i, True)
        block_time = int(block['timestamp'], 16)
        for t in block['transactions']:
            token = get_token(t['to'])
            if token == "":
                continue
            try:
                if t['input'].startswith('0xc00007b'):
                    receipt = heco.get_tx_receipt(t['hash'])
                    level = 0
                    sub = ""
                    for l in receipt['logs']:
                        if l['address'].lower() == tokenAddr[token].lower():
                            session.add(HecoSwapReward(
                                symbol=token,
                                blockNum=i,
                                blockTime=block_time,
                                addr='0x'+l['topics'][2][25:],
                                reward=f"{int(l['data'], 16)/10**18:>.6f}",
                                sub=sub,
                                subLevel=level
                            ))
                            print(block_time, '0x'+l['topics'][2]
                                  [25:], int(l['data'], 16)/10**18)
                        if level == 0:
                            sub = l['address']
                        level += 1
                    session.commit()
            except Exception as e:
                print(str(e))
        if i % 1000 == 0:
            print(i)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG,
    #                 format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    #                 datefmt='%Y-%m-%d  %H:%M:%S %a'
    #                 )
    scan_token(1784272)
