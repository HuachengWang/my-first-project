command = ""
started = True
stopped = True
while True:
    command = input ('> ').lower()
    if command == "help":
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif command == 'start':
        if started:
            print('Car is already started!')
        else:
            print('Car started... Ready to go!')
    elif command == 'stop':
        if stopped:
            print('Car is already stopped!')
        else:
            print('Car stopped.')
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that...")