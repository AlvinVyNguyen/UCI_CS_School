#include <iostream>
#include "String.h"
using namespace std;

//PRIVATE

String::ListNode * String::ListNode::stringToList( const char *s )
{
	return !*s ? nullptr : new String::ListNode( *s, stringToList( (s+1) ) );
}
String::ListNode * String::ListNode::copy( ListNode * L )
{
	return !L ? nullptr : new String::ListNode( L->info, String::ListNode::copy( L->next ) );
}
bool String::ListNode::equal( ListNode *L1, ListNode *L2 )
{
	for( ; L1 && L2; L1 = L1->next, L2 = L2->next )
		if( L1->info != L2->info )
			return false;
	return !L1 && !L2;
}
String::ListNode * String::ListNode::concat( ListNode *L1, ListNode *L2 )
{
	return !L1 ? String::ListNode::copy( L2 )
		: new ListNode( L1->info, String::ListNode::concat( L1->next, L2 ) );
}
int String::ListNode::compare( ListNode *L1, ListNode *L2 )
{
	if( String::ListNode::equal( L1, L2 ) ) return 0;
	for( ; L1 && L2; L1 = L1->next, L2 = L2->next )
	{
		if ( L1->info < L2->info )
			return -1;
		else if( L1->info > L2->info )
			return 1;
	}
}
void String::ListNode::deleteList( ListNode *L )
{
	if( L )
	{
		String::ListNode::deleteList( L->next );
		delete L;
	}
}
int String::ListNode::length( ListNode *L )
{
	return !L ? 0 : 1 + length( L->next );
}
void String::error( char const *msg )
{
	cerr << "Error: " << msg << endl;
}

//PUBLIC

String::String( const char *s )
	: head( ListNode::stringToList( s ) ) 
{	
}
String::String( const String & s )
	: head( ListNode::copy( s.head ) )
{
}
String String::operator = ( const String & s )
{
	ListNode::deleteList( head );
	this->head = ListNode::copy( s.head );
	return *this;
}
char & String::operator [] ( const int index )
{
	if ( !inBounds( index ) ) 
	{
		error( "Out of bounds" );
		return head->info;
	}
	ListNode *p = head;
	for( int i = 0; i < index; ++i )
		p = p->next;
	return p->info;	
}
int String::indexOf( char c ) const
{
	int i = 0;
	for( ListNode *p = head; p != nullptr; p = p->next)
	{	
		if( p->info == c)
			return i;
		++i;
	}
	return -1;
}
bool String::operator == ( const String & s ) const
{
	return ListNode::equal( this->head, s.head );
}
bool String::operator < ( const String & s ) const
{
	return ListNode::compare( this->head, s.head ) == -1 ? true : false;
}
String String::operator + ( const String & s ) const
{
	String newString = "";
	newString.head = ListNode::concat( head, s.head );
	return newString;
}
String String::operator += ( const String & s )
{
	ListNode *temp = ListNode::concat( head, s.head );
	ListNode::deleteList( head );
	this->head = ListNode::concat( '\0', temp );
	ListNode::deleteList( temp );
	return *this;
}
void String::print( ostream & out )
{
	for( ListNode *p = head; p != nullptr; p = p->next )
		out << p->info;
}
void String::read( istream & in )
{
	char s[128];
	in >> s;
	ListNode *temp = ListNode::stringToList( s );
	ListNode::deleteList( head );
	head = ListNode::concat( '\0', temp );
	ListNode::deleteList( temp );
}
String::~String()
{
	ListNode::deleteList( head );
}

//OSTREAM AND ISTREAM
ostream & operator << ( ostream & out, String s )
{
	s.print(out);
	return out;
}
istream & operator >> ( istream & in, String & s )
{
	s.read(in);
	return in;
}
