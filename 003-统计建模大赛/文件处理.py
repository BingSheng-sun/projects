import pandas as pd
import os
import csv

csv_folder_path = r"C:\Users\SUN\Desktop\我的素材\Excel learning\非期望产出核算"
output_folder_path = csv_folder_path  # 结果默认和原文件保存在同一文件夹


# ==============================================
# 【容错核心】安全读取CSV，解决编码+列数不一致报错
# ==============================================
def safe_read_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig', errors='replace') as f:
            reader = csv.reader(f)
            rows = list(reader)
        return pd.DataFrame(rows)
    except:
        pass
    try:
        with open(file_path, 'r', encoding='gbk', errors='replace') as f:
            reader = csv.reader(f)
            rows = list(reader)
        return pd.DataFrame(rows)
    except:
        return pd.read_csv(
            file_path,
            header=None,
            encoding="utf-8",
            dtype=str,
            on_bad_lines="skip",
            engine="python"
        )


# ==============================================
# 固定省份排序规则（北京市永远第一个）
# ==============================================
STANDARD_PROVINCE_ORDER = [
    "北京市", "天津市", "河北省", "山西省", "内蒙古自治区",
    "辽宁省", "吉林省", "黑龙江省",
    "上海市", "江苏省", "浙江省", "安徽省", "福建省", "江西省", "山东省",
    "河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省",
    "重庆市", "四川省", "贵州省", "云南省", "西藏自治区",
    "陕西省", "甘肃省", "青海省", "宁夏回族自治区", "新疆维吾尔自治区"
]


# ==============================================
# 1. 读取文件列表
# ==============================================
csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith(".csv")]
print(f"📂 找到{len(csv_files)}个指标文件：")
for i, file in enumerate(csv_files, 1):
    print(f"   {i:2d}. {file}")


# ==============================================
# 2. 批量处理每个指标文件（核心修复：列名传递）
# ==============================================
all_indicator_data = []

for file_name in csv_files:
    file_full_path = os.path.join(csv_folder_path, file_name)
    print(f"\n🔄 正在处理：{file_name}")

    # --------------------------
    # 步骤1：提取指标名
    # --------------------------
    indicator_name = file_name.replace(".csv", "").strip()
    print(f"   提取指标名：{indicator_name}")

    # --------------------------
    # 步骤2：安全读取CSV+清洗数据
    # --------------------------
    df_raw = safe_read_csv(file_full_path)
    # 适配新版本pandas：map替代applymap
    df_raw = df_raw.map(lambda x: str(x).strip() if pd.notna(x) else "")

    # --------------------------
    # 步骤3：定位表头+提取年份列（核心修复：直接用索引，避免列名错误）
    # --------------------------
    header_row_idx = 2
    header_row = df_raw.iloc[header_row_idx]

    # 提取年份列：所有带「年」字的列，用列索引定位
    year_col_indices = []
    year_cols = []
    for idx, col in enumerate(header_row):
        if "年" in str(col):
            year_col_indices.append(idx)
            year_cols.append(col)
    year_count = len(year_cols)

    if year_count == 0:
        print(f"   ❌ 未识别到有效年份列，跳过该文件")
        continue
    print(f"   识别到年份范围：{year_cols[-1]} → {year_cols[0]}，共{year_count}年")

    # --------------------------
    # 步骤4：提取有效省份数据（核心修复：直接用索引，彻底避免列名错误）
    # --------------------------
    # 省份列固定为第0列，从表头下一行开始取
    df_valid = df_raw.iloc[header_row_idx + 1 :, :].copy()
    # 提取省份列（第0列）和年份列（对应索引）
    province_col = df_valid.iloc[:, 0].tolist()
    year_value_cols = df_valid.iloc[:, year_col_indices].values.tolist()

    # 过滤无效省份行
    valid_provinces = []
    valid_values = []
    for p, v in zip(province_col, year_value_cols):
        p_clean = str(p).strip()
        if (p_clean != "" 
            and not pd.isna(p_clean) 
            and "注：" not in p_clean 
            and "数据来源" not in p_clean 
            and "nan" not in p_clean
            and "合计" not in p_clean
            and "全国" not in p_clean):
            valid_provinces.append(p_clean)
            valid_values.append(v)

    if len(valid_provinces) == 0:
        print(f"   ❌ 未识别到有效省份数据，跳过该文件")
        continue
    print(f"   有效省份数：{len(valid_provinces)} 个")

    # --------------------------
    # 步骤5：构建宽表→转长表（彻底避免列名错误）
    # --------------------------
    # 构建宽表DataFrame
    df_wide = pd.DataFrame(
        data=valid_values,
        columns=year_cols,
        index=valid_provinces
    )
    df_wide.index.name = "省份"
    df_wide.reset_index(inplace=True)

    # 宽表转长表
    df_melted = df_wide.melt(
        id_vars=["省份"],
        var_name="年份_str",
        value_name=indicator_name
    )

    # --------------------------
    # 步骤6：清洗数据
    # --------------------------
    # 清洗年份
    df_melted["年份"] = df_melted["年份_str"].str.replace("年", "", regex=False)
    df_melted["年份"] = pd.to_numeric(df_melted["年份"], errors="coerce")
    # 清洗数值
    df_melted[indicator_name] = pd.to_numeric(df_melted[indicator_name], errors="coerce")

    # 删除无效行、整理列顺序
    df_final = df_melted.dropna(subset=["年份"]).copy()
    df_final["年份"] = df_final["年份"].astype(int)
    df_final = df_final[["省份", "年份", indicator_name]].copy()

    # 加入总结果列表
    all_indicator_data.append(df_final)
    print(f"   ✅ 处理完成，有效样本量：{len(df_final)} 行")


# ==============================================
# 3. 合并所有指标+按标准顺序排序
# ==============================================
if len(all_indicator_data) == 0:
    print("\n❌ 没有成功处理任何文件，请检查路径和CSV格式！")
else:
    # 合并所有指标
    total_data = all_indicator_data[0]
    for df in all_indicator_data[1:]:
        total_data = pd.merge(total_data, df, on=["省份", "年份"], how="outer")

    # 强制按标准顺序排序
    total_data["省份"] = pd.Categorical(
        total_data["省份"],
        categories=STANDARD_PROVINCE_ORDER,
        ordered=True
    )
    total_data = total_data.sort_values(by=["省份", "年份"], ascending=[True, True]).copy()
    total_data["省份"] = total_data["省份"].astype(str)

    # ==============================================
    # 4. 保存最终结果
    # ==============================================
    total_output_path = os.path.join(output_folder_path, "农业投入指标_合并总表_标准长面板.csv")
    total_data.to_csv(total_output_path, index=False, encoding="utf-8-sig")

    # 保存单指标文件
    for df in all_indicator_data:
        ind_name = df.columns[2]
        single_output_path = os.path.join(output_folder_path, f"{ind_name}_标准长面板.csv")
        df.to_csv(single_output_path, index=False, encoding="utf-8-sig")

    # ==============================================
    # 5. 输出校验结果
    # ==============================================
    print("\n" + "="*70)
    print("🎉 所有农业投入指标处理完成！")
    print(f"📊 合并总表概况：")
    print(f"   • 总样本量：{len(total_data)} 行")
    print(f"   • 覆盖省份数：{len(total_data['省份'].unique())} 个")
    print(f"   • 覆盖年份范围：{total_data['年份'].min()} 年 - {total_data['年份'].max()} 年")
    print(f"   • 包含指标数：{len(total_data.columns)-2} 个")
    print(f"   • 指标列表：{list(total_data.columns[2:])}")
    print(f"\n🏆 最终省份排序（前10个，北京市首）：")
    top10_provinces = total_data["省份"].unique()[:10]
    for i, p in enumerate(top10_provinces, 1):
        print(f"   {i:2d}. {p}")
    print(f"\n📁 保存路径：")
    print(f"   所有指标合并总表：{total_output_path}")
    print("="*70)
    print("\n🔍 北京市前5行数据预览：")
    print(total_data[total_data["省份"] == "北京市"].head())