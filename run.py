import os
import subprocess

# フォルダ名のリスト
folders = [
    "chips",
    "chocolate",
    "cookie",
    "fried dough cookie",
    "marshmallow",
    "ramune",
    "rice cracker",
    # "sandwich cookie",
    # "small ramune",
    "snack",
    "soft candy",
    "stick snack"
]

# 各フォルダに対してコマンドを実行
for folder in folders:
    # コマンドを作成
    command = f"anomalib train --data notebooks/tools/yaml/{folder}_classification.yaml --model anomalib.models.Patchcore --task CLASSIFICATION"
    print(f"Executing: {command}")

    # コマンドを実行
    result = subprocess.run(command, shell=True)

    # 結果をチェック
    if result.returncode != 0:
        print(f"Error occurred while training on {folder}.")
