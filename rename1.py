import os

def rename_files_in_subdirectories(root_directory):
    for current_path, dirnames, filenames in os.walk(root_directory):
        # 跳过根目录，只处理子文件夹
        if current_path == root_directory:
            continue

        # 获取相对于根目录的路径，并用下划线代替路径分隔符来构造新文件名的前缀
        relative_path = os.path.relpath(current_path, root_directory)
        subdir_names = relative_path.split(os.sep)
        prefix = '_'.join(filter(None, subdir_names))  # 过滤掉空元素（即根路径情况）

        # 按名称升序排序文件
        sorted_filenames = sorted(filenames)

        for index, filename in enumerate(sorted_filenames, start=1):
            # 获取文件的扩展名
            name, ext = os.path.splitext(filename)

            # 生成新的文件名
            new_filename = f"{prefix}_{index:03}{ext}"

            # 获取文件的旧路径和新路径
            old_file_path = os.path.join(current_path, filename)
            new_file_path = os.path.join(current_path, new_filename)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{old_file_path}' to '{new_file_path}'")

if __name__ == "__main__":
    # 使用当前工作目录
    base_directory = os.getcwd()
    rename_files_in_subdirectories(base_directory)