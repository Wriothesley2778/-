import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta

def generate_stock_prices(start_price=100,days=252,mu=0.08,sigma=0.2):
    dt=1/252
    prices=np.zeros(days)
    prices[0]=start_price
    for i in range(1,days):
        drift=(mu-0.5*sigma**2)*dt
        shock=sigma*np.sqrt(dt)*np.random.normal(0,1)
        prices[i]=prices[i-1]*np.exp(drift+shock)
    base_day=datetime.now()
    dates=[base_day-timedelta(days=days-1-i) for i in range(days)]
    return dates,prices

def calculate_daily_returns(prices):
    returns=np.diff(prices)/prices[:-1]
    return returns

def calculate_volatility(returns,annualize=True):
    daily_vol=np.std(returns)
    if annualize:
        return daily_vol*np.sqrt(252)
    return daily_vol

def calculate_moving_average(prices,window):
    weights=np.ones(window)/window
    ma=np.convolve(prices,weights,mode='valid')
    return ma

def portfolio_risk_analysis(returns_matrix):
    cov_matrix=np.cov(returns_matrix)
    var_vector=np.diag(cov_matrix)
    equal_weights=np.ones(len(var_vector))/len(var_vector)
    portfolio_var=equal_weights@cov_matrix@equal_weights
    portfolio_std=np.sqrt(portfolio_var)
    return cov_matrix,var_vector,portfolio_var,portfolio_std

def plot_stock_prices(dates,prices,ticker="Stock"):
    plt.figure(figsize=(12,6))
    plt.plot(dates,prices,label=f'{ticker} Price')
    plt.title(f'{ticker} Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{ticker.lower()}_price.png')
    plt.close()

def plot_returns(dates,returns,ticker="Stock"):
    plt.figure(figsize=(12,6))
    plt.plot(dates[1:],returns,label=f'{ticker} Daily Returns',color='orange')
    plt.title(f'{ticker} Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{ticker.lower()}_returns.png')
    plt.close()

def plot_moving_average(dates,prices,ma_short,ma_long,ticker="Stock"):
    plt.figure(figsize=(12,6))
    plt.plot(dates,prices,label=f'{ticker} Price',alpha=0.5)
    plt.plot(dates[len(prices)-len(ma_short):],ma_short,label='20-Day MA',color='blue')
    plt.plot(dates[len(prices)-len(ma_long):],ma_long,label='50-Day MA',color='red')
    plt.title(f'{ticker} Price With MA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{ticker.lower()}_ma.png')
    plt.close()

def plot_cov_matrix(cov_matrix,tickers):
    plt.figure(figsize=(8,8))
    plt.imshow(cov_matrix,cmap='coolwarm')
    plt.colorbar()
    plt.xticks(range(len(tickers)),tickers)
    plt.yticks(range(len(tickers)),tickers)
    plt.title('Covariance Matrix')
    for i in range(len(tickers)):
        for j in range(len(tickers)):
            plt.text(j,i,f'{cov_matrix[i,j]:.4f}',ha='center',va='center',color='white')
    plt.savefig('cov_matrix.png')
    plt.close()

def main():
    np.random.seed(42)
    tickers=['AAPL','GOOGL','MSFT','AMZN']
    stock_data={}
    returns_data={}

    print("生成股票数据")
    for tick in tickers:
        mu=np.random.uniform(0.06,0.12)
        sigma=np.random.uniform(0.15,0.28)
        date,price=generate_stock_prices(np.random.uniform(80,200),252,mu,sigma)
        stock_data[tick]={'dates':date,'prices':price}
        print(f"{tick} start:{price[0]:.2f} end:{price[-1]:.2f}")

    print("\n计算日收益率")
    for tick in tickers:
        p=stock_data[tick]['prices']
        ret=calculate_daily_returns(p)
        returns_data[tick]=ret
        print(f"{tick} mean return:{np.mean(ret):.4f} max:{np.max(ret):.4f} min:{np.min(ret):.4f}")

    print("\n计算年化波动率")
    for tick in tickers:
        vol=calculate_volatility(returns_data[tick])
        print(f"{tick} annual vol:{vol:.2%}")

    print("\n计算移动均线")
    for tick in tickers:
        p=stock_data[tick]['prices']
        ma20=calculate_moving_average(p,20)
        ma50=calculate_moving_average(p,50)
        stock_data[tick]['ma20']=ma20
        stock_data[tick]['ma50']=ma50
        print(f"{tick} ma20 last:{ma20[-1]:.2f} ma50 last:{ma50[-1]:.2f}")

    print("\n投资组合风险分析")
    ret_mat=np.array([returns_data[t] for t in tickers])
    cov,var,port_var,port_std=portfolio_risk_analysis(ret_mat)

    print("\n单资产风险")
    for idx,tick in enumerate(tickers):
        annual_std=np.sqrt(var[idx])*np.sqrt(252)
        print(f"{tick} var:{var[idx]:.6f} vol:{annual_std:.2%}")

    print("\n协方差矩阵")
    print(np.round(cov,4))
    port_vol=port_std*np.sqrt(252)
    print(f"\n组合方差:{port_var:.6f} 组合年化波动:{port_vol:.2%}")

    print("\n生成图表")
    for tick in tickers:
        d=stock_data[tick]['dates']
        p=stock_data[tick]['prices']
        r=returns_data[tick]
        m20=stock_data[tick]['ma20']
        m50=stock_data[tick]['ma50']
        plot_stock_prices(d,p,tick)
        plot_returns(d,r,tick)
        plot_moving_average(d,p,m20,m50,tick)
    plot_cov_matrix(cov,tickers)
    print("图片保存完成")

if __name__=="__main__":
    main()