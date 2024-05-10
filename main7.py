
from seminar_7 import task_7
from seminar_7_HW import hw7_task_1
from pathlib import Path



if __name__ == '__main__':
    
    task_7.sort_files(Path('dir'))
    hw7_task_1.group_files_rename(Path('dir'), end_file='_file_',digits=3,
                       extention_before='rnd', extention_after='doc',
                       name_range=[3, 6])
