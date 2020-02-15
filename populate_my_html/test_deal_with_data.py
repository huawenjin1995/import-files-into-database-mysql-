from deal_with_data import DIR, File





if __name__ == '__main__':
    import _thread
    dirs = DIR('/home/huawenjin/learning_materials/python学习资料/html/')
    dirs.getFileName()  # 获取目录中所有文件名
    print(dirs)
    print(dirs.files)
