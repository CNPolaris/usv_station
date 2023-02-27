<div align="center">
  <h1>元理创新USV地面站软件</h1>
</div>

### 🏷简介


### 📺配套视频



### 📔相关文档



### 💣特性

- 远程操控船体
- 监测环境数据
- 船载监控
- 百度地图轨迹
- 船体运行状态
- 船控指令

### 🎿安装步骤

### 开发相关
在main.py同级目录下创建main.spec文件，并将以下内容全部粘贴到里面
```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
py_files = [
    '.\\components\\*.py',
    ',\\core\\*.py',
    '.\\layout\\*.py',
    '.\\threads\\*.py',
    '.\\ui\\*.py',
    '.\\utils\\*.py'
]
add_files = [
    ('.\\static\\img\\*.png', '.\\static\\img'),
    ('.\\templates\\*.html', '.\\templates'),
    ('.\\setup.cfg', '.'),
    ('.\\setup_copy.cfg', '.')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=add_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='USV地面站软件',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
```
在终端中执行`pyinstaller main.spec`即可进行软件打包

### 🎯更新日志

[CHANGELOG](./CHANGELOG.zh_CN.md)

### 🩺Git提交规范参考

- `feat`增加新的业务功能
- `fix`修复业务问题/BUG
- `perf`优化性能
- `style`更改代码风格，不影响运行结果
- `refactor`重构代码
- `revert`撤销更改
- `test`测试相关，不涉及业务代码的更改
- `docs`文档和注释相关
- `wip`开发中
- `types`类型定义文件更改