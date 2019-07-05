#define begin {
#define repeat do{
#define until(COND) }while(!(COND))
#define end }

int fromPascalToCpp(int Sum, int finish, int start)
{
	begin
		repeat
		  Sum = Sum + start;
	    start = start + 1;
	  until(start>=finish);
	end;
	return Sum;
}