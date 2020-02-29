from expiringdict import ExpiringDict


__format = '{}|{}'
__cache = ExpiringDict(max_len=256, max_age_seconds=10)


def _get(session_id, key):
    return __cache.get(__format.format(session_id, key))


def _refresh(session_id, key, refreshed_element):
    __cache[__format.format(session_id, key)] = refreshed_element


def describe(image_base64):
    return None
