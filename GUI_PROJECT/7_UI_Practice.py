import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Image Merge")

# 파일 프레임
frame_file = Frame(root)
frame_file.pack(fill = "x", padx = 5, pady = 5)
btn_addfile = Button(frame_file, text = "파일추가", padx = 5, pady = 5, width = 12)
btn_addfile.pack(side = "left")
btn_deletefile = Button(frame_file, text = "선택삭제", padx = 5, pady = 5, width = 12)
btn_deletefile.pack(side = "right")

# 리스트 프레임
frame_list = Frame(root)
frame_list.pack(fill = "both", padx = 5, pady = 5)

scrollbar_filelist = Scrollbar(frame_list)
scrollbar_filelist.pack(side = "right", fill = "y")

listbox_filelist = Listbox(frame_list, selectmode = "extended", height = 15, yscrollcommand = scrollbar_filelist.set)
listbox_filelist.pack(side = "left", fill = "both", expand = True)

# 저장경로 프레임
frame_path = LabelFrame(root, text = "저장경로")
frame_path.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

entry_destpath = Entry(frame_path)
entry_destpath.pack(side = "left", fill = "x", expand = True, padx = 5, pady = 5, ipady = 4)

btn_destpath = Button(frame_path, text = "찾아보기", width = 10)
btn_destpath.pack(side = "right", padx = 5, pady = 5)

# 옵션 프레임
frame_opt = LabelFrame(root, text = "옵션")
frame_opt.pack(padx = 5, pady = 5)

label_width = Label(frame_opt, text = "가로넓이", width = 8)
label_width.pack(side = "left", padx = 5, pady = 5)

# 옵션 프레임 - 가로넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
combo_width = ttk.Combobox(frame_opt, state = "readonly", values = opt_width, width = 10)
combo_width.current(0)      # 기본값을 0번으로 지정
combo_width.pack(side = "left", padx = 5, pady = 5)

# 옵션 프레임 - 간격옵션
label_space = Label(frame_opt, text = "간격", width = 8)
label_space.pack(side = "left", padx = 5, pady = 5)

opt_space = ["없음", "좁게", "보통", "넓게"]
combo_space = ttk.Combobox(frame_opt, state = "readonly", values = opt_space, width = 10)
combo_space.current(0)
combo_space.pack(side = "left", padx = 5, pady = 5)

# 옵션 프레임 - 파일 포멧
label_format = Label(frame_opt, text = "포멧", width = 8)
label_format.pack(side = "left", padx = 5, pady = 5)

opt_format = ["png", "jpg", "bmp"]
combo_format = ttk.Combobox(frame_opt, state = "readonly", values = opt_format, width = 10)
combo_format.current(0)
combo_format.pack(side="left", padx = 5, pady = 5)

# 프로그레스바 프레임
frame_progress = LabelFrame(root, text = "진행상황")
frame_progress.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill = "x", padx = 5, pady = 5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady = 5)

btn_close = Button(frame_run, padx = 5, pady = 5, text = "닫기", width = 12)
btn_close.pack(side = "right", padx = 5, pady = 5)

btn_start = Button(frame_run, padx = 5, pady = 5, text = "시작", width = 12)
btn_start.pack(side = "left", padx = 5, pady = 5)

root.resizable(False, False)
root.mainloop()