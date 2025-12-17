# Python 初学笔记

在 2025 年寒假的时候草草看完《python 从入门到实践（第 3 版）》的书，到现在已经过去好久了，自己的技术一直都没有精进。所以该笔记用来巩固知识，探索新知。

# 1. 逻辑运算符优先级

`not` > `and` > `or`

# 2. 列表

python 用 `[]` 来定义列表。
列表有许多方法，比如对于纯数字列表，`max()`可以直接获取列表最大值，不在这里赘述。

# 3. 字典

python 用 `{}` 来定义字典，即键值对。
注意键需要用不可变的数据类型来定义，不能用列表。
例子：如果出现多个相同的人名，就可以用元组来定义不一样的人。

```python
phoneBook = {("Alice", 10): "2341", ("Alice", 20): "9102", ("Alice", 30): "3258"}
print(phoneBook[("Alice", 10)])
```

# 4. 字符串格式化

我比较喜欢用`f"...{value}"`这种方式来写。
此外，如果变量是数字，还可以指定小数位数：

```python
import math
pi = math.pi
print(f"{pi:.10f}") # 指定小数点后10位
```

# 5. 类

继承：`class 子类(父类)`。
在子类的 `__init__()` 中使用 `super().__init__()`可继承父类的构造函数，然后在下面写自己的新的参数。

```python
class Pet:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
```

# 6. 文件路径

`./` 表示当前文件所在的目录
`../` 表示更上一层的父目录

# 7. 文件操作

## 7.1 读取

首先要用`open()`函数来打开文件；`r`参数代表读取，换成`w`代表写入；`encoding="utf-8"`表示编码方式

```python
file = open("url","r",encoding="utf-8")
```

`read()`函数读取全部文件内容

```python
print(file)
```

读完后要关闭文件

```python
file.close()
```

也可以把上面所有操作整合，文件会自动关闭，释放资源：

```python
with open("url","r",encoding="utf-8") as 别名:
    # 对文件的操作
```

## 7.2 写入

`w`：写入（覆盖原有）
`a`：附加到后面
`r+`：即可读又可写，写是追加的形式

```python
with open("url","w",encoding="utf-8") as 别名:
    # 对文件的操作
```

# 8. 异常处理

```python
try:
    # 有可能错误的代码
except ValueError:
    # 产生值错误时运行
except ZeroDivisionError:
    # 产生除零错误时运行
except:
    # 有其他错误时运行
else:
    # 没有错误时运行
finally:
    # 无论正确与否都会执行
```

# 9. 测试

python 自带`unittest`单元测试库，还可以用`pytest`第三方库

# 10.高阶函数和匿名函数

函数的参数里可以传入其他函数，如果有些函数只用了一次，但是额外定义的话就有点麻烦了，这时候可以写`lambda`匿名函数

```python
function_print(7,lambda num1,num2:num1*num2,other_function)
```
