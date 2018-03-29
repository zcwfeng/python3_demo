# 导入数据库批量操作脚本
import subprocess

file_path = "tencent.sql"
# cmd = ["mysql", "-h", IP, "-u", UserName, "-p%s" % PassWord, '-f', Database]
cmd = ["mysql", "-h", "127.0.0.1", "-u", "xxxroot", "-p%s" % "xxxx", '-f', "itzhaopin"]
process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,encoding="utf-8")
output = process.communicate("source " + file_path)



print(output)
