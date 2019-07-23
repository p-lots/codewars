def v(p):
  l='%s, %s'%(p,'doo doo doo doo doo doo')
  return '%s\n%s!'%('\n'.join(l for _ in range(3)),p)
def baby_shark_lyrics():
  ps=['Baby shark','Mommy shark','Daddy shark','Grandma shark','Grandpa shark','Let\'s go hunt']
  return '\n'.join(v(p) for p in ps)+'\nRun away,…'