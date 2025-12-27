class FileProcessor:

    def __init__(self, blockedWordsFile):
        self.blockedWords = self.loadBlockedWords(blockedWordsFile)

    def loadBlockedWords(self, blockedWordsFile):
        with open(blockedWordsFile, "r") as file:
            return {line.strip().lower() for line in file}


    def processFile(self, inputFile, outputFile):
        with open(inputFile, "r") as infile, open(outputFile, "w") as outfile:
            for line in infile:
                words = line.split()
                process_line = " ".join("BLOCKED" if word.lower() in self.blockedWords else word for word in words)
                outfile.write(process_line + "\n")
                outfile.write("\r\n")


# Example usage:
blocked_words_file = "blocked_words.txt"  # Each line contains one blocked word
input_file = "large_text.txt"  # Large input file
output_file = "processed_text.txt"  # Output file with replaced words

processor = FileProcessor(blocked_words_file)
processor.processFile(input_file, output_file)
