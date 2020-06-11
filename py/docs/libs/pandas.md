# pandas

## basics
- 选取特定列
```
mydf[['city_name','code','country_ISO_Code','Sub_Region_Code']]
```
- dropna 删除空内容
```
 # 删除含有空数据的全部行
df4 = pd.read_csv('4.csv',  encoding='utf-8')
df4 = df4.dropna()
# 可以通过axis参数来删除含有空数据的全部列
df4 = df4.dropna(axis=1)
# 可以通过subset参数来删除在age和sex中含有空数据的全部行
df4 = df4.dropna(subset=["age", "sex"])
```
- 获取特定的行列
```
df.iloc[0:2]#前2行
df.iloc[0]#第0行
df.iloc[0:2,0:2]#0、1行，0、1列
df.iloc[[0,2],[1,2,3]]#第0、2行，1、2、3列
df.loc([0], ['size'])  选择“size”列的第一行
```
- 重命名一列
```
df.rename(columns = {df.columns[2]:'size'}, inplace=True)
```


## apply
- apply使用多列计算生成新的列
```
data["x1"]=data[["a","b"]].apply(lambda x:x["a"]+x["b"],axis=1)

self.right_lane_all["c3_gap"]=self.right_lane_all[["c3","c3_eyeq"]].apply(lambda x: abs(x["c3"]- x["c3_eyeq"]), axis=1)

```
## merge
- merge

```
self.left_lane_all.merge(self.right_lane_all, left_on='img_path', right_on='img_path',  suffixes=('_left', '_right'))
在相同的列名分别修正加上后缀
```

## sort
- sort_values
```
lane_all_sorted = lane_all.sort_values(by="c0_gap", ascending=False)

```
## merge_asof
```
# 相同的列名加后缀进行区分
self.left_lane_all = pd.merge_asof(left_lane_df, eyeq4_left_lane, left_on="t_send",\
             right_on="t_send", tolerance=precision, direction="nearest", suffixes=("", "_eyeq"))
```

## count,  null 判断
```
self.left_lane_all['img_path'].isnull().sum()
```

## groupby
```
df.groupby("img").apply(lambda x: iou_join(x, IOU_thresh))

def iou_join(group_df, IOU_thresh):
    NM_columns = ["label_NM", "score_NM", "x_NM", "y_NM", "w_NM", "h_NM"]
    df_NM = group_df[NM_columns].dropna()
    strong_columns = ["label_strong", "score_strong", "x_strong", "y_strong", "w_strong", "h_strong"]
    df_strong = group_df[strong_columns].dropna()
    matched_id = []
    matched_IOU = []
    for x1, y1, w1, h1 in df_NM[["x_NM", "y_NM", "w_NM", "h_NM"]].values:
        iou = get_IOU_by_df(x1, y1, w1, h1, df_strong, {"x": "x_strong", "y": "y_strong", "w": "w_strong", "h": "h_strong"})
        if iou.empty:
            max_value = 0
        else:
            max_ind = iou.idxmax()
            max_value = iou.loc[max_ind]
        if max_value >= IOU_thresh:
            matched_id.append(max_ind)
            matched_IOU.append(max_value)
        else:
            matched_id.append(-1)
            matched_IOU.append(None)
    df_NM = df_NM.assign(matched_id=matched_id, iou=matched_IOU)    
    df = pd.merge(df_NM, df_strong, left_on="matched_id", right_index=True, how='outer')
    return df

 def get_IOU_by_df(x1,y1,w1,h1, df, bbox_namings={"x":"x", "y":"y", "w":"w", "h":"h"}):
    #Computer left-bottom from width and height
    
    x2 = df[bbox_namings["x"]]
    y2 = df[bbox_namings["y"]]
    w2 = df[bbox_namings["w"]]
    h2 = df[bbox_namings["h"]]

    X1 = x1 + w1
    Y1 = y1 + h1
    X2 = x2 + w2
    Y2 = y2 + h2

    # xx = max(x1,x2)
    xx = x2.apply(lambda v: max(x1, v))
    # XX = min(X1,X2)
    XX = X2.apply(lambda v: min(X1, v))
    # yy = max(y1,y2)
    yy = y2.apply(lambda v: max(y1, v))
    # YY = min(Y1,Y2)
    YY = Y2.apply(lambda v: min(Y1, v))
    # m = max(0., XX-xx)
    m = (XX-xx).apply(lambda v: max(0, v))
    # n = max(0., YY-yy)
    n = (YY-yy).apply(lambda v: max(0, v))
    # print(m,n)
    intersection = m*n
    # print(intersection)
    union = (X1-x1)*(Y1-y1)+(X2-x2)*(Y2-y2)-intersection
    # print(union)
    return (intersection/union)   
```

## df['ImageName'].unique().tolist()

## FAQ

### How to select rows from a DataFrame based on column values?
https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values

### How to iterate over rows in a DataFrame in Pandas?
https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas

```
for index, row in df.iterrows():
    print(row['c1'], row['c2'])
```