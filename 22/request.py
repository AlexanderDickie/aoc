import os
import requests

def curl_input(day, part):
    if part==0:
        url = f"https://adventofcode.com/2022/day/{day}#"
    elif part==1:
        url = f"https://adventofcode.com/2022/day/{day}/input"
    else:
        url = f"https://adventofcode.com/2022/day/{day}/input"
    cookie = open("cookie-header.txt").read()[:-1]
    headers = {'Cookie': cookie}
    request = requests.get(url, headers=headers).text

    if part==0:
        # example input, find the longest <code> division and its probs that
        i = 0
        mx_len = 0
        example = 0
        while i < len(request):
            start = request.find("<code>", i)
            end = request.find("</code>", i+len("<code>"))
            if start == -1:
                break

            if end-start > mx_len:
                example = request[start+len("<code>"): end]
                mx_len = end-start

            i = end + len("</code>")
        return example
    else:
        return request

def get_input(day, part): 
    path = f"inputs/day{day}-{part}.txt"
    if os.path.exists(path):
        return open(path).read()
    else:
        print("curling input")
        input = curl_input(day, part)
        open(path, 'w').write(input)
        return input
