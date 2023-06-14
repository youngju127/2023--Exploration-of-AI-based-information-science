import pandas as pd

def double(n):
    """
    x2
    :param n:
    :return:
    """
    return n * 2


df1 = pd.DataFrame({
     "a" : [7, -2, 7],
     "b" : [9, 0, 7],
     "c" : [7, 7, 7]
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
}).sort_values('val', ascending=False)
#print(df3['val'].nunique())
print(df1.apply(lambda x : x*x))
