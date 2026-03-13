import os
import re

# 定义匹配并处理的函数
def rename_files_in_directory(directory):
    # 遍历给定目录和所有子目录
    for root, dirs, files in os.walk(directory):
        # 合并文件和目录（文件夹）一起处理
        items = files + dirs

        for item in items:
            # 获取文件或文件夹的完整路径
            old_path = os.path.join(root, item)

            # 分离文件名和扩展名
            name, ext = os.path.splitext(item)

            # 从右向左截取4个字符进行匹配
            if len(name) > 4:
                search_area = name[-4:]
            else:
                search_area = name

            # 匹配正则表达式，查找单个括号中的数字
            match = re.search(r'\((\d)\)$', search_area)

            if match:
                # 提取匹配的数字
                num = match.group(1)

                # 构造新的名称
                new_name = f"{name[:-len(search_area)]}{search_area[:-len(match.group(0))]}({int(num):02}){ext}"

                # 获取新的路径
                new_path = os.path.join(root, new_name)

                # 重命名文件或文件夹
                if old_path != new_path:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

# 执行脚本，搜索当前目录（或指定目录）
# 调整路径到你需要的起始目录
if __name__ == "__main__":
    # 替换为你想要检查的目录路径
    directory_to_check = '.'
    rename_files_in_directory(directory_to_check)