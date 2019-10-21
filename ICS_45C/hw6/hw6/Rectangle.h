#ifndef Rectangle_h
#define Rectangle_h
#include "Shape.h"
#include "Square.h"

class Rectangle
	: public Square
{

protected:
	double width;
	double rect_area = side * width;
	int start = 1;

public:
	Rectangle(int x, int y, string n, double h , double w )
		: Square( centerX = x, centerY = y, name = n, h ), width( w )
	{}

	virtual double area()
	{
		return rect_area;
	}
	virtual void draw()
	{
		cout << name << endl;
		int a;
		int b;
		for(a = start; a <= side; ++a )
		{
			for( b = start; b <= width; ++b )
				cout << " .";
			cout << endl;
		}
	}
};

#endif
