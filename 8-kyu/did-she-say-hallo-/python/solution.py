def validate_hello(greetings):
    greetings = [''.join(ch for ch in word if ch.isalpha()) for word in greetings.lower().split()]
    hellos = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(hello in greetings for hello in hellos)
