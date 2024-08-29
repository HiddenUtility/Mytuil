class MySingleton(object):
    """シングルトーンぶち込む"""
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(MySingleton, cls).__new__(cls)
        return cls._instance
    


