# <img src="assets/Python.svg" /> Python-Anything

学习 Python ，巩固知识，探索新知

| Python 包管理器 |         笔记         | 代码编辑器  |
| :-------------: | :------------------: | :---------: |
|     **uv**      | **Jupyter Notebook** | **VS Code** |

## 🛠️ 更新说明（2025-01-06）

修改部分文档，后续会继续处理

## <img src="assets/vscode.svg" /> VS code 配置

如果你喜欢用 VS Code 来写 Jupyter，请和我一样配置

1. 在插件市场安装 jupyter
2. 如需运行 Jupyter Notebook 的代码块，请先在打开的 `.ipynb` 文件的右上角指定 Python 内核

## ⚙️ 依赖安装

1. 安装 [uv](https://docs.astral.sh/uv/) （若已经安装，可跳过该步骤）

   - Windows 环境

   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   - MacOS 或 Linux 环境

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. 解析项目包

   ```bash
   uv sync
   ```

## ⏬ 数据下载

由于数据集有点大，不好放在 Github 中，在这里用百度网盘分享 >> [data 数据集](https://pan.baidu.com/s/1viV7dAD-0YMQBUahWpifOw?pwd=xmtx) <br />
下载后，请将该 data 文件夹放入 `Pandas` 目录中，即最后的文件位置为 `Pandas/data`

## ✍️ 写在最后

> 找一颗属于你自己的星星吧，它会给你指引方向，一直到天明。 <br />
> -- 凯蒂·克劳泽
