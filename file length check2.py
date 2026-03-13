import os

def shorten_filename(filename):
    # 计算文件名的字节长度
    length = len(filename.encode('utf-8'))

    # 如果文件名长度不超过255字节，就不需要缩短
    if length <= 255:
        return filename

    # 计算需要替换的字节数
    replace_length = length // 2

    # 计算前后两端需要保留多少字节
    prefix_length = (length - replace_length) // 2
    suffix_length = length - replace_length - prefix_length

    # 获取前缀部分和后缀部分
    prefix = filename.encode('utf-8')[:prefix_length].decode('utf-8', 'ignore')
    suffix = filename.encode('utf-8')[-suffix_length:].decode('utf-8', 'ignore')

    # 用 "..." 替换中间部分
    shortened_filename = prefix + "..." + suffix

    return shortened_filename

def process_files_in_directory(root_directory):
    for root, _, files in os.walk(root_directory):
        for file in files:
            original_filepath = os.path.join(root, file)
            shortened_file = shorten_filename(file)
            if shortened_file != file:
                # 重命名文件
                shortened_filepath = os.path.join(root, shortened_file)
                os.rename(original_filepath, shortened_filepath)
                print(f'Renamed: {original_filepath} -> {shortened_filepath}')

# 使用当前目录作为起始目录
start_directory = os.getcwd()
process_files_in_directory(start_directory)