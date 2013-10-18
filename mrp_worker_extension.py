from osv import fields, osv
import openerp.addons.decimal_precision as dp

class mrp_worker_extension(osv.osv_memory):

    _name='mrp.product.produce'
    _inherit='mrp.product.produce'
    
    _columns={
        'produced_qty': fields.float('Produced Quantity', digits_compute=dp.get_precision('Product Unit of Measure'), required=False),
    }
    
    def _get_produced_qty(self, cr, uid, context=None):
        print '_get_produced_qty()'
        print 'context ' + str(context)
        done = 0.0
        return done
        
    def _get_product_qty(self, cr, uid, context=None):
        
        if context is None:
            context = {}
        prod = self.pool.get('mrp.production').browse(cr, uid, context['active_id'], context=context)
        done = 0.0
        for move in prod.move_created_ids2:
            if move.product_id == prod.product_id:
                if not move.scrapped:
                    done += move.product_qty
        if prod.product_uos_qty > 0.0:
            return prod.product_uos_qty

        return (prod.product_qty - done) or prod.product_qty

    def do_produce(self, cr, uid, ids, context=None):
        print 'mrp_worker_extension.do_produce()'
        super(mrp_worker_extension, self).do_produce(cr, uid, ids, context=context)
        # get produced product's latest stock move and display a form
        prod = self.pool.get('mrp.production').browse(cr, uid,context['active_id'], context=context)
        print 'latest move: ' + str(prod.move_created_ids2)
        cr.execute("select * from ir_model_data where name = 'mrp_extension_view'")
        resource_id = cr.dictfetchall()[0]['res_id']

        return {
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
    _defaults = {
        'product_qty': _get_product_qty,
        'produced_qty': _get_produced_qty
    }

mrp_worker_extension()

