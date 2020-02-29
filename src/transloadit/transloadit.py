import base64

from transloadit import client


def main(image_base64):
	tl = client.Transloadit('ffa9682462e34cefb1d3308f52fdca54', '79b5408ebb4ad85e1e10a955c803478712ca9385')
	assembly = tl.new_assembly()

	assembly.add_step(':original', {
		'robot': '/upload/handle',
		'result': True
	})
	assembly.add_step('described', {
		'use': ':original',
		'robot': '/image/describe',
		'result': True,
		'format': 'meta',
		'granularity': 'list',
		'provider': 'aws'
	})

	# Add image to upload
	encoded_string = base64.b64decode(image_base64)
	assembly.add_file(encoded_string)

	# Start the Assembly
	assembly_response = assembly.create(retries=5, wait=True)
	result = assembly_response.data.get('results')
	return result
