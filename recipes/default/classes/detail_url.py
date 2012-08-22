from urlparse import urlparse
from monitoring_detail import MonitoringDetail

def __detail_ident__(params={}):
    if params["monitoring_type"] == "URL":
        return MonitoringDetailUrl


class MonitoringDetailUrl(MonitoringDetail):
    property = "urls"
    property_type = list

    def __init__(self, params):
        self.monitoring_type = params["monitoring_type"]
        self.url = params.get("monitoring_0", None)
        self.warning = params.get("monitoring_1", "5") or "5"
        self.critical = params.get("monitoring_2", "10") or "10"
        self.url_expect = params.get("monitoring_3", None)
        o = urlparse(self.url)
        for attr in ["scheme", "netloc", "path", "params", "query", "fragment", "username", "password", "hostname", "port"]:
            setattr(self, attr, getattr(o, attr))

    def __str__(self):
        return "%s %s:%s" % (self.url, self.warning, self.critical)
