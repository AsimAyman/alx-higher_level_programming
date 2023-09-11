#include "lists.h"
/**
 * recurPalindrome - checks if singly linked list is palindrome
 * @left: pointer to head of singly linked list
 * @right: head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int recurPalindrome(listint_t **left, listint_t *right)
{
	int r;

	if (right == NULL)
		return (1);

	r = recurPalindrome(left, right->next);
	if (r == 0)
		return (0);

	r = (right->n == (*left)->n);

	*left = (*left)->next;

	return (r);
}
/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (recurPalindrome(head, *head));
}
