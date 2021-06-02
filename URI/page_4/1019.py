convert = [3600, 60]
display = [False] * 3

time = lambda time, con: (time % con, time / con)

if __name__ == '__main__':
    userTime = int(input())
    for i in range(3):
        if userTime <= 59:
            display[2] = userTime
            break
        else:
            userTime, output = time(userTime, convert[i])
            display[i] = output
    print("%i:%i:%i" % (display[0], display[1], display[2]))