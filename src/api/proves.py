import argparse
import base64
import requests	

class State();
	def __init__(self, objects):
		self.objects = objects
		self.new_objects = list()		
	
	# adding objects that were detected to the state
	def add_objects(new_objects):
		for item in new_objects:
			if item not in self.objects:
				print("The object already is new") 
				self.new_objects.add(item)
	
	# deleting an object from the state because we do not see it 
	def __delete_object(old_object):
		self.objects.remove(old_object)
		
			




	
if __name__ == '__main__':
	"""
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
	
	if args.image:
		text = create_text(args.image)
		print(text)	
	"""
