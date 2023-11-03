
from datasource.rdbms.base import RdbmsType
from datasource.rdbms.factory import Rdbms, get_rdbms


RDBMS_CONF = Rdbms(uri='sqlite:///resources/local.db', type=RdbmsType.Sqlite)
rdbms_instance = get_rdbms(RDBMS_CONF)


