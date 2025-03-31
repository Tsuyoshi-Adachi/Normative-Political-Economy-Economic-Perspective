import os
import pandas as pd

# 現在の作業ディレクトリ（mdファイルがあるフォルダ）を取得
folder_path = os.getcwd()

# スプレッドシート（Excel）ファイルのパスとシート名を指定
spreadsheet_path = 'data.xlsx'  # 例: 同じフォルダの場合 'data.xlsx'
sheet_name = 'Sheet1'  # シート名を適宜変更

# Excelファイルの読み込み
df = pd.read_excel(spreadsheet_path, sheet_name=sheet_name)

# 各行を処理
for index, row in df.iterrows():
    filename = row['B']  # B列: ファイル名
    prefix = row['C']    # C列: 5行目に追加する文字列
    suffix = row['D']    # D列: 末尾に追加する文字列

    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        # ファイルを行単位で読み込み
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 5行目（インデックス4）の位置にprefixを挿入（行数が足りない場合は末尾に追加）
        if len(lines) >= 4:
            lines.insert(4, prefix + "\n")
        else:
            lines.append(prefix + "\n")

        # ファイル末尾にsuffixを追加
        lines.append(suffix + "\n")

        # 更新内容を上書き保存
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"{filename} を更新しました。")
    else:
        print(f"{filename} が見つかりませんでした。")

print("処理が完了しました。")
