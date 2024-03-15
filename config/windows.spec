# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ('..\\packages\\core\\dist-app', 'dist-app'),
    ('..\\packages\\core\\epic7_bot\\images', 'epic7_bot\\images'),
]

a = Analysis(
    ['..\\packages\\core\\view.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    icon='..\\packages\\app\\public\\icon.ico',
    name='Epic7 Bot',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
)