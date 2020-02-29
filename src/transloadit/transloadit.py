from transloadit import client


def process(image_path):
	try:
		tl = client.Transloadit('ffa9682462e34cefb1d3308f52fdca54', '79b5408ebb4ad85e1e10a955c803478712ca9385')
		assembly = tl.new_assembly()
		assembly.add_step(':original', robot='/upload/handle', options={'result': True})
		assembly.add_step('described', robot='/image/describe', options={
			'use': ':original',
			'result': True,
			'format': 'meta',
			'granularity': 'list',
			'provider': 'aws'
		})

		# Add image to upload
		image_file = open(image_path, 'rb')
		assembly.add_file(image_file)

		# Start the Assembly
		assembly_response = assembly.create(retries=5, wait=True)
		result = assembly_response.data.get('results', {})
		detections = result.get('described', [{}])[0].get('meta', {}).get('descriptions', [])
		image_file.close()
		return detections
	except Exception as e:
		print('error: could not process image through transloadit: {}'.format(e))
		return []
