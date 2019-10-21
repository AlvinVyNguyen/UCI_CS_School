#ifndef Triangle_h
#define Triangle_h
#include "Shape.h"

class Triangle
	: public Shape
{
private:
	double base;
	double height;
	int doubled = 2;
	double total_area = base * height;
	int start = 1;
public:
	Triangle( int x, int y, string n, double h, double b )
		: Shape( centerX = x, centerY = y, name = n), height( h ), base( b )
	{}

	virtual double area()
	{
		return total_area / doubled;
	}

	virtual void draw()
	{
		cout << name << endl;
		int a;
		int b;
		if( base != height )
		{	for( a = start; a <= height-start; ++a )
			{
				for(b = start; b <= a && b <= base-start; ++b )
				{
					cout << " .";
				}
				cout << endl;
			}
			for( b = start; b <= base; ++b )
			{
				cout << " .";
			}
			cout << endl;
			
		}
		else
		{
			for( a = start; a <= height; ++a )
			{
				for( b = start; b <= a; ++b )
					cout << " .";
				cout << endl;
			}
		}
	}
};

#endif
