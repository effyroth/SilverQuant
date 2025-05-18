

# from mytt.MyTT import *
from mytt.MyTT_advance import *
from mytt.MyTT_custom import *


def select(df: pd.DataFrame, code: str, quote: dict, ema_fast_period, ema_slow_period):
    if len(df.close) < 120:
        df['金叉'] = False
        df['死叉'] = False
        return df

    O = df.open
    C = df.close
    H = df.high
    L = df.low
    V = df.volume

    # ————— 参数模块（可自定义调整）—————
    短期均线周期 = ema_fast_period    # 短期EMA周期
    长期均线周期 = ema_slow_period    # 长期EMA周期
    
    # ————— 计算双均线 —————
    短期均线 = EMA(C, 短期均线周期)  # 短期EMA均线
    长期均线 = EMA(C, 长期均线周期)  # 长期EMA均线
    
    # ————— 均线金叉死叉判断 —————
    金叉 = CROSS(短期均线, 长期均线)    # 短期均线上穿长期均线
    死叉 = CROSS(长期均线, 短期均线)    # 短期均线下穿长期均线
    
    
    
    df['金叉'] = 金叉
    df['死叉'] = 死叉

    return df

