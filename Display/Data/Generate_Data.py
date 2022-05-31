import alpaca_trade_api as alpaca
import matplotlib.pyplot as plt

api = alpaca.REST('PKJ7TUUMCUZ7PDY2PRTJ', 'jfFmk7yr6OdfeM5Px2CoYtcQxx6BQvJ7H2h52f1L', 'https://paper-api.alpaca.markets')

portfolio = api.list_positions()
positions = []
pos_val = {}
for position in portfolio:
    positions.append(position.symbol)
    pos_val[position.symbol] = float(position.unrealized_pl)

pos_val_sort = (sorted(pos_val.items(), key=lambda item: item[1]))
pos_val_loss = [i for i in pos_val_sort if i[1] < 0]
pos_val_gain = [i for i in pos_val_sort if i[1] > 0]

loss_labels = [i[0] for i in pos_val_loss][:4]
loss_labels.append("Other")
loss_sizes = [i[1] for i in pos_val_loss][:4]
loss_sizes.append(sum([i[1] for i in pos_val_loss][5:]))
loss_sizes = [ -x for x in loss_sizes]

gain_labels = [i[0] for i in pos_val_gain][-5:]
gain_labels.append("Other")
gain_sizes = [i[1] for i in pos_val_gain][-5:]
gain_sizes.append(sum([i[1] for i in pos_val_gain][:-5]))

fig = plt.figure()
loss_pie = fig.add_subplot(121)
loss_pie.pie(loss_sizes, labels = loss_labels, shadow = True, startangle = 90)
loss_pie.axis('equal')
plt.title("Pie Chart showing percentages of losses by asset")

gain_pie = fig.add_subplot(122)
gain_pie.pie(gain_sizes, labels = gain_labels, shadow = True, startangle = 90)
gain_pie.axis('equal')
plt.title("Pie Chart showing percentages of gain by asset")
plt.tight_layout()
plt.show()

fig.savefig('pie_charts.png', bbox_inches="tight")