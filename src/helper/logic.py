from random import choice
from expiringdict import ExpiringDict

from src.transloadit import transloadit

__format = '{}|{}'
__cache = ExpiringDict(max_len=256, max_age_seconds=10)


def _get(session_id, key):
    return __cache.get(__format.format(session_id, key))


def _refresh(session_id, key, refreshed_element):
    __cache[__format.format(session_id, key)] = refreshed_element



def _from_labels_to_sentence(label_list):
	possibilities = ['There is a', 'You are approaching', 'Nearby you have']
	length = len(label_list)
	if length > 1:
		if length == 2:
			result = '{} {} and {}.'.format(choice(possibilities),",".join(label_list[:-1]), label_list[-1]) 
		else:
			result = '{} {} and {}.'.format(choice(possibilities),",".join(label_list[:-1]), label_list[-1]) 
	else:

	return ''


def describe(image_path):
    transloadit_result = transloadit.process(image_path)
    sentence = _from_labels_to_sentence(transloadit_result)
    return sentence
