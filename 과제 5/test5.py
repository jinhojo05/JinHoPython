class contact:

	book = [];
	count = 0

	def __init( self ):
		count = 0;

	def add( self, name, phonenumber ):
		temp_book = []
		print( '추가할 연락처를 입력하세요.' )
		print('name:', name)
		print('number:', phonenumber)

		temp_book.append( name );
		temp_book.append( phonenumber );

		self.book.append( temp_book )
		self.count = self.count + 1;
		#book.append( phonenumber )
		print('연락처를 추가하였습니다.\n')

	def delete( self, name, phonenumber ):
		temp_book = []

		temp_book.append( name )
		temp_book.append( phonenumber )

		print('삭제할 이름을 입력하세요.')
		print('name:', name)
		self.count = self.count - 1;
		self.book.remove( temp_book )
		print('연락처가 삭제되었습니다.\n')

	def printbook(self):
		for i in range(0, self.count ):
			print( 'name:', self.book[i][0] )
			print('name:', self.book[i][1])
			print('-------------------------')
			#print( 'number:', s)


contact_1 = contact()

contact_1.add( "다현", "111-111" )
contact_1.add( "나연", "222-222" )
contact_1.add( "지영", "333-333" )
contact_1.delete( "나연", "222-222" )
contact_1.printbook()




