# classify-video-format
# 按照视频编码分类文件

依赖： `os, sys, subprocess, json, shutil`

放到需要按视频编码分类的视频文件目录中，运行脚本，将会创建对应编码名的文件夹，并将相应编码的视频移动到文件夹中

**注意！本脚本并不会递归检查子目录，以避免发生无限递归的问题**！
必须确保系统path里包含了ffmpeg三件套！测试方法：任意位置打开cmd/shell，输入ffprobe回车，不提示找不到命令即可
