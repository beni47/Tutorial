name = input("Whats your name? ").lower().strip()
#replace with match
#if name == "Harry":
 #   print("Gryffindor")
#lif name == "Hermione":
#    print("Gryffindor")
#elif name == "Ron":
 #   print("Gryffindor")
#lif name == "Draco":
 #   print("sly")
#else:
  #  print("WHO?" )

match name:
    case 'harry'|'hermione'|'ron':
        print("Gry")
    case 'draco':
        print('Sly')
    case _ :
        print('who?')


