from pathlib import Path
import shutil
from course_organizer.rules import get_file_type

#遍历源目录获取所有文件
def scan_source(src_dir):
    src=Path(src_dir)
    file_list=[]
    for item in src.iterdir():
        if item.is_file():
            file_list.append(item)
    return file_list

#处理重名文件，自动加后缀_1/_2
def fix_dup(target_path):
    if not target_path.exists():
        return target_path
    stem=target_path.stem
    suffix=target_path.suffix
    parent=target_path.parent
    num=1
    while True:
        new_p=parent/f"{stem}_{num}{suffix}"
        if not new_p.exists():
            return new_p
        num+=1

#生成整理计划：[(源路径,目标路径,分类文件夹)]
def make_plan(source,target):
    src_root=Path(source)
    dst_root=Path(target)
    files=scan_source(src_root)
    plan=[]
    for f in files:
        cat=get_file_type(f)
        dst_folder=dst_root/cat
        raw_dst=dst_folder/f.name
        real_dst=fix_dup(raw_dst)
        plan.append((str(f),str(real_dst),cat))
    return plan

#执行整理/预览，生成报告
def run_task(source,target,dry_run=False):
    plan=make_plan(source,target)
    report=[]
    cat_count={}
    total=len(plan)
    run_mode="预览模式(dry-run)" if dry_run else "复制模式"
    report.append(f"执行模式:{run_mode}")
    report.append(f"本次整理文件总数:{total}")
    report.append("-"*30)
    for src,dst,cat in plan:
        cat_count[cat]=cat_count.get(cat,0)+1
        line=f"源:{src} → 目标:{dst} 分类:{cat}"
        report.append(line)
        print(line)
        #非预览模式才复制文件
        if not dry_run:
            dst_parent=Path(dst).parent
            dst_parent.mkdir(exist_ok=True,parents=True)
            shutil.copy2(src,dst)
    report.append("-"*30)
    report.append("各类文件数量统计:")
    for c,count in cat_count.items():
        report.append(f"{c}:{count}个")
    #仅真实复制时生成报告文件
    if not dry_run:
        report_file=Path(target)/"整理报告.txt"
        report_file.write_text("\n".join(report),encoding="utf-8")
        print(f"\n整理完成，报告保存至:{report_file}")
    else:
        print("\ndry-run仅预览，未创建/复制任何文件")
    return report
