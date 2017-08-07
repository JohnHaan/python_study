
def main():
    b_ban = ['dolbam','ianlee','sungdae','john']
    identity = ['NM001','NM002','NM003','NM004']
    result = {}
    zipped = zip(b_ban, identity)
    for k,v in zipped:
        result[k] = v

    print result

if __name__ == '__main__':
    main()