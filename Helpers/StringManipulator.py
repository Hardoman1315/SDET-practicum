class StringManipulator:
    def extract_name_from_code(self, code: str) -> str:
        name_code = code[:10]
        return self.__internal_extractor(name_code)

    def extract_surname_from_code(self, code: str) -> str:
        surname_code = code[10:]
        return self.__internal_extractor(surname_code)

    @staticmethod
    def check_for_length(num: int, limit: int) -> int:
        while num > limit:
            num = num - (limit + 1)
        return num

    def __internal_extractor(self, code: str, step: int = 2) -> str:
        """
        This method convert integer code to word
        :param code: Code to convert
        :param step: How many digits are supposed to be converted to a letter. Default = 2
        :return: str
        """
        extracted_line = ""
        for i in range(0, len(code), step):
            char_code = self.check_for_length(int(code[i:i + 2]), 25)
            ucode = (char_code + 97)
            extracted_line = extracted_line + chr(ucode)
        return extracted_line
