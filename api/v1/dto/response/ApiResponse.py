from dataclasses import dataclass

from api.v1.enum.ResultCodeEnum import ResultCodeEnum


@dataclass
class ApiResponse:
    code: str
    message: str
    data: any

    @classmethod
    def of(cls, code: str, message: str, data: any):
        return cls(code, message, data)

    @classmethod
    def ok(cls, data: any):
        return cls.of(ResultCodeEnum.get_code(ResultCodeEnum.SUCCESS),
                      ResultCodeEnum.get_message(ResultCodeEnum.SUCCESS), data)

    @classmethod
    def error(cls, message: str):
        return cls.of(ResultCodeEnum.get_code(ResultCodeEnum.ERROR),
                      message, [])
