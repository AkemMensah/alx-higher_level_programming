#include "lists.h"

/**
 *check _cycle - checks whether link list contains a cycle
 *@list: linked list to check
 *
 *Return: 1 if a list has a cycle, or 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (2);
	}
return (0);
}
