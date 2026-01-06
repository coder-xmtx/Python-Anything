---
日期: 2025-09-23
tags:
  - python
---

## 什么是 UV
uv 是新一代python包管理器，可创建虚拟环境，替代`pip`

## 安装 uv
```shell
pip install uv
```

## 查看uv可支持的python版本
这里也会列出本机以安装的python版本
```shell
uv python list
```
输出如下
```txt
cpython-3.14.0rc3-windows-x86_64-none                 <download available>
cpython-3.14.0rc3+freethreaded-windows-x86_64-none    <download available>
cpython-3.13.7-windows-x86_64-none                    <download available>
cpython-3.13.7+freethreaded-windows-x86_64-none       <download available>
cpython-3.12.11-windows-x86_64-none                   <download available>
cpython-3.11.13-windows-x86_64-none                   <download available>
cpython-3.10.18-windows-x86_64-none                   <download available>
cpython-3.10.10-windows-x86_64-none           D:\program\python 3.10\python.exe
cpython-3.9.23-windows-x86_64-none                    <download available>
cpython-3.8.20-windows-x86_64-none                    <download available>
pypy-3.11.13-windows-x86_64-none                      <download available>
pypy-3.10.16-windows-x86_64-none                      <download available>
pypy-3.9.19-windows-x86_64-none                       <download available>
pypy-3.8.16-windows-x86_64-none                       <download available>
graalpy-3.12.0-windows-x86_64-none                    <download available>
graalpy-3.11.0-windows-x86_64-none                    <download available>
graalpy-3.10.0-windows-x86_64-none                    <download available>
```

## 下载python指定版本
```shell
uv python install 3.13
```

---

## 创建uv虚拟环境
执行以下命令，同时也创建了Git版本管理
```shell
uv init
```

## 加载库
执行以下命令，会创建`.venv` 虚拟环境，`xxxx`为需要安装的库名
安装好的库会写进toml配置文件里面
```shell
uv add xxxx
```

## 删除库
```shell
uv remove xxxx
```

## 查看库与库之间的依赖关系
```shell
uv tree
```

--------------

## 更改虚拟环境的python版本
默认使用的是本机上的python版本，也可以自己指定

#### step1：更改`pyproject.toml`文件
```toml
[project]
name = "test-uv"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"   （在这一行改版本号）
dependencies = []
```

#### step2：更改`.python-version`文件
```txt
3.12    （更改版本号）
```

#### step3：让uv重新解析
```shell
uv sync
```

---

## uv tool
格式规范工具`ruff`等等，详细看视频

---

## 相关资源
[uv官方网站](https://docs.astral.sh/uv/)
[uv快速入门](https://www.bilibili.com/video/BV1JxLEzGEq5)
[从pip到uv](https://www.bilibili.com/video/BV13WGHz8EEz)