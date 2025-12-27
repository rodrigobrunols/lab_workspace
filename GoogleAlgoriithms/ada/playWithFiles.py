class Solution:

    def readWordsFile(self, filename):

        resultSet = set()
        with open(filename, "r") as file:
            for line in file:
                resultSet.add(line.strip().upper())
        
        return resultSet

    def blockWords(self,inputFile, wordsBlockedFile):
        
        blockedWords = self.readWordsFile(wordsBlockedFile)
        print(f"Words blocked: {blockedWords}")
        newLine = []

        with open(inputFile, "r" ) as file:
            for line in file:
                for word in line.split():
                    # print(word.upper() , end=" ")
                    if word.upper() in blockedWords:
                        # print("  IF ")
                        newLine.append('BLOCKED')
                    else:
                        # print("  ELSE ")
                        newLine.append(word)

                print(" ".join(newLine))
                newLine = []


s  = Solution()
s.blockWords("sample_lines.txt","words_to_block.txt")