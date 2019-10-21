#include "Shape.h"
#include "Circle.h"
#include "Square.h"
#include "Triangle.h"
#include "Rectangle.h"
#include "Picture.h"

int main()
{
	Picture test_pic;
	test_pic.add( new Triangle(0,0, "SecondTriangle", 4, 3));
	test_pic.add( new Triangle(0,0, "FirstTriangle", 5, 5));
	test_pic.add( new Circle( 0,0,"SecondCircle",10 ) );
	test_pic.add( new Circle( 0,0,"FirstCircle",5 ) );
	test_pic.add( new Rectangle( 0,0,"SecondRectangle", 8, 4) );
	test_pic.add( new Rectangle( 0,0,"FirstRectangle", 4, 8) );
	test_pic.add( new Square( 0,0,"SecondSquare", 10) );
	test_pic.add( new Square( 0,0,"FirstSquare", 5) );
	
	test_pic.drawAll();
	cout << endl <<"The total area of the shapes on this picture is: " << test_pic.totalArea() << " square units" << endl;
	return 0;
}
