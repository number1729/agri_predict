import os

def combine_html_files(folder_path, output_file):
    # 結合するHTMLファイルのリストを初期化
    html_files = []

    # フォルダ内のHTMLファイルを取得
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    html_files.sort()
    
    # HTMLファイルを結合
    combined_html = ""
    for file_path in html_files:
        with open(file_path, "r") as file:
            combined_html += file.read()

    # 結合結果を出力ファイルに保存
    with open(output_file, "w") as output:
        output.write(combined_html)

    print(f"{len(html_files)} つのHTMLファイルを結合しました。結果は {output_file} に保存されました。")
    
combine_html_files("figure_html", "output_html.html")