try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

from PythonConfigParser.instrument import Instrument






def get_instrument(instmt_id):
    """
    Return the instrument object by instrument id
    :param instmt_id: Instrument ID
    :return Instrument object
    """
    exchange_name = cf.get(instmt_id, 'exchange')
    instmt_name = cf.get(instmt_id, 'instmt_name')
    instmt_code = cf.get(instmt_id, 'instmt_code')
    enabled = int(cf.get(instmt_id, 'enabled'))
    params = dict(cf.items(instmt_id))
    del params['exchange']
    del params['instmt_name']
    del params['instmt_code']
    del params['enabled']

    if enabled == 1:
        return Instrument(exchange_name, instmt_name, instmt_code, **params)
    else:
        return None

cf = ConfigParser.ConfigParser()
cf.read("test3.ini")
# test read
# instmts = [self.get_instrument(inst) for inst in self.get_instmt_ids()]
#         return [instmt for instmt in instmts if instmt is not None]
print(cf.sections())
instmts = [get_instrument(inst) for inst in cf.sections()]
print(instmts)
print([instmt for instmt in instmts if instmt is not None])

