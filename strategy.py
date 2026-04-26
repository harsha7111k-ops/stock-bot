def score_stock(df):
    latest = df.iloc[-1]
    score = 0
    reasons = []

    if latest['EMA20'] > latest['EMA50']:
        score += 20
        reasons.append("Trend")

    if latest['RSI'] > 55:
        score += 15
        reasons.append("Momentum")

    if latest['Volume'] > latest['VolAvg']:
        score += 15
        reasons.append("Volume")

    if latest['Close'] > df['Close'].iloc[-5]:
        score += 15
        reasons.append("Breakout")

    if abs(latest['Close'] - latest['EMA20']) / latest['Close'] < 0.01:
        score += 10
        reasons.append("Pullback")

    return score, reasons


def suggest_option(score):
    if score >= 85:
        return "BUY CE (ITM)"
    elif score >= 70:
        return "BUY CE (ATM)"
    elif score < 50:
        return "BUY PE"
    return "NO TRADE"
