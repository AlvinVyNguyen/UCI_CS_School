#ifndef Square_h
#define Square_h
#include "Shape.h"

class Square
	: public Shape
{
protected:
	double side;
	double doubledside = side*side;
	int start = 1;
public:
	Square( int x, int y, string n, double s )
		: Shape(centerX = x, centerY = y, name = n), side( s )
	{}

	virtual double area()
	{
		return doubledside;
	}

	virtual void draw()
	{
		cout << name << endl;
		int a;
		int b;
		for(a = start; a <= side; ++a ) 
		{
			for(b= start; b <= side; ++b )
				cout << " .";
			cout << endl;
		}
	}
	~Square()
	{
	;
	}
};

#endif
