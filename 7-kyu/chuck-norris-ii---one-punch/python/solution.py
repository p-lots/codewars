one_punch = lambda item: ' '.join(''.join(ch for ch in word if ch.lower() != 'e' and ch.lower() != 'a') for word in sorted(item.split())) if item and isinstance(item, str) else 'Broken!'