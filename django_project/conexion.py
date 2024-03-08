class conexion():
    def __init__(self):
        self._conectar = ['django.db.backends.mysql', 'railway', 'root', 'WDRlyVhpaqJNFNNvYYFxKSCQxDzpdkcY', 'monorail.proxy.rlwy.net', '30917',]
    
    def getter(self):
        return self._conectar