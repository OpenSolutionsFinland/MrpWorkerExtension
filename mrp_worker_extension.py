from osv import fields, osv

class mrp_worker_extension(osv.osv_memory):
	_name='mrp.product.produce'
	_inherit='mrp.product.produce'

	def do_produce(self, cr, uid, ids, context=None):
		print 'mrp_worker_extension.do_produce()'
		super(mrp_worker_extension, self).do_produce(cr, uid, ids, context=context)
		# get produced product's latest stock move and display a form
		prod = self.pool.get('mrp.production').browse(cr, uid,context['active_id'], context=context)
		print 'latest move: ' + str(prod.move_created_ids2)
		cr.execute("select * from ir_model_data where name = 'mrp_extension_view'")
		resource_id = cr.dictfetchall()[0]['res_id']

		return {
			'name': "mrp_worker_extension.mrp_extension_view",
			'view_id': 'mrp_worker_extension.mrp_extension_view',
			"views": [(resource_id,'form')],
			"type": "ir.actions.act_window",
			'view_type': 'form',
			'res_model': 'stock.move',
			'res_id': prod.move_created_ids2[len(prod.move_created_ids2)-1].id,
			'view_mode': 'form',
			'target': 'new',
			'context': context,
		}

mrp_worker_extension()

