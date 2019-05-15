import xml.dom.minidom

dom = xml.dom.minidom.parse('transactions.xml')
rootdata = dom.documentElement

itemlist_trans = rootdata.getElementsByTagName('transaction')
itemlist_from = rootdata.getElementsByTagName('from')
itemlist_to = rootdata.getElementsByTagName('to')
itemlist_amount = rootdata.getElementsByTagName('amount')


# itemlist_amount_attr = itemlist_amount[0]
# itemlist_amount_attrname = itemlist_amount_attr.getAttribute("currency")


for i in range(len(itemlist_amount)):
    if itemlist_amount[i].getAttribute("currency") == 'USD':
        print(f"from {itemlist_from[i].firstChild.data} to {itemlist_to[i].firstChild.data} USD amount {itemlist_amount[i].firstChild.data}")
    