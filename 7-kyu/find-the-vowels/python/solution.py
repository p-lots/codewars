def vowel_indices(word):
	return [idx for idx, ch in enumerate(word, 1) if ch.lower() in 'aeiouy']
