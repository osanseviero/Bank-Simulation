import xlsxwriter
import sys

class WorkSheet:

	def __init__(self, count):
		self.workbook = xlsxwriter.Workbook('results/' + str(sys.argv[1]) + '/simulation' + str(count) + '.xlsx')
		self.analysis = self.workbook.add_worksheet('summary and analysis')
		self.worksheet1 = self.workbook.add_worksheet('830to900')
		self.worksheet2 = self.workbook.add_worksheet('900to930')
		self.worksheet3 = self.workbook.add_worksheet('930to1000')
		self.worksheet4 = self.workbook.add_worksheet('1000to1030')
		self.worksheet5 = self.workbook.add_worksheet('1030to1100')
		self.worksheet6 = self.workbook.add_worksheet('1100to1130')
		self.worksheet7 = self.workbook.add_worksheet('1130to1200')
		self.worksheet8 = self.workbook.add_worksheet('1200to1230')
		self.worksheet9 = self.workbook.add_worksheet('1230to1300')
		self.worksheet10 = self.workbook.add_worksheet('1300to1330')
		self.worksheet11 = self.workbook.add_worksheet('1330to1400')
		self.worksheet12 = self.workbook.add_worksheet('1400to1430')
		self.worksheet13 = self.workbook.add_worksheet('1430to1500')
		self.worksheet14 = self.workbook.add_worksheet('1500to1530')
		self.worksheet15 = self.workbook.add_worksheet('after')

		self.bold = self.workbook.add_format({'bold': True})

		self.setStyle()
		self.row = 0
		self.col = 0

	
	def printBold(self, ws, text):
		ws.write(self.row, self.col, text, self.bold)

	def getWorksheets(self):
		return [self.worksheet1, self.worksheet2, self.worksheet3,
				self.worksheet4, self.worksheet5, self.worksheet6, self.worksheet7,
				self.worksheet8, self.worksheet9, self.worksheet10, self.worksheet11,
				self.worksheet12, self.worksheet13, self.worksheet14, self.worksheet15]

	def getWorksheet(self, n):
		return self.getWorksheets()[n]

	def setStyle(self):
		self.analysis.set_column(0, 0, 30)

		for ws in self.getWorksheets():
			ws.set_column(0, 0, 30)

	def close(self):
		self.workbook.close()

	