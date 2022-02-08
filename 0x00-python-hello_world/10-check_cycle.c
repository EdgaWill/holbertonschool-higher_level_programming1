#include "lists.h"
/**
 * check_cycle - checks if a linked
 * @list: linked list
 *
 * Return: 1
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;

	if (!list)
		return (0);

	while (hare && hare->next != NULL && hare->next->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (hare == turtle)
			return (1);
	}
	return (0);
}
