#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted
 * singly linked list
 * @head: double pointer
 * @number: number to insert
 *
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp_head, *prev_node;

	tmp_head = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (tmp_head)
	{
		if (tmp_head->n > number)
		{
			break;
		}
		prev_node = tmp_head;
		tmp_head = tmp_head->next;
	}
	new->next = tmp_head;
	prev_node->next = new;
	return (*head);
}
