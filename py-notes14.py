'''Execute trades, leverage and sma'''

def initialize(context):
    context.appl = sid(24)

def handle_data(context, data): #It runs for every minutes, it is a problem fot the algotithm when the sma 20 is crossing with the sma50 manytimes in a short period
    hist = data.history(context.appl, 'price', 50, '1d')
    log.info(hist.head())

    #simple moving average
    sma_50 = hist.mean()
    sma_20 = hist[-20:].mean()

    open_orders = get_open_orders()

    if sma_20 > sma_50:
        if context.appl not in open_orders:
            order_target_percemt(context.appl, 1.0) #Target to have 100% of portfolio in Apple
    elif sma_50 > sma_20:
        if context.appl not in open_orders:
            order_target_percemt(context.appl, -1.0)  # Target to short 100% of portfolio in Apple

    #Check the leverage to ensure it is realistic
    record(leverage = context.account.leverage)
