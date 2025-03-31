from random import randint


class Generator:
    @staticmethod
    def generate_code(bottom_threshold: int = 0, top_threshold: int = 100,
                      code_size: int = 10, digit_size: int = 2) -> str:
        code = ""
        for i in range(code_size):
            code = code + str(randint(bottom_threshold, top_threshold + 1)).zfill(digit_size)
        return code
