import os
import json

dataset = "cora"
ratio = 0.15

if __name__ == "__main__":

    arr = []
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                os.system("python3 run.py --dataset %s --gpu 0 --ratio %.3lf --rho %.1lf,%.1lf,%.1lf" % (
                    dataset, ratio, a / 10, b / 10, c / 10))

                score = float(open("temp/auc.txt", "r").readline()[:-1])
                arr.append((score, a / 10, b / 10, c / 10))

                break
            break
        break

    arr.sort()

    json.dump(arr, open("temp/%s.txt" % dataset, "w"), indent=2, ensure_ascii=False, sort_keys=True)
