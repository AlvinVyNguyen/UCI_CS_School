#include <iostream>
#include "String.h"
using namespace std;


void test_constructor_and_assignment()
{
	String s1 = "Hello";
	String s2("World");
	String s3 = "Replaced";
	
	cout << "----------------------------------" << endl;
	cout << "Testing constructor and assignment" << endl;
	cout << "----------------------------------" << endl;

	cout << s1 << "\nShould be Hello" << endl;
	cout << s2 << "\nShould be World" << endl;
	
	s1 = s3;
	
	cout << s1 << "\nShould be Replaced" << endl;
}
void test_index_and_indexOf()
{
	String s1("Hello");
	
	cout << "----------------------------------" << endl;
	cout << "    Testing index and indexOf     " << endl;
	cout << "----------------------------------" << endl;

	cout << s1[3] << "\nShould be l" << endl;
	cout << s1[5] << "\nShould be error" << endl;
	
	cout << s1.indexOf('e') << "\nShould be 1" << endl;
	cout << s1.indexOf('p') << "\nShould be -1" << endl;
}
void test_relationals()
{
	String s1 = "Hello";
	String s3 = "Hello";

	cout << "----------------------------------" << endl;
	cout << "       Testing relationals        " << endl;
	cout << "----------------------------------" << endl;

	cout << (s1 == s3) << "\nShould be true/1" << endl;
	cout << (s1 < s3) << "\nShould be false/0" << endl;
}
void test_concat()
{
	String s1 = "Hello";
	String s2 = "World";
	
	cout << "----------------------------------" << endl;
	cout << "          Testing concat          " << endl;
	cout << "----------------------------------" << endl;

	cout << (s1 + s2) << "\nShould be HelloWorld" << endl;
	cout << s1 << "\nShould be Hello" << endl;
	cout << (s1+=s2) << "\nShould be HelloWorld" << endl;	
}
void test_read()
{
	String s1 = "";
	
	cout << "----------------------------------" << endl;
	cout << "           Testing read           " << endl;
	cout << "----------------------------------" << endl;

	cin >> s1;
	cout << s1 << endl;
}

int main()
{
	test_constructor_and_assignment();
	test_index_and_indexOf();
	test_relationals();
	test_concat();
	test_read();
	return 0;
}
