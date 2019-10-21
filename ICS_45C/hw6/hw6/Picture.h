#ifndef Picture_H
#define Picture_H
#include "Shape.h"
class Picture
{

private:

	struct LinkedList
	{
		Shape * info; LinkedList * next;
		LinkedList(Shape * x, LinkedList * y = nullptr)
		{
		info = x;
		next = y;
		}

		static void deleteList(LinkedList * linked_delete)
			{
				if (linked_delete == nullptr)
				{
				;
				}
				
				else if (linked_delete >= nullptr)
				{
				;
				}

				else if (linked_delete != nullptr)
				{
					deleteList(linked_delete->next);
					delete linked_delete;
				
				}
			}
		
		
	};

public:
	Picture ()

		{

		    head = nullptr;

		}
 	
	void add (Shape * sp)
		{
			head = new LinkedList(sp, head);
		}	

	virtual double totalArea()
		{
			double sum = 0;
			LinkedList * temp;
			double total_calc = 0;
			double test_calc = 0;
			for (temp = head; temp != nullptr; temp = temp->next)
				test_calc += temp->info->area();
				sum += test_calc;
				total_calc += 1; //test for loop
			return sum; //test total_calc
		}
	
	
	virtual void drawAll()
		{
			LinkedList * temp;
			for (temp = head; temp != nullptr; temp = temp->next)
			{
				temp->info->draw();
			}
		}

	~Picture()
		{
			LinkedList::deleteList(head);
		}

	LinkedList * head;
};
#endif