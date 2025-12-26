# 使用 uv 来管理 python 环境

uv 是新一代 python 包管理工具，旨在替代 pip 或者 conda 这种传统工具，
在终端中使用`uv python list`可以查看本地已经安装的 python 版本

## windows 安装 uv

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 配置镜像

在系统环境变量新增`UV_DEFAULT_INDEX`，将值设置为清华源或者阿里源

## 清除 uv 本地缓存

```bash
Remove-Item -Recurse -Force "$(uv python dir)"
Remove-Item -Recurse -Force "$(uv tool dir)"
```

## 卸载 uv

```bash
Remove-Item "$env:USERPROFILE\.local\bin\uv.exe" -Force
Remove-Item "$env:USERPROFILE\.local\bin\uvx.exe" -Force
```

---

# 使用 uv

## 1. 创建 uv 环境

```bash
uv init
```

## 2. 添加 venv，激活环境

```bash
uv venv
```

## 3. 运行 python 文件

```bash
uv run main.py
```

## 4. 添加库

```bash
uv add ...
```

## 5. 删除库

```bash
uv remove ...
```

## 6. 查看项目依赖关系树

```bash
uv tree
```

## 清除 uv 全局缓存

```shell
uv cache clean
```
