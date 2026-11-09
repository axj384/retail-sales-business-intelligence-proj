from pathlib import Path
import pandas as pd, sqlite3, matplotlib.pyplot as plt
p=Path(__file__).resolve().parent; d=pd.read_csv(p/'data/sample_data.csv'); (p/'outputs').mkdir(exist_ok=True)
assert d.order_id.is_unique and d.revenue.ge(0).all()
category=d.groupby('category',as_index=False).agg(revenue=('revenue','sum'),orders=('order_id','nunique')).sort_values('revenue',ascending=False)
category.to_csv(p/'outputs/category_summary.csv',index=False)
monthly=d.assign(month=d.order_date.str[:7]).groupby('month').revenue.sum()
ax=monthly.plot(figsize=(10,4),marker='o',title='Monthly Retail Revenue (synthetic)');ax.set_ylabel('Revenue ($)');plt.xticks(rotation=45);plt.tight_layout();plt.savefig(p/'figures/monthly_revenue.png');plt.close()
with sqlite3.connect(p/'outputs/retail.db') as con:d.to_sql('retail_orders',con,if_exists='replace',index=False)
print('Revenue:',round(d.revenue.sum(),2),'Orders:',d.order_id.nunique());print(category.to_string(index=False))
