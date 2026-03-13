import os

def rename_files_in_subdirectories(base_dir):
    # 遍历当前目录下的所有条目
    for entry in os.listdir(base_dir):
        entry_path = os.path.join(base_dir, entry)

        # 如果条目是一个目录，则处理该子文件夹中的文件
        if os.path.isdir(entry_path):
            files = os.listdir(entry_path)
            # 按名称递增排序文件列表
            files.sort()

            # 重命名子文件夹中的文件
            for idx, file_name in enumerate(files, start=1):
                file_path = os.path.join(entry_path, file_name)

                # 如果条目是文件，进行重命名
                if os.path.isfile(file_path):
                    # 提取文件扩展名
                    file_extension = os.path.splitext(file_name)[1]
                    # 构建新的文件名
                    new_file_name = f"{entry}_{str(idx).zfill(3)}{file_extension}"
                    new_file_path = os.path.join(entry_path, new_file_name)

                    # 重命名文件
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file_path}' to '{new_file_path}'")

# 指定当前工作的目录，即我们要处理的基目录
base_directory = os.getcwd()
rename_files_in_subdirectories(base_directory)