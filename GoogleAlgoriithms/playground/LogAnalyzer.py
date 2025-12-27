class LogAnalyser:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.log_lines = self._read_file()  # Now returns a list

    def _read_file(self) -> list[str]:
        with open(self.input_file, 'r') as file:
            return [line.strip() for line in file]  # Preserves order/duplicates

    def process_file(self):
        error_lines = [line for line in self.log_lines if line.startswith('ERROR')]
        with open(self.output_file, 'w') as outfile:
            outfile.write('\n'.join(error_lines))  # No trailing \n (optional)
