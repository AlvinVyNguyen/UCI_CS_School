#ifndef Circle_h
#define Circle_h
#include "Shape.h"
#include <math.h>

class Circle: public Shape
{

protected:
	double radius;

private:
	double radius_squared = radius * radius;

public:
	Circle(int x, int y, string n, double circle_r )	
		: Shape(centerX = x, centerY = y, name = n ), radius( circle_r )
	{}

	virtual double area()
	{
		return 3.14 * radius_squared;
	}

	virtual void draw()
	{
		cout << name << endl;
		int start = 1;
		int y;
		int x;
		int radius_mult = radius*2;
		for( y = start; y <= radius_mult; ++y )
		{ 
			for(x = start; x <= radius_mult; ++x )
			{
				int real_radiusx = x-radius;
				int real_radiusy = y-radius;
				int combined_radiusx = real_radiusx * real_radiusx;
				int combined_radiusy = real_radiusy * real_radiusy;
				int formula_circle = combined_radiusy + combined_radiusx;
				double distance = sqrt(formula_circle);
				if( distance < radius )
					cout << " .";
				else
					cout << "  ";
			}
			cout << endl;
		}			
	}
	~Circle()
	{
	;
	}
};



#endif
