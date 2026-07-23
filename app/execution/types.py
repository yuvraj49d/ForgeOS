from enum import Enum


class ExecutorType(str, Enum):
    MOCK = "mock"
    FILESYSTEM = "filesystem"