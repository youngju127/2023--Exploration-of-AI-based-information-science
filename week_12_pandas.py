import pandas as pd

df1 = pd.DataFrame({
     "a" : [11, -2, 7],
     "b" : [9, 0, 77],
     "c" : [55, 33, 19]
     }, index=[1, 2, 3])
df2 = pd.DataFrame(
    [[11, 9, 55],
     [-2, 0, 33],
     [7, 77, 19]],
    index=[1,2,3],
    columns=["a", "b", "c"])
df3 = df1.melt().rename(columns={
    'variable' : 'var',
    'value' : 'val'
}).query('val > 10')
print(df3)
