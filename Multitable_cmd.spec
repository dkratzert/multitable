# -*- mode: python -*-

block_cipher = None


a = Analysis(['multitable.py'],
             pathex=['D:\\Programme\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x64', 'D:\\GitHub\\multitable'],
             binaries=[],
             datas=[('templates', 'templates')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='multitable',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
