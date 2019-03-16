#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(0,n, 2):
        # 读取每一行
        people_num = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()

        i_scores = []
        all_samples = []
        for score in line.split():
            i_scores.append(int(score))
        all_sample.append([people_num, i_scores]))
    

       
    
    for sample in all_sample:
        N = sample[0]
        score = sample[1]
        score.index(max(score))        
        score_rever = score[::-1]
        
        
    #for i in range(1, all_sample[0][1])
    