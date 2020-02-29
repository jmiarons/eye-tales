from random import choice
from expiringdict import ExpiringDict

from src.helper.detections import DETECTIONS_LIST, SENTENCE_BEGIN
from src.transloadit import transloadit


__format = '{}|{}'
__cache = ExpiringDict(max_len=256, max_age_seconds=30)


def _get(session_id, key):
    return __cache.get(__format.format(session_id, key))


def _refresh(session_id, key, refreshed_element):
    __cache[__format.format(session_id, key)] = refreshed_element


def _extract_new_detections(session_id, result):
    new_result = []
    for item in result:
        cached_item = _get(session_id, item)
        if not cached_item:
            _refresh(session_id, item, True)
            new_result.append(item)
    return new_result


def _from_labels_to_sentence(label_list):
    if label_list:
        if len(label_list) == 1:
            object_list_str = 'a {}'.format(label_list[0])
        else:
            object_list_str = '{} and a {}'.format(', '.join(label_list[:-1]), label_list[-1])
        return '{} {}'.format(choice(SENTENCE_BEGIN), object_list_str)
    return None


def describe(session_id, image_path):
    result = transloadit.process(image_path)
    result = [i.lower() for i in result if i.lower() in DETECTIONS_LIST]
    result = _extract_new_detections(session_id, result)
    sentence = _from_labels_to_sentence(result)
    return sentence
