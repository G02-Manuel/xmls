from xmlrpc import client


common = client.ServerProxy(url + 'xmlrpc/common')
user = common.login(db, user, pwd)

print(f"User: {user}")

model = 'res.partner'
search = []
method = 'search'

operation = client.ServerProxy(url + '/xmlrpc/object')
list_of_partner_ids = operation.execute_kw(db, user, pwd, model, method, search)
print(list_of_partner_ids)