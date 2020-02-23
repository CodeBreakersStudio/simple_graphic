from .imports_setup import time, _root
def update(rate=None):
    global _update_lasttime
    if rate:
        now = time.time()
        pauseLength = 1/rate-(now-_update_lasttime)
        if pauseLength > 0:
            time.sleep(pauseLength)
            _update_lasttime = now + pauseLength
        else:
            _update_lasttime = now

    _root.update()