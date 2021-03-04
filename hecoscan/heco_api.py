# -*- coding: utf-8 -*-

import json
import logging
import requests
import fire


# transfer_to_contract_testing swapcaller XWCCTueWEr4UADuoJHidBxTe1webiT8NTYp5Z 0.01 ETH "ETH,1000000,XWC,1000000,10000000"
# transfer_to_contract swapcaller XWCCTueWEr4UADuoJHidBxTe1webiT8NTYp5Z 1 ETH "ETH,100000000,XWC,1000000,10000000" 0.001 4150 true
# invoke_contract_offline swapcaller XWCCTueWEr4UADuoJHidBxTe1webiT8NTYp5Z "caculateExchangeAmount" "ETH,100000000,XWC"
class HecoApi:
    def __init__(self, url):
        self.baseUrl = url #"http://47.75.155.116:40123"
        self.gasPrice = "0.00000001"

    def rpc_request(self, method, args):
        args_j = json.dumps(args)
        payload =  "{\"jsonrpc\":\"2.0\",\r\n \"id\": 1,\r\n \"method\": \"%s\",\r\n \"params\": %s\r\n}" % (method, args_j)
        headers = {
                'content-type': "application/json",
                'cache-control': "no-cache",
        }
        logging.debug(self.baseUrl)
        for i in range(5):
            try:
                logging.debug("[HTTP POST] %s" % payload)
                response = requests.request("POST", self.baseUrl, data=payload, headers=headers)
                # if method == "invoke_contract":
                #     pass
                    # print(response.text)
                rep = response.json()
                if "result" in rep:
                    return rep["result"]
            except Exception:
                logging.error("Retry: %s" % payload)
                continue

    def get_contract_events(self, contract, start, count):
        try:
            resp = self.rpc_request('get_contract_events_in_range', [contract, start, count])
        except:
            pass
        return resp

    def get_block_number(self):
        blockNumber = 0
        try:
            resp = self.rpc_request('eth_blockNumber', [])
            if resp:
                blockNumber = int(resp, 16)
        except:
            pass
        return blockNumber

    def get_block(self, blockNumber, withDetail=False):
        resp = ""
        try:
            resp = self.rpc_request('eth_getBlockByNumber', [hex(blockNumber), withDetail])
        except:
            pass
        return resp

    # def get_transaction(self, account):
    #     res = self.rpc_request("wallet_create_account",[account])
    #     return res

    def get_tx_receipt(self, tx):
        res = self.rpc_request("eth_getTransactionReceipt",[tx])
        return res

    def dump_private_keys(self):
        res = self.rpc_request("dump_private_keys",[])
        return res



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d  %H:%M:%S %a'
                    )
    heco = HecoApi("http://192.168.1.123:16909/")
    fire.Fire(heco)
    # heco.send_order("xwc_eth", 0.3891, 877543175/10**8, 0)
