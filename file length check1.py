import os
import shutil

def check_file_name_length_and_copy(base_dir, destination_dir):
    # 确保目标文件夹存在
    os.makedirs(destination_dir, exist_ok=True)

    # 打开结果文件用于写入
    with open("file_length_check.txt", "w", encoding="utf-8") as f_out:
        # 遍历文件夹及其子文件夹
        for root, _, files in os.walk(base_dir):
            for file in files:
                # 检查文件名长度
                file_path = os.path.join(root, file)
                if len(file.encode('utf-8')) > 255:
                    f_out.write(f"文件名: {file}\n路径: {file_path}\n\n")

                    # 复制文件到目标文件夹
                    shutil.copy(file_path, destination_dir)

# 使用当前文件夹作为起始目录，并指定目标文件夹
current_dir = os.getcwd()
destination_folder = "specified_folder"  # 请替换为您指定的文件夹路径
check_file_name_length_and_copy(current_dir, destination_folder)