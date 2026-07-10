#作业优先匹配关键字
HOME_KEY=["作业","练习","实验","任务"]
#后缀-文件夹映射字典
EXT_MAP={
    "slides":[".ppt",".pptx",".key"],
    "code":[".py",".ipynb",".c",".cpp",".java"],
    "data":[".csv",".xlsx",".json"],
    "documents":[".pdf",".doc",".docx",".txt",".md"],
    "images":[".png",".jpg",".jpeg",".gif"],
    "others":[]
}

def get_file_type(file_path):
    from pathlib import Path
    f=Path(file_path)
    fname=f.name
    #优先判断作业文件
    for word in HOME_KEY:
        if word in fname:
            return "homework"
    #匹配文件后缀
    ext=f.suffix.lower()
    for folder,ext_list in EXT_MAP.items():
        if ext in ext_list:
            return folder
    return "others"
