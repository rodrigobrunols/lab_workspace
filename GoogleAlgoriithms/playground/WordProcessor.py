import math
import threading

file_lock = threading.Lock()

class WordProcessor:
    def __init__(self, inputfile):
        self.blockedWords = self._read_file(inputfile)

    def _read_file(self, input_file):
        with open(input_file, "r") as infile:
            words_set = set(line.strip().lower() for line in infile if line.strip())
        return words_set

    def replace_blocked_words(self, inputfile, outputfile ):
        # with file_lock:
        with open(inputfile, "r") as infile:
            # with file_lock:
            processed_line = []
            for line in infile:
                words = line.split()
                processed_line.append(" ".join("BLOCKED" if word.lower() in self.blockedWords else word for word in words))

            with file_lock:
                with open(outputfile, "w") as outfile:
                    outfile.writelines(processed_line)


def main():
    blocked_words_file = "blocked_words.txt"  # Each line contains one blocked word
    input_file = "large_text.txt"  # Large input file
    output_file = "processed_text2.txt"  # Output file with replaced words

    processor = WordProcessor(blocked_words_file)
    processor.replace_blocked_words(input_file, output_file)
    # file_lock.release()

    # processor.replace_blocked_words(input_file, output_file)
    # with file_lock:
    #     processor.replace_blocked_words(input_file,output_file)


if __name__ == "__main__":
    main()
