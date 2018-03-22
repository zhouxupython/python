import inspect
import os

# define __LINE__ as the usage in c language
# os.sep 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
class Meta(type):
    def __repr__(self):
        # Inspiration: https://stackoverflow.com/a/6811020
        callerframerecord = inspect.stack()[1]  # 0 represents this line
        # 1 represents line at caller
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        # print(info.filename)  # __FILE__     -> Test.py
        # print(info.function)  # __FUNCTION__ -> Main
        # print(info.lineno)  # __LINE__     -> 13
        # return str(info.filename + ': ' + info.function + '(' + str(info.lineno) + ') > ')
        return str((info.filename[::-1])[0:info.filename[::-1].index(os.sep)][::-1] + ': ' + info.function + '(' + str(info.lineno) + ') > ')

class __LINE__(metaclass=Meta):
    pass
    
# F:\_LEARN\06_Python\python_ws\pluginbase\pluginbase.py: __enter__(374) >   __enter__:     
print(__LINE__, ..........)
