from cx_Freeze import setup, Executable

# GUI应用程序可能需要不同的base，取决于你的系统
base = None

# 创建可执行文件的配置
executables = [Executable("pdf2image.py", base=base)]

# 设置配置
setup(name="Pdf2ImageApp",
      version="1.0",
      description="A PDF to Image converter",
      executables=executables)
