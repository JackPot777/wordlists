import os

def line_count(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

print "# Wordlists\n\n"
out = list()

for dirname, dirnames, filenames in os.walk('.'):
    if '.git' in dirnames:
        dirnames.remove('.git')
    
    for subdirname in dirnames:
        print "## %s\n" % subdirname.title()
    
    for filename in filenames:
        if dirname != '.':
            lang = filename.split('_')[0].upper()
            details = ' '.join(filename.split('.')[0].split('_')[1:])
            number_of_line = line_count(os.path.join(dirname, filename))
            out.append(" * [**%5.i**] [%s *%s*](%s/%s)" % (number_of_line, lang, details, dirname, filename))

out.sort()
out.reverse()
print '\n'.join(out)