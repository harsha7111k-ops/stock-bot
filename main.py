from config import STOCKS, MIN_SCORE, TOP_N
from scanner import fetch_data
from strategy import score_stock, suggest_option
from notifier import send

results = []

for stock in STOCKS:
    df = fetch_data(stock)
    if df is None:
        continue

    score, reasons = score_stock(df)

    if score >= MIN_SCORE:
        results.append({
            "stock": stock,
            "score": score,
            "reasons": ", ".join(reasons),
            "trade": suggest_option(score)
        })

# sort
results = sorted(results, key=lambda x: x['score'], reverse=True)[:TOP_N]

# message
msg = "📊 AI STOCK PICKS\n\n"

for r in results:
    msg += (
        f"{r['stock']} → Score {r['score']}\n"
        f"Trade: {r['trade']}\n"
        f"Reason: {r['reasons']}\n\n"
    )

send(msg)
