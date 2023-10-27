class ResultCodeEnum:
    SUCCESS = ("200", "Success")
    ERROR = ("500", "Error")

    @classmethod
    def get_code(cls, code_enum):
        return code_enum[0]

    @classmethod
    def get_message(cls, code_enum):
        return code_enum[1]
