#include "lists.h"
/**
 * is_palindrome - function in C that checks if a singly
 * linked list is a palindrome
 * @head: double pointer
 *
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (checker(head, *head));
}

/**
 * checker - function in C that checks if a singly
 * linked list is a palindrome
 * @head: double pointer
 * @last: pointer
 *
 * Return: 1
 */
int checker(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (checker(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
