import os
import re

def rename_files_in_directory(root_dir):
    # 定义匹配的正则表达式模式
    pattern = re.compile(r'_[0-9]$')

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 遍历所有文件和文件夹
        for name in dirnames + filenames:
            # 分离文件名和扩展名
            base, ext = os.path.splitext(name)

            # 检查从右向左倒数4个字符内是否有匹配的模式
            if len(base) >= 4 and pattern.search(base[-4:]):
                # 查找匹配的数字并替换为两位格式
                new_base = pattern.sub(lambda x: f"_{int(x.group(0)[1]):02}", base)

                # 构建新的文件/文件夹名称
                new_name = new_base + ext

                # 原文件/文件夹的完整路径
                original_path = os.path.join(dirpath, name)

                # 新文件/文件夹的完整路径
                new_path = os.path.join(dirpath, new_name)

                # 重命名文件或文件夹
                os.rename(original_path, new_path)
                print(f'Renamed: {original_path} -> {new_path}')

if __name__ == "__main__":
    # 指定要搜索的目录（当前目录）
    root_directory = '.'
    rename_files_in_directory(root_directory)