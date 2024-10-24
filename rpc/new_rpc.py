import odoorpc



# Obtener todos los campos del modelo 'res.partner' en Odoo 11 (old_mec)
partner_fields = old_mec.env['res.partner'].fields_get()

# Obtener todos los contactos de old_mec (Odoo 11) con todos los campos
old_contacts = old_mec.env['res.partner'].search_read([], fields=list(partner_fields.keys()))

# Obtener los contactos de new_mec (Odoo 17) para filtrar por ID
new_contacts = new_mec.env['res.partner'].search_read([], fields=['id'])

# Convertir a un conjunto los IDs de los contactos en new_mec para comparación rápida
new_contact_ids = set(contact['id'] for contact in new_contacts)

# Total de contactos en old_mec para seguimiento
total = len(old_contacts)
count = 1
print('Total de contactos en old_mec: {}'.format(total))
# # Iterar sobre los contactos de old_mec y filtrar los que no están en new_mec
# for contact in old_contacts:
#     print('{} de {}'.format(count, total))
#     try:
#         # Verificar si el contacto ya existe en new_mec usando el ID como referencia
#         if contact['id'] not in new_contact_ids:
#             # Crear un diccionario con todos los campos del contacto
#             contact_data = {
#                 key: contact[key] if not isinstance(contact[key], tuple) else contact[key][0]  # Convertir los Many2one
#                 for key in partner_fields.keys()
#                 if key != 'id'  # Excluir 'id' del contacto de old_mec
#             }

#             # Crear el contacto en new_mec (Odoo 17) con todos los campos
#             new_mec.env['res.partner'].create({
#                 'id': contact['id'],  # Mantener el mismo ID de Odoo 11
#                 **contact_data  # Pasar todos los datos del contacto
#             })
#             print("Contacto creado: {}".format(contact['name']))
#         else:
#             print("El contacto ya existe en new_mec: {}".format(contact['name']))

#         count += 1

#     except Exception as e:
#         print("Error al procesar el contacto ID {}: {}".format(contact['id'], e))
#         count += 1
#         continue










































# AccountPayment = old_mec.env['account.payment'].search_read([
#     ('payment_type', '!=', 'inbound'), ('state', 'in', ['posted', 'sent', 'reconciled'])],
#     fields=['payment_type', 'journal_id', 'check_amount_in_words', 'check_manual_sequencing', 'check_number', 'payment_method_id'])
# print(AccountPayment)
# total = len(AccountPayment)
# count = 1
# for ap in AccountPayment:
#     print('{} de {}'.format(count, total))
#     try:
#         payment_method_line = new_mec.env['account.payment.method.line'].search_read([
#             ('payment_type', '=', ap['payment_type']),
#             ('journal_id', '=', ap['journal_id'][0]),
#             ('payment_method_id', '=', ap['payment_method_id'][0])], fields=['journal_id', 'payment_method_id'])
#         print('payment_method_line', payment_method_line)
#         new_mec.env['account.payment'].write(ap['id'], {
#             'check_amount_in_words': ap['check_amount_in_words'],
#             'check_manual_sequencing': ap['check_manual_sequencing'],
#             # 'check_number': ap['check_number'], #hacer por sql update account_payment set check_number = openupgrade_legacy_13_0_check_number;
#             'payment_method_id': ap['payment_method_id'][0],
#             'payment_method_line_id': payment_method_line[0]['id'],
#         })
#         count += 1
#     except:
#         count += 1
#         continue