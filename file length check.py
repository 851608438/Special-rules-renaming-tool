import os
import shutil

def check_and_copy_long_filenames(source_directory, destination_directory, log_file_path):
    # 确保目标文件夹存在
    os.makedirs(destination_directory, exist_ok=True)

    # 打开日志文件进行写入
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        # 遍历指定目录下的所有文件
        for root, dirs, files in os.walk(source_directory):
            for file_name in files:
                # 将文件名编码为字节并检查其长度
                if len(file_name.encode('utf-8')) > 255:
                    full_file_path = os.path.join(root, file_name)
                    print(f"文件名超过 255 字节: {full_file_path}")

                    # 将文件名写入日志文件
                    log_file.write(full_file_path + '\n')

                    # 将文件复制到目标文件夹
                    shutil.copy2(full_file_path, destination_directory)

# 指定源目录、目标目录和日志文件路径
source_directory = 'D:\Music'
destination_directory = 'D:\Music1'
log_file_path = 'D:\Music1/log_file.txt'

# 运行函数
check_and_copy_long_filenames(source_directory, destination_directory, log_file_path)
