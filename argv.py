from sys import argv
print 'Hello, ' + (argv[1] if len(argv) > 1 else 'Guest')
