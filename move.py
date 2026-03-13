import os
import shutil

def move_files_and_cleanup():
    current_folder = os.getcwd()

    # 列出当前文件夹中的所有项
    for item in os.listdir(current_folder):
        item_path = os.path.join(current_folder, item)

        # 检查该项是否为目录
        if os.path.isdir(item_path):
            # 尝试移动子文件夹内的所有文件
            try:
                for root, _, files in os.walk(item_path):
                    for file in files:
                        source_file = os.path.join(root, file)
                        destination_file = os.path.join(current_folder, file)

                        # 检查目标文件是否已经存在
                        if os.path.exists(destination_file):
                            print(f"文件名冲突：'{file}' 已存在于 '{current_folder}'，"
                                  f"因此保留文件夹 '{item}'。")
                            # 如果有冲突，保留当前文件夹，跳过剩下的操作
                            raise FileExistsError

                        # 移动文件
                        shutil.move(source_file, current_folder)

                # 如果没有发生冲突，删除空的子文件夹
                shutil.rmtree(item_path)
                print(f"成功处理且删除文件夹 '{item}'。")

            except FileExistsError:
                continue

if __name__ == "__main__":
    move_files_and_cleanup()