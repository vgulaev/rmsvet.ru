import dbclasses.dbworker 
import suds
from suds.cache import DocumentCache
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential( sett )

#api_url = "https://api-iz.merlion.ru/mlservice.php?wsdl"
api_url = "https://api.merlion.com/dl/mlservice2?wsdl"
api = suds.client.Client(api_url, username='TC0034492|MPC', password='12345')
api.set_options(cache=DocumentCache())

def fs():
    a = api.service.getShipmentAgents()
    #f = codecs.open("merlion_ShipmentAgents.json", "w", "utf-8")
    f = open("merlion_ShipmentAgents.json", "w")
    f.write(str(a))
    a = api.service.getCurrencyRate()
    f.write(str(a))

fs()