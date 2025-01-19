def bolinger(df,col,win=20):
    df['SMA'] = df[col].rolling(window=win).mean()
    df['SD'] = df[col].rolling(window=win).std()
    df['BB_UPPER'] = df['SMA'] + 2 * df['SD']
    df['BB_LOWER'] = df['SMA'] - 2 * df['SD']

    bb_upper = round(float(df['BB_UPPER'].iloc[-1]),2)
    bb_lower = round(float(df['BB_LOWER'].iloc[-1]),2)
    bb_mean = round(float(df['SMA'].iloc[-1]),2)

    return [ bb_lower, bb_mean, bb_upper]


def rsi(df,col,win=14):
    change = df[col].diff()
    change.dropna(inplace=True)

    # two copies 
    change_up = change.copy()
    change_down = change.copy()

    # zero out opposite trend
    change_up[change_up<0] = 0
    change_down[change_down>0] = 0

    # verify the above zero outting
    change.equals(change_up+change_down)

    # averages 
    avg_up = change_up.rolling(14).mean()
    avg_down = change_down.rolling(14).mean().abs()

    # relative stregth
    rsi = 100 * avg_up / (avg_up + avg_down)

    # Take a look at the 20 oldest datapoints
    rsi.dropna(inplace=True)
    #self.rsi = rsi

    return round(rsi.iloc[-1],2)


def macd(df,col, fast=12, slow=26, signal=9):
    df[f'EMA{fast}'] = df[col].ewm(span=fast, adjust=False).mean()
    df[f'EMA{slow}'] = df[col].ewm(span=slow, adjust=False).mean()
    df['MACD'] = df[f'EMA{fast}'] - df[f'EMA{slow}']
    df['sline'] = df['MACD'].ewm(span=signal, adjust=False).mean()

    macd = round(float(df['MACD'].iloc[-1]),2)
    signal = round(float(df['sline'].iloc[-1]),2)
    return [macd,signal]


def history(df,col):
    week = 5 * -1
    month = week * 4
    month_3 = month * 3
    year = month  * 12

    d_last= round(float(df[col].iloc[-2]),2) 
    d_week= round(float(df[col].iloc[week]),2) 
    d_month= round(float(df[col].iloc[month]),2) 
    d_month_3 = round(float(df[col].iloc[month_3]),2) 
    d_year = round(float(df[col].iloc[year]),2) 


    p_week = round(((d_last - d_week) / d_last) * 100,2)
    p_month = round(((d_last - d_month) / d_last) * 100,2)
    p_month_3 = round(((d_last - d_month_3) / d_last) * 100,2)
    p_year = round(((d_last - d_year) / d_last) * 100,2)

    return [ p_week, p_month, p_month_3, p_year ]


def last_entry(df,col):
    return round(float(df[col].iloc[-1]),2) 