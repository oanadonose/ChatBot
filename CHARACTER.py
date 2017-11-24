from imdb import IMDb
ia = IMDb() 
imdb_access = imdb.IMDb()

def summary(self) :
 """"This returns a string with a summary for the character """
if not self:
      return ''
      
s = 'Character\n=====\nName: %s\n' % self.get('name','')
bio = self.get('biography')
if bio:
    s += 'Biography: %s\n' % bio[0]
filmo = self.get('filmography')
if filmo:
    a_list = [x.get('long imdb canonical title','')]

for x in filmo[:5]]
s += 'Last movies with this character: %s. \n' % '; '.join(a_list)
return s 
