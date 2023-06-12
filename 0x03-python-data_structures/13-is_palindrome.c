#include "lists.h"

/**
 * reverse_linked_list - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_linked_list(listint_t **head)
{
	listint_t *prev_node = NULL;
	listint_t *current_node = *head;
	listint_t *next_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}

	*head = prev_node;
}

/**
 * is_linked_list_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_linked_list_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, 
              *fast_ptr = *head, 
              *temp_ptr = *head, 
              *dup_ptr = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
      
        if (!fast_ptr) {
			dup_ptr = slow_ptr->next;
			break;
        }
        
        if (!fast_ptr->next) {
			dup_ptr = slow_ptr->next->next;
			break;          
        }
        
		slow_ptr = slow_ptr->next;      
	}

	reverse_linked_list(&dup_ptr);

	while (dup_ptr && temp_ptr)
	{
		if (temp_ptr->n == dup_ptr->n)
		{
			dup_ptr = dup_ptr->next;
			temp_ptr = temp_ptr->next;
		}
		else
			return (0);
	}

	if (!dup_ptr)
		return (1);

	return (0);
}
