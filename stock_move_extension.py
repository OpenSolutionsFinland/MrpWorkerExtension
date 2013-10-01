from osv import fields, osv
from datetime import datetime
import pytz

class stock_move_extension(osv.osv):
	_name = 'stock.move'
	_inherit = 'stock.move'

	_columns = {
		'product_quality_text': fields.related('product_id','x_quality_checks',type='text', relation="product.product", string="Quality"),
		'product_quality_lower_limit': fields.related('product_id','x_quality_lower_limit',type='float', relation="product.product", string="Lower Limit"),
		'product_quality_upper_limit': fields.related('product_id','x_quality_upper_limit',type='float', relation="product.product", string="Upper Limit"),
		'product_quality_weight': fields.float('Weight', required=False),
		'inspected_by': fields.char('Inspector', size=64, required=False, translate=True),
		'localized_date': fields.datetime('Localized Date'),
	}

	def onPrintLabelClicked(self, cr, uid, ids, context=None):
		print 'onPrintLabelClicked'
		datas = {'ids':ids}
 		# Change localized date accordingly
        
		#print str(localDate)
 		print str(ids)

		dateString = self.browse(cr, uid, ids, context=None)[0].date
        
		print 'creation date: ' + dateString
 		utcDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

		utcDate = utcDate.replace(tzinfo=pytz.utc)

		local = datetime.astimezone(utcDate, pytz.timezone("EET"))
		self.write(cr, uid, ids, {'localized_date':local}, context)
		# save current data from the form
		print str(context)
		#self.write(cr, uid, ids, context)

		#print 'localized date: ' + str(self.x_localized_date)
		if context is None:
			print 'no context'
			context = {}
			datas = {}
		
		if not self.browse(cr, uid, ids, context=None)[0].inspected_by:
			raise osv.except_osv('Error', 'Aseta tarkastaja')


		return {
			'type' : 'ir.actions.report.xml',
			'report_name' : 'stock.move.extended.label',
			'datas' : datas,
		}

stock_move_extension()
