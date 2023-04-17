import time
import subprocess

start_time = time.time()

## source code
file_path = "/Users/ryuhansol/workspace/helloAlgorithms/boj/haryu/10950.py"

# 표준 입력으로 전달할 데이터
input_data = "5\n1 1\n2 3\n3 4\n9 8\n5 2"  # 표준 입력으로 전달할 데이터를 입력하세요

# Popen 객체 생성
process = subprocess.Popen(["python3", file_path], stdin=subprocess.PIPE)

# 표준 입력으로 데이터 전송
process.communicate(input_data.encode())  # 문자열 데이터를 바이트로 변환하여 전송

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_formatted = round(elapsed_time, 10)
print("Code Processed: ", elapsed_time_formatted, "sec")