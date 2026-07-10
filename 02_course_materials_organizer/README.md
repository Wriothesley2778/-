# 课程资料整理器
## 一、功能说明
自动扫描文件夹内课程文件，**作业关键字优先级高于后缀**，默认复制文件不删除源文件；支持dry-run预览模式，自动处理重名文件避免覆盖，整理完成生成`整理报告.txt`。

## 二、分类规则
1. 文件名含【作业/练习/实验/任务】→ homework文件夹
2. 其余按后缀分类：
ppt/pptx/key → slides
py/ipynb/c/cpp/java → code
csv/xlsx/json → data
pdf/doc/docx/txt/md → documents
png/jpg/jpeg/gif → images
未知后缀 → others

## 三、运行命令（验收命令）
1. 预览模式（不生成任何文件夹、文件）
python main.py --source sample_materials --target organized_materials --dry-run

2. 正式复制整理（生成目录与报告）
python main.py --source sample_materials --target organized_materials

## 四、运行输出示例
### dry-run预览输出
执行模式:预览模式(dry-run)
本次整理文件总数:9
------------------------------
源:sample_materials\Python第01讲_基础语法.pptx → 目标:organized_materials\slides\Python第01讲_基础语法.pptx 分类:slides
源:sample_materials\Python第01讲_课堂代码.py → 目标:organized_materials\code\Python第01讲_课堂代码.py 分类:code
源:sample_materials\Python第01讲_作业说明.pdf → 目标:organized_materials\homework\Python第01讲_作业说明.pdf 分类:homework
源:sample_materials\NumPy数组练习.ipynb → 目标:organized_materials\code\NumPy数组练习.ipynb 分类:code
源:sample_materials\成绩样例.csv → 目标:organized_materials\data\成绩样例.csv 分类:data
源:sample_materials\课程通知.txt → 目标:organized_materials\documents\课程通知.txt 分类:documents
源:sample_materials\学生问题记录.md → 目标:organized_materials\documents\学生问题记录.md 分类:documents
源:sample_materials\截图_环境配置.png → 目标:organized_materials\images\截图_环境配置.png 分类:images
源:sample_materials\未分类文件.xyz → 目标:organized_materials\others\未分类文件.xyz 分类:others
------------------------------
各类文件数量统计:
slides:1个
code:2个
homework:1个
data:1个
documents:2个
images:1个
others:1个

dry-run仅预览，未创建/复制任何文件

### 正式复制输出
执行模式:复制模式
本次整理文件总数:9
[同上文件映射列表省略]
------------------------------
各类文件数量统计:
slides:1个
code:2个
homework:1个
data:1个
documents:2个
images:1个
others:1个

整理完成，报告保存至:organized_materials\整理报告.txt

## 五、程序体现Python的作用
1. 快速编写自动化脚本：几行代码实现批量文件分类，替代手动拖拽整理
2. 高效处理文件与路径：pathlib内置跨平台路径操作，不用手动拼接分隔符
3. 模块化分层解耦：规则、核心逻辑、入口分离，字典统一管理分类规则，便于修改扩展
4. 命令行参数灵活调用：argparse实现无交互脚本，可自定义源目录、目标目录、预览模式
5. 安全可控：先生成整理计划再执行操作，预览模式规避误操作，自动重名防止覆盖

## 六、知识点对应学习目标
1. Path与字符串路径：Path是面向对象路径，自带.name/.suffix/.parent属性，自动适配Windows/Linux；字符串路径需手动切割拼接，跨平台易出错
2. argparse：解析终端输入的--source/--target/--dry-run参数，无需手动input交互，脚本可批量调度
3. 先建整理计划再执行：先扫描全部文件生成完整映射列表，预览模式直接打印计划；正式执行统一遍历复制，逻辑分离、安全校验
4. 字典存储后缀规则：EXT_MAP字典键为分类文件夹，值为后缀列表，新增文件类型仅修改字典，不改动业务代码
5. 程序分层：main.py入口解析参数、rules.py存放分类规则、core.py实现文件扫描/计划生成/复制/报告核心逻辑
