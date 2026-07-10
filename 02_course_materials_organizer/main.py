import argparse
from course_organizer.core import run_task

def main():
    parser=argparse.ArgumentParser(description="课程资料自动整理工具")
    parser.add_argument("--source",required=True,help="原始资料文件夹路径")
    parser.add_argument("--target",required=True,help="整理后存放文件夹路径")
    parser.add_argument("--dry-run",action="store_true",help="仅预览整理计划，不操作文件")
    args=parser.parse_args()
    run_task(args.source,args.target,args.dry_run)

if __name__=="__main__":
    main()
