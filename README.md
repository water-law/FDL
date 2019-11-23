# A small quickly download software

### 环境

Qt5.10 + Python3.6.0 + Pyinstaller 3.4 +Windows10

### 运行

```shell
pyinstaller FDL.spec -y
```

在 dist/FDL 下有个 FDL.exe, 必须整个 dist/FDL 文件夹才能使用。

### 项目结构

|-- FDL

​	|-- designer  # 存放 ui 文件

​	|-- form  # 存放继承 ui 目录下的自定义窗口类

​	|-- static  # 一些静态资源，收集起来统一放在这里

​	|-- ui  # 存放 ui 文件生成的 python 文件

​	|-- utils  # 工具类

​	|-- build.bat  # build 脚本

​	|-- conf.json  # 软件配置文件

​	|-- FDL.ico  # 软件图标

​	|-- FDL.py  # 主窗口类

​	|-- FDL.spec  # pyinstaller 文件

​	|-- log_conf.yml  # 日志配置文件

​	|-- tool.py  # 静态资源生成工具类

​	|-- ts.bat  # 国际化生成脚本(待完善)

​	|-- ui.bat  # pylupdate5、pyuic5、pyrcc5 环境初始化脚本， 根据自己实际情况修改

​	|-- *.qm, *.ts  # 国际化文件

### 说明

FDL.spec 下添加下 datas=[("conf.json", "."), ("log_conf.yml", "."), ("*.qm", ".")]

```python
a = Analysis(['FDL.py'],
             pathex=['E:\\Projects\\github\\FDL'],
             binaries=[],
             datas=[("conf.json", "."), ("log_conf.yml", "."), ("*.qm", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
```



调试时 console 设置为 True， 方便看到错误信息.

```python
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='FDL',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='FDL.ico')
```

