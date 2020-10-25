import logging
import time
import sys

import smpplib.gsm
import smpplib.client
import smpplib.consts
import config

# if you want to know what's happening
logging.basicConfig(level='DEBUG')

client = smpplib.client.Client(config.host, config.port, allow_unknown_opt_params=True)



# Print when obtain message_id
client.set_message_sent_handler(
    lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
client.set_message_received_handler(lambda pdu: handle_receive_sms(pdu))

client.connect()
client.bind_transceiver(system_id=config.system_id, password=config.password)

try:
	listen(client)
except:
	time.sleep(600)
	listen(client)
	


def handle_receive_sms(pdu):
        logging.debug('Sample dict log: %s', pdu)
        return 0 # cmd status for deliver_sm_resp
        
def send_message(part):
	pdu = client.send_message(
        source_addr_ton=smpplib.consts.SMPP_TON_INTL,
        source_addr=config.source_addr,
        dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
        destination_addr=config.default_receiver,
        short_message=part,
        data_coding=encoding_flag,
        esm_class=msg_type_flag,
        registered_delivery=True,
    	)
    	print(pdu.sequence)
    	
def listen(client)
	# Enters a loop, waiting for incoming PDUs
	client.listen()	
