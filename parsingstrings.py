while True:
        print("Enter input string: ")
        str = input()
        if(str != 'q'):
            str = str.replace(' ', '')
            if ',' in str:

                str = str.split(',')

                print('First word: ' + str[0])
                print('Second word: ' + str[1])
                print("\n")
            else:
                print('Error: No comma in string.')
        else:
          break
