@echo off
call "C:\Program Files\QGIS 3.0\bin\o4w_env.bat"
call "C:\Program Files\QGIS 3.0\bin\qt5_env.bat"
call "C:\Program Files\QGIS 3.0\bin\py3_env.bat"

@echo on
pylupdate5 ui/Ui_fdldialog.py -ts zh_CN.ts && pylupdate5 ui/Ui_fdldialog.py -ts zh_CN.ts ^
&& pylupdate5 ui/Ui_urlLinkDialog.py -ts zh_CN.ts && pylupdate5 ui/Ui_downloadFileInfoDialog.py -ts zh_CN.ts

