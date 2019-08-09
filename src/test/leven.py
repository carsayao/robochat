
def main():

    def levenshtein(str1, s2):
        ''' 
        Distance between two strings
        '''
        N1 = len(str1)
        N2 = len(s2)

        stringRange = [range(N1 + 1)] * (N2 + 1)
        for i in range(N2 + 1): 
            stringRange[i] = range(i,i + N1 + 1)
        for i in range(0,N2):
            for j in range(0,N1):
                if str1[j] == s2[i]:
                    stringRange[i+1][j+1] = min(stringRange[i+1][j] + 1,stringRange[i][j+1] + 1,stringRange[i][j])
                else:
                    stringRange[i+1][j+1] = min(stringRange[i+1][j] + 1,stringRange[i][j+1] + 1,stringRange[i][j] + 1)
        return stringRange[N2][N1]

    levenshtein(['hello', 'there'], ['mellow', 'hair'])

if __name__ == '__main__':
    main()
