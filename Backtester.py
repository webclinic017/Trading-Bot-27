class Backtester:
    def __init__(self, data, strategy,selected_strategy,initial_account_value, ivestment_amount,fee_per_trade):
        self.data = data
        self.strategy = strategy
        self.selected_strategy = selected_strategy
        self.initial_account_value = initial_account_value
        self.ivestment_amount = ivestment_amount
        self.fee_per_trade = fee_per_trade


    # def run_backtest(self, **kwargs):
    #     params = kwargs
    #     # Create a copy of the data to avoid modifying the original
    #     data = self.data.copy()
        
    #     # Apply the strategy to the data
    #     signals = self.strategy.generate_signals_backtest(data,self.selected_strategy,**params)
    #     # Calculate the total profit in whole dollars
    #     total_profit,account_value,signals= self.calculate_total_profits(signals,self.initial_account_value,self.ivestment_amount,self.fee_per_trade)
        
    #     # Calculate sharpe ratio
    #     sharpe_ratio = self.calculate_sharpe_ratio(signals)
       
    #     # Calculate win rate
    #     win_rate = self.calculate_win_rate(signals)
    #     signals.to_csv('signals.csv')
    #     # Return the results
    #     return {'sharpe_ratio': sharpe_ratio, 'innitial_account_value':self.initial_account_value, 'account_value': account_value,'total_profit': total_profit, 'win_rate': win_rate}
      
        

    # def calculate_total_profits(self, data, initial_account_value, investment_amount, fee_per_trade):
    #     """
    #     Calculates the total profits from a trading strategy given a DataFrame with closing prices and trade signals.

    #     Args:
    #     - data: A Pandas DataFrame with columns "close" (closing prices) and "signal" (trade signals, where 1 represents a buy signal, 0 represents a hold signal, and -1 represents a sell signal).
    #     - initial_account_value: The total amount of money in the account at the start of the trading period.
    #     - dollar_amount_spent_per_trade: The dollar amount spent on each trade.
    #     - fee_per_trade: The fee associated with each trade.

    #     Returns:
    #     - The total profits (or losses) from the trading strategy.
    #     """
    #     account_value = initial_account_value
    #     num_shares = 0
    #     num_trades = 0
    #     total_profit = 0
    #     data['Account Value'] = 0
    #     data['Gains/Losses'] = 0
    #     for i in range(len(data)):
    #         if data['Signal'][i] == 1: # Buy signal
    #             # Calculate how many tokens were purchased with the investment amount, factoring in the trading fee
    #             num_shares = (investment_amount - (fee_per_trade*100)) / data['Close'][i]
    #             # Deduct the total investment amount and trading fee from the account value
    #             account_value -= investment_amount 
    #             data['Account Value'][i] = account_value
    #         elif data['Signal'][i] == -1: # Sell signal
    #             # Calculate the gross proceeds from selling the tokens, factoring in the trading fee
    #             gross_proceeds = num_shares * data['Close'][i] - (fee_per_trade*100)
    #             # Calculate the profit or loss from the trade
    #             profit_loss = gross_proceeds - investment_amount
    #             # Add the profit or loss to the total profit
    #             total_profit += profit_loss
    #             # Add the gross proceeds (minus trading fee) to the account value
    #             account_value += gross_proceeds
    #             # Reset the number of shares to 0
    #             num_shares = 0
    #             # Increment the number of trades counter
    #             num_trades += 1

    #             data['Account Value'][i] = account_value
    #             data['Gains/Losses'][i] = profit_loss
    #         else: # Hold signal
    #             data['Account Value'][i] = account_value

    #     # Add the final account value to the total profit
    #     total_profit += account_value - initial_account_value

        
        
    #     return total_profit,account_value,data
    
    # def calculate_sharpe_ratio(self,data):
    #     """
    #     Calculate the Sharpe Ratio from a DataFrame of daily closing prices.

    #     Parameters:
    #     df_prices (pandas.DataFrame): A DataFrame of daily closing prices.

    #     Returns:
    #     float: The Sharpe Ratio.
    #     """

    #     # Calculate the daily returns based on the trade signals
    #     data['Returns'] = data['Signal'] * (data['Close'] - data['Close'].shift(1)) / data['Close'].shift(1)

    #     # Calculate the Sharpe ratio
    #     R_p = data['Returns'].mean() * 252
    #     R_f = 0.02 # Assume a risk-free rate of 2%
    #     sigma_p = data['Returns'].std() * np.sqrt(252)
    #     sharpe_ratio = (R_p - R_f) / sigma_p


    #     return sharpe_ratio
    
    # def calculate_win_rate(self,data):
    #     """
    #     Calculate the win rate for a trading strategy based on a DataFrame of closing prices and signals.

    #     Parameters:
    #     data (pandas.DataFrame): A DataFrame containing closing prices and signals.

    #     Returns:
    #     float: The win rate as a percentage.
    #     """
    #     # Calculate the number of winning and losing trades
    #     num_wins = len(data[data['Gains/Losses'] > 0])
    #     num_losses = len(data[data['Gains/Losses'] < 0])
        
    #     if num_losses == 0 and num_wins == 0:
    #         win_rate = 0
    #     # Calculate the win rate as a percentage
    #     else:
    #         win_rate = num_wins / (num_wins + num_losses) * 100

    #     return win_rate
    
    # def plot_backtest(self,indicator=None, **params):    
    #     # Create a copy of the data to avoid modifying the original
    #     data = self.data.copy()
        
        
    #     # Apply the strategy to the data
    #     signals = self.strategy.generate_signals_backtest(data,self.selected_strategy,**params)
    #     # Create a candlestick chart of the data
    #     candlestick = go.Candlestick(
    #         x=data['Date'],
    #         open=data['Open'],
    #         high=data['High'],
    #         low=data['Low'],
    #         close=data['Close']
    #     )

    #     # Create a scatter plot of the buy and sell signals
    #     buys = signals[signals['Signal'] == 1]
    #     sells = signals[signals['Signal'] == -1]

    #     buy_scatter = go.Scatter(
    #         x=buys['Date'],
    #         y=buys['Close'],
    #         mode='markers',
    #         name='Buy',
    #         marker=dict(
    #             symbol='triangle-up',
    #             size=10,
    #             color='green'
    #         )
    #     )

    #     sell_scatter = go.Scatter(
    #         x=sells['Date'],
    #         y=sells['Close'],
    #         mode='markers',
    #         name='Sell',
    #         marker=dict(
    #             symbol='triangle-down',
    #             size=10,
    #             color='red'
    #         )
    #     )
        
    #     # Create a layout for the chart with a secondary axis for the RSI plot
    #     fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    #     # Add the candlestick chart to the first row of the subplot
    #     fig.add_trace(candlestick, row=1, col=1)

    #     # Add the buy and sell signals to the first row of the subplot
    #     fig.add_trace(buy_scatter, row=1, col=1)
    #     fig.add_trace(sell_scatter, row=1, col=1)

    #     # Create a plot of the RSI indicator, if provided, and add it to the second row of the subplot
    #     if indicator is not None:
    #         rsi_trace = go.Scatter(
    #             x=data['Date'],
    #             y=indicator,
    #             name='RSI'
    #         )
    #         fig.add_trace(rsi_trace, row=2, col=1)

    #     # Update the layout to include a title and axis labels
    #     fig.update_layout(
    #         title='Trading Signals',
    #         xaxis=dict(title='Date', tickformat='%Y-%m-%d %H:%M:%S'),
    #         yaxis=dict(title='Price', domain=[0.2, 1]),
    #         yaxis2=dict(title='RSI', domain=[0, 0.15])
    #     )

    #     # Display the figure
    #     fig.show()
       
       
    
    # def optimize_parameters(self, parameter_values):
    #     results = []
    #     with tqdm(total=len(parameter_values)) as pbar:
    #         for params in parameter_values:
    #             try:
    #                 result = self.run_backtest(**params)
    #                 result.update(params)
    #                 results.append(result)
    #                 pbar.update(1)
    #             except:
    #                 continue
            
    #     results_df = pd.DataFrame(results)
    #     try:
    #         max_win_ratio = results_df['win_rate'].max()
    #         max_win_ratio_params = results_df.loc[results_df['win_rate'].idxmax()].to_dict()
    #     except:
    #         max_win_ratio = 0
    #         max_win_ratio_params = {}
        
    #     return {'max_sharpe_ratio': max_win_ratio, 'max_sharpe_ratio_params': max_win_ratio_params}