def vowelsubstring(s):
    output = []
    for i in range(len(s)):
        for j in range(len(s)):
            if s[j] not in ["a","e","i","o","u"]:
                output.append(s[i:j])
    count = 0
    for w in output:
        if set(w) == {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    return count
            
            
            
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = vowelsubstring(s)

    fptr.write(str(result) + '\n')

    fptr.close()
