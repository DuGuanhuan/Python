num_subjects = int(input("How many subjects would you choose for this session: "))
remain_subjects = num_subjects  # 初始化剩余未选择的科目数量

for i in range(1, num_subjects + 1):
    is_continue = input("Would you like to continue subject enrolment? (Y/N): ")
    
    if is_continue == 'Y':
        subject_enrolled = input("Which subject would you like: ")
        print(f"You have successfully enrolled in {subject_enrolled}.")
        remain_subjects -= 1  # 每成功选择一个科目，剩余数量减少

    elif is_continue == 'N':
        if remain_subjects == 1:
            print(f"You have not completely finished the enrollment. There is 1 subject to be enrolled.")
        else:
            print(f"You have not completely finished the enrollment. There are {remain_subjects} subjects to be enrolled.")
        break

if remain_subjects == 0:
    print(f"You have finished the enrollment of all {num_subjects} subjects.")
